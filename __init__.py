# datacrafter/__init__.py
from .reader import read_data
from .analyzer import Analyzer
from .visualizer import Visualizer
from .cleaner import Cleaner
from .suggester import Suggester
from .pipeline import generate_pipeline

class DataCrafter:
    def __init__(self, data_source, target=None):
        self.data = read_data(data_source)
        self.target = target
        self.analyzer = Analyzer(self.data)
        self.visualizer = Visualizer(self.data, target)
        self.cleaner = Cleaner(self.data)
        self.suggester = Suggester(self.data, target)
        self.pipeline = None

    def analyze(self):
        self.analyzer.show_summary()

    def visualize(self):
        self.visualizer.show_all()

    def suggest_cleaning(self):
        self.suggester.show_suggestions()

    def transform(self, return_pipeline=False):
        clean_data = self.cleaner.clean_data()
        self.pipeline = generate_pipeline(clean_data, self.target)
        if return_pipeline:
            return clean_data, self.pipeline
        return clean_data
