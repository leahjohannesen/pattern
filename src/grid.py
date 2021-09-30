from helpers import Measurement, Point, Line
from measure import BodyMeasurement


class Moulage():
    def __init__(self):
        self.points = None
        self.guidelines = {}
        self.lines = {}
        self.origin = Point(Measurement(raw=0), Measurement(raw=0))

    def create_points(self, m):
        output = {}

        # CF reference points
        output['R'] = self.origin.dupe()
        output['P'] = self.origin + (0, Measurement('8 1/2'))
        output['b'] = output['P'] - (0, Measurement('4 1/2'))
        output['A'] = output['P'] + (0, m['le fr'])
        output['I'] = output['A'] - (0, m['le fr'] / 2)
        output['q'] = output['A'] - (0, Measurement('3'))

        # calcd
        output['B'] = output['A'] + (m['ne fr'], 0)

        self.points = output


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
    mu.create_points(bm)
    print(mu.points)