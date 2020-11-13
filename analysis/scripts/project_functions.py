import pandas as pd
import numpy as np

def load_and_process(path):

    # Method Chain 1 (Load data and deal with missing data)

    df = (
          pd.read_csv(path)
          .dropna()
      
      )

    return df

