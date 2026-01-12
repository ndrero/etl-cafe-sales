import os
import duckdb

class DB:
   def __init__(self, parquet_dir, parquet_file):
      self.conn = duckdb.connect('data/warehouse.duckdb')
      self.file_name = os.path.splitext(parquet_file)[0]
      self.parquet_path = os.path.join(parquet_dir, self.file_name)
      
   def load_df_to_database(self):
      self.conn.execute(f"CREATE OR REPLACE TABLE {self.file_name} AS SELECT * FROM read_parquet('{self.parquet_path}.parquet')")

   