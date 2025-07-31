class Analyzer:
    def __init__(self, df):
        self.df = df

    def show_summary(self):
        print("\n--- Shape ---")
        print(self.df.shape)

        print("\n--- Columns ---")
        print(self.df.columns.tolist())

        print("\n--- Info ---")
        print(self.df.info())

        print("\n--- Missing Values ---")
        print(self.df.isnull().sum())

        print("\n--- Describe ---")
        print(self.df.describe(include='all'))

