import os 
import pandas as pd

class Extractor:
   def __init__(self, input_path):
      self.input_path = input_path

   def load_df_from_file(self):
         file = os.path.split(self.input_path)
         file_name, ext = os.path.splitext(file[1])
         if ext.lower() == '.csv':
            df = pd.read_csv(self.input_path)
            return df

         else:
            print(f'File {file_name} ignored : {ext} not supported')
      
if __name__ == '__main__':
   data_extractor = Extractor('data/bronze/cafe_sales.csv')
   df = data_extractor.load_df_from_file()
   print(df)