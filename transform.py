import pandas as pd

class Transformer:
   def __init__(self, dataframe : pd.DataFrame):
      self.dataframe = dataframe
   
   def _basic_cleaning(dataframe : pd.DataFrame):
      cleaned_df = dataframe.drop_duplicates()
      
         