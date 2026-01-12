import os
from extract import Extractor
from transform import Transformer
from load import Loader
from database import DB

def run_etl(bronze_dir, silver_dir, gold_dir):
   for file in os.listdir(bronze_dir):
      input_path = os.path.join(bronze_dir, file)

      data_extractor = Extractor(input_path)
      df = data_extractor.load_df_from_file()

      transfomer = Transformer(df)
      silver_df = transfomer.clean_sales_df()

      loader = Loader(file)
      loader.load_to_parquet(silver_df, silver_dir)

      gold_df = transfomer.create_gold_df(df)
      loader.load_to_parquet(gold_df, gold_dir)

      db = DB(gold_dir, file)
      db.load_df_to_database()
if __name__ == '__main__':
   bronze_dir= 'data/bronze'
   silver_dir = 'data/silver'
   gold_dir = 'data/gold'
   run_etl(bronze_dir, silver_dir, gold_dir)