import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, df, target=None):
        self.df = df
        self.target = target

    def show_all(self):
        print("\n--- Generating Visualizations ---")

        plt.figure(figsize=(8, 4))
        sns.heatmap(self.df.isnull(), cbar=False)
        plt.title("Missing Value Heatmap")
        plt.show()

        if self.target and self.target in self.df.columns:
            sns.countplot(x=self.df[self.target])
            plt.title(f"Distribution of Target: {self.target}")
            plt.show()

        self.df.hist(bins=20, figsize=(12, 10))
        plt.tight_layout()
        plt.show()