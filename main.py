import os
import logging
from extract import Extractor
from transform import Transformer
from load import Loader
from database import DB

os.makedirs('logs', exist_ok=True)

logging.basicConfig(
   filename='logs/etl.log',
   filemode='a',
   format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
   level=logging.INFO
)

logger = logging.getLogger(__name__)

def run_etl(bronze_dir, silver_dir, gold_dir):
   logger.info('Starting ETL')

   if not os.path.exists(bronze_dir):
      logger.error(f'Directory {bronze_dir} does not exists')
      raise FileNotFoundError(f'Directory {bronze_dir} does not exists')
   
   files = os.listdir(bronze_dir)

   if not files:
      logger.error(f'Directory {bronze_dir} is empty')
      raise FileNotFoundError(f'Directory {bronze_dir} is empty')

   for file in os.listdir(bronze_dir):
      try:
         logger.info(f'Processing file: {file}')
         
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

         logger.info('Finished ETL run')

      except Exception:
         logger.error(f'Failed processing {file}')
         continue
      
if __name__ == '__main__':
   bronze_dir= 'data/bronze'
   silver_dir = 'data/silver'
   gold_dir = 'data/gold'
   run_etl(bronze_dir, silver_dir, gold_dir)