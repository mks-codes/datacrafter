import pandas as pd

def read_data(source):
    if isinstance(source, pd.DataFrame):
        return source.copy()
    elif isinstance(source, str):
        if source.endswith('.csv'):
            return pd.read_csv(source)
        elif source.endswith('.xlsx'):
            return pd.read_excel(source)
        else:
            raise ValueError("Unsupported file type")
    else:
        raise TypeError("Data source must be a DataFrame or a file path")

