import os
from extract import Extractor
from transform import Transformer


# output_dir = 'data/silver'

def run_pipeline(input_dir):
   for file in os.listdir(input_dir):
      
      input_path = os.path.join(input_dir, file)
      print(input_path)
      data_extractor = Extractor(input_path)
      df = data_extractor.load_df_from_file()
      print(df)

      cleaner = Transformer(df)
      df = cleaner.clean_sales_df()
      print(df)
if __name__ == '__main__':
   input_dir= 'data/bronze'
   run_pipeline(input_dir)