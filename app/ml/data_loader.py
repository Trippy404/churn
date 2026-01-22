import pandas as pd

class DataLoader:

    @staticmethod
    def load_csv(file) -> pd.DataFrame:
        return pd.read_csv(file)
