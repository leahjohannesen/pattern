import matplotlib.pyplot as plt
import seaborn as sns

class Grid():
    def __init__(self):
        pass

    def graph_thing(self, thing):
        # inputs are expected to have points, lines, and guidelines
        # first guidelines
        for label, line in thing.guidelines.items():
            line.graph(kind='guide')

        for label, line in thing.lines.items():
            line.graph()
        
        plt.show()
        
