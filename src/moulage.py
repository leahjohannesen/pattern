from helpers import Measurement, Point, Line
from measure import BodyMeasurement
from grid import Grid


class Moulage():
    def __init__(self):
        self.points = None
        self.lines = None
        self.origin = Point(Measurement(raw=0), Measurement(raw=0))

    def create(self, m):
        points = {}
        lines = {}
        guidelines = {}

        # guidelines/setup
        points['R'] = self.origin.dupe()
        points['P'] = self.origin + (0, Measurement('8 1/2'))
        points['b'] = points['P'] - (0, Measurement('4 1/2'))
        points['A'] = points['P'] + (0, m['le fr'])
        points['I'] = points['A'] - (0, m['le fr'] / 2)
        points['q'] = points['A'] - (0, Measurement('3'))

        # guidelines
        guidelines['center_front'] = Line(points['R'], points['A'])
        guidelines['low_hip'] = Line(points['R'], points['R'] + (m['lh fr'], 0))
        guidelines['high_hip'] = Line(points['b'], points['b'] + (m['lh fr'], 0))
        guidelines['waist'] = Line(points['P'], points['P'] + (m['lh fr'], 0))
        guidelines['bust'] = Line(points['I'], points['I'] + (m['bu fr'], 0))
        guidelines['front length'] = Line(points['A'], points['A'] + (Measurement('4'), 0))
        guidelines['cross front'] = Line(points['q'], points['q'] + (Measurement('8'), 0))

        # calcd
        points['B'] = points['A'] + (m['ne fr'], 0)
        lines['AB'] = Line(points['A'], points['B'])
        print(lines['AB'].length + (1 / 8))
        points['C'] = points['B'] + (0, lines['AB'].length)
        lines['BC'] = Line(points['B'], points['C'])

        self.guidelines = guidelines
        self.points = points
        self.lines = lines

        return

    # def create_guidelines(self, measurements):
    #     # drawn version has diff lengths, but for this doesn't matter
    #     low_hip_a = self.origin + (0, 0)
    #     low_hip_b = self.origin + (measurements['lh fr'], 0)
    #     self.guidelines['waist'] = 

if __name__ == '__main__':
    raw = {
        'neck': Measurement('19'),
        'shoulder': Measurement('4 3/4'),
        'front length': Measurement('17 3/4'),
        'back length': Measurement('17'),
        'figure length': Measurement('9 1/2'),
        'figure breadth': Measurement('9 1/2'),
        'cross front': Measurement('16 1/2'),
        'cross back': Measurement('19 1/2'),
        'bust': Measurement('52'),
        'underbust': Measurement('45 1/4'),
        'side': Measurement('9 1/2'),
        'armhole': Measurement('24'),
        'waist': Measurement('43 1/2'),
        'high hip': Measurement('47 1/2'),
        'low hip': Measurement('48 1/2'),
    }

    bm = BodyMeasurement(raw)
    bm.show()
    mu = Moulage()
    mu.create(bm)
    grid = Grid()
    grid.graph_thing(mu)