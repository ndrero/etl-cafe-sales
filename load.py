import pandas as pd
import os
class Loader:
   def __init__(self, file):
      self.file_name = os.path.splitext(file)[0]

   def load_to_parquet(self, df: pd.DataFrame, output_dir):
      os.makedirs(output_dir, exist_ok=True)
      output_path = f'{os.path.join(output_dir, self.file_name)}.parquet'
      df.to_parquet(output_path)