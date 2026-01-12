import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

class Transformer:
   def __init__(self, dataframe : pd.DataFrame):
      if not isinstance(dataframe, pd.DataFrame):
         logger.error('dataframe must be a pandas DataFrame')
         raise TypeError('dataframe must be a pandas DataFrame')
      self.dataframe = dataframe
   
   @staticmethod
   def __clean_df(df: pd.DataFrame):
      df.columns = [c.lower().replace(' ', '_') for c in df.columns]
      df.drop_duplicates(inplace=True)
      return df
   
   @staticmethod
   def __is_missing_flag(df, columns, value): 
      for column in columns:
         df.loc[(df[column] == value) | (df[column].isna()), 'is_missing'] = True

      return df
   
   @staticmethod
   def __is_error_flag(df, columns, value): 
      for column in columns:
         df.loc[df[column] == value, 'is_error'] = True

      return df
   
   def __define_flags(self, df):
      df['is_error'] = False

      df['is_missing'] = False

      columns_for_missing_flag = ['item', 'quantity', 'price_per_unit', 'total_spent', 'transaction_date']
      self.__is_missing_flag(df, columns_for_missing_flag, 'UNKNOWN')

      columns_for_error_flag = ['item', 'quantity', 'price_per_unit', 'total_spent']
      self.__is_error_flag(df, columns_for_error_flag, 'ERROR')

      return df

   @staticmethod
   def __change_value_types(df):
      df['price_per_unit'] = df['price_per_unit'].astype(float)

      df['total_spent'] = df['total_spent'].astype(float)

      df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').astype('Int64')

      df['transaction_date'] = pd.to_datetime(df['transaction_date'], utc=True)
      
      return df
   
   @staticmethod
   def __create_mapping_item_price(df):
      mapping_df = df.loc[
         (df['item'].notna()) & 
         (df['price_per_unit'].notna()),
         ['item', 'price_per_unit']].drop_duplicates()

      mapping_price_dict = dict(zip(mapping_df['item'], mapping_df['price_per_unit']))

      mapping_df.drop_duplicates(subset=['price_per_unit'], keep=False, inplace=True)

      mapping_item_dict = dict(zip(mapping_df['item'], mapping_df['price_per_unit']))

      return mapping_price_dict, mapping_item_dict
   
   def __infer_values(self, df):
      mapping_price_dict, mapping_item_dict = self.__create_mapping_item_price(df)

      for item, price in mapping_item_dict.items():
         mask = (df['item'].isna()) & (df['price_per_unit'] == price)
         df.loc[mask, 'item'] = item

      for item, price in mapping_price_dict.items():
         mask = (df['price_per_unit'].isna()) & (df['item'] == item)
         df.loc[mask, 'price_per_unit'] = price

      df.loc[
         (df['price_per_unit'].notna()) &
         (df['total_spent'].isna()) &
         (df['quantity'].notna()
         ), 'total_spent'] = df['price_per_unit'] * df['quantity']

      df.loc[
         (df['price_per_unit'].isna() &
         df['total_spent'].notna() &
         df['quantity'].notna()
         ), 'price_per_unit'] = df['total_spent']/df['quantity']

      return df

   def clean_sales_df(self):
      df = self.dataframe
      logger.info("Cleaning dataframe | rows=%d cols=%d", df.shape[0], df.shape[1])
      try:
         df = self.__clean_df(df)

         df = self.__define_flags(df)

         df.replace(['ERROR', 'UNKNOWN'], np.nan, inplace=True)

         df = self.__change_value_types(df)

         df = self.__infer_values(df)

         logger.info("Cleaned dataframe | rows=%d cols=%d", df.shape[0], df.shape[1])
         return df
      
      except Exception:
         logger.exception('Could not clean dataframe')
         raise

   @staticmethod
   def create_gold_df(df: pd.DataFrame):
      try:
         df['transaction_month'] =  pd.to_datetime(df['transaction_date']).dt.month_name()

         df['day_of_the_week'] = pd.to_datetime(df['transaction_date']).dt.day_name()

         return df
      
      except Exception:
         logger.exception('Could not create gold dataframe')
         raise