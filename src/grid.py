import matplotlib.pyplot as plt
import seaborn as sns
from helpers import Measurement

class Grid():
    def __init__(self, meas):
        self.params = self.setup_grid(meas)

    def setup_grid(self, meas):
        # sets up the grid based on measurements
        output = {}
        height = (meas['le ba'] + 15)
        width = height / 2
        # TODO get based off 
        buffer = Measurement('1').raw
        output['ax_bot'] = -1 * buffer
        output['ax_top'] = height.raw - buffer
        output['ax_left'] = -0.5 * buffer
        output['ax_right'] = width.raw - 0.5 * buffer
        return output

    def graph_thing(self, thing):
        # inputs are expected to have points, lines, and guidelines
        # first guidelines
        n = 9
        f, ax = plt.subplots(figsize=(n/2, n))
        ax.set_xlim(left=self.params['ax_left'], right=self.params['ax_right'])
        ax.set_ylim(bottom=self.params['ax_bot'], top=self.params['ax_top'])
        
        for label, line in thing.lines.items():
            line.graph()
        
        plt.show()
        
