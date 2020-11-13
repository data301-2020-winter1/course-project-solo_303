import pandas as pd
import numpy as np
def load_and_process(path):

       #(Load data and deal with missing data)
    df = (
        pd.read_csv(path)
        .dropna()

        )
        return df

