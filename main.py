import os
from extract import Extractor
from transform import Transformer
from load import Loader


def run_pipeline(input_dir, output_dir):
   for file in os.listdir(input_dir):
      
      input_path = os.path.join(input_dir, file)

      data_extractor = Extractor(input_path)
      df = data_extractor.load_df_from_file()

      cleaner = Transformer(df)
      df = cleaner.clean_sales_df()

      loader = Loader(file, output_dir)
      loader.load_to_parquet(df)
if __name__ == '__main__':
   input_dir= 'data/bronze'
   output_dir = 'data/silver'
   run_pipeline(input_dir, output_dir)