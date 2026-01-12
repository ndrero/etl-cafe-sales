import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

class Loader:
   def __init__(self, file):
      self.file_name = os.path.splitext(file)[0]

   def load_to_parquet(self, df: pd.DataFrame, output_dir):
      if not isinstance(df, pd.DataFrame):
         logger.error('df must be a pandas Dataframe')
         raise TypeError('df must be a pandas Dataframe')

      logger.info(f'Loading {self.file_name} to parquet')
      
      try:
         os.makedirs(output_dir, exist_ok=True)
         output_path = f'{os.path.join(output_dir, self.file_name)}.parquet'
         df.to_parquet(output_path)

         logger.info(f'Successfully saved to {output_path}')
         return output_path
      
      except Exception:
         logger.exception(f'Could not load {self.file_name} to parquet')
         raise