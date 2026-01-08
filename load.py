import pandas as pd
import os

class Loader:
   def __init__(self, file, output_dir):
      self.file_name = os.path.splitext(file)[0]
      self.output_dir = output_dir
      os.makedirs(output_dir, exist_ok=True)
      self.output_path = f'{os.path.join(self.output_dir, self.file_name)}.parquet'
   def load_to_parquet(self, df: pd.DataFrame):
      df.to_parquet(self.output_path)