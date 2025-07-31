class Suggester:
    def __init__(self, df, target=None):
        self.df = df
        self.target = target

    def show_suggestions(self):
        print("\n--- Suggestions ---")
        nulls = self.df.isnull().sum()
        print(f"Fill missing values using mean/mode (Total missing: {nulls[nulls > 0].sum()})")

        nunique = self.df.nunique()
        high_card = nunique[nunique > 20]
        if not high_card.empty:
            print(f"High cardinality columns: {high_card.index.tolist()} → Consider encoding or dropping")

        if self.target and self.df[self.target].dtype == 'object':
            print(f"Target column '{self.target}' is categorical → Use classification models")
        elif self.target:
            print(f"Target column '{self.target}' is numeric → Use regression models")

