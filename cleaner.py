class Cleaner:
    def __init__(self, df):
        self.df = df

    def clean_data(self):
        df = self.df.copy()

        # Drop constant columns
        nunique = df.nunique()
        const_cols = nunique[nunique == 1].index
        df.drop(columns=const_cols, inplace=True)

        # Fill missing numerics with mean, categoricals with mode
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col].fillna(df[col].mode()[0], inplace=True)
            else:
                df[col].fillna(df[col].mean(), inplace=True)

        return df