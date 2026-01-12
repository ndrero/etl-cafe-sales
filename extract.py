import os 
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class Extractor:
   def __init__(self, input_path):
      self.input_path = input_path

   def load_df_from_file(self):
      file = os.path.split(self.input_path)
      file_name, ext = os.path.splitext(file[1])

      if ext.lower() != '.csv':
         logger.error(f'File {file_name} ignored : {ext} not supported')
         return 

      try:
         df = pd.read_csv(self.input_path)
         logger.info(f'File {file_name} extracted succesfully')
         return df  
      
      except Exception as e: 
         logger.exception(f'Error while extracting file {file_name}: {e}')
         raise
      
if __name__ == '__main__':
   data_extractor = Extractor('data/bronze/cafe_sales.csv')
   df = data_extractor.load_df_from_file()