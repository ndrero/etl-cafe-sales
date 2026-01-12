import os
import duckdb
import logging

logger = logging.getLogger(__name__)

class DB:
   def __init__(self, parquet_dir, parquet_file):
      logger.info('Connecting to database')
      try:
         self.conn = duckdb.connect('data/warehouse.duckdb')
         logger.info('Connected to database')
      except Exception:
         logger.exception('Failed to connect to database')
         raise 

      self.file_name = os.path.splitext(parquet_file)[0]
      self.table_name = self.file_name.replace("-", "_").replace(" ", "_")
      self.parquet_path = os.path.join(parquet_dir, f"{self.file_name}.parquet")

      if not os.path.exists(self.parquet_path):
         logger.error(f'Path {self.parquet_path} does not exists')
         raise FileNotFoundError(f'Path {self.parquet_path} does not exists')
      
   def load_df_to_database(self):
      logger.info(f'Loading {self.file_name} parquet to database')
      try:
         self.conn.execute(f"CREATE OR REPLACE TABLE {self.table_name} AS SELECT * FROM read_parquet('{self.parquet_path}')")
         logger.info(f'Successfully loaded {self.file_name} parquet to database')

      except Exception:
         logger.exception(f'Failed to load {self.file_name} parquet to database')
         raise

   