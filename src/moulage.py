from helpers import Measurement, Point, Line
from measure import BodyMeasurement
from grid import Grid


class Moulage():
    # shoulder | side | armhole
    cup_dart_ref = {
        'A': ('0 3/8', '0 3/4', '0 3/8'),
        'B': ('0 1/2', '1 0/1', '0 1/2'),
        'C': ('0 5/8', '1 1/4', '0 5/8'),
        'D': ('0 3/4', '1 1/2', '0 3/4'),
    }

    waist_dart_ref = {
        ( '0',  '2'): '0 0/1',
        ( '2',  '5'): '0 3/8',
        ( '5',  '8'): '0 1/2',
        ( '8', '11'): '0 3/4',
        ('11', '14'): '1 0/1',
        ('14', '16'): '1 1/4',
    }

    def __init__(self):
        self.points = None
        self.lines = None
        self.origin = Point(Measurement(raw=0), Measurement(raw=0))

    def create(self, m):
        points = {}
        lines = {}

        # guidelines/setup
        points['R'] = self.origin.dupe()
        points['P'] = self.origin + (0, Measurement('8 1/2'))
        points['b'] = points['P'] - (0, Measurement('4 1/2'))
        points['A'] = points['P'] + (0, m['le fr'])
        points['I'] = points['A'] - (0, m['le fr'] / 2)
        points['q'] = points['A'] - (0, Measurement('3'))

        # guidelines
        lines['center_front'] = Line(points['R'], points['A'], kind='guide')
        lines['low_hip'] = Line(points['R'], points['R'] + (m['lh fr'], 0), kind='guide')
        lines['high_hip'] = Line(points['b'], points['b'] + (m['lh fr'], 0), kind='guide')
        lines['waist'] = Line(points['P'], points['P'] + (m['lh fr'], 0), kind='guide')
        lines['bust'] = Line(points['I'], points['I'] + (m['bu fr'], 0), kind='guide')
        lines['front length'] = Line(points['A'], points['A'] + (Measurement('4'), 0), kind='guide')
        lines['cross front'] = Line(points['q'], points['q'] + (Measurement('8'), 0), kind='guide')

        # calcd
        points['B'] = points['A'] + (m['ne fr'], 0)
        lines['AB'] = Line(points['A'], points['B'])

        points['C'] = points['B'] + (0, lines['AB'].length + (1 / 8))
        lines['BC'] = Line(points['B'], points['C'])

        points['D'] = points['B'] + (0, lines['BC'].length / 2)
        lines['BD'] = Line(points['B'], points['D'])

        points['E'] = points['D'] + (6, 0)
        lines['CE'] = Line(points['C'], points['E'], kind='temp')
        lines['DE'] = Line(points['D'], points['E'], kind='temp')

        shoulder_dart = Measurement(self.cup_dart_ref[m['cu']][0])
        points['G'] = lines['CE'].dist_along(m['sh'] / 2)
        points['H'] = lines['CE'].dist_along(m['sh'] / 2 + shoulder_dart)
        points['F'] = lines['CE'].dist_along(m['sh'] + shoulder_dart)
        lines['CF'] = Line(points['C'], points['F'])
        lines['CG'] = Line(points['C'], points['G'])
        lines['GH'] = Line(points['G'], points['H'])

        points['J'] = points['I'] + (m['bu fr'], 0)
        points['K'] = points['I'] + (m['br fi'], 0)
        lines['IJ'] = Line(points['I'], points['J'])
        lines['IK'] = Line(points['I'], points['K'])

        points['L'] = points['K'] + (0, 3)
        points['M'] = points['K'] - (0, 3)
        lines['LM'] = Line(points['L'], points['M'], kind='temp')

        


        
        self.points = points
        self.lines = lines

        return

    def show_lines(self):
        max_len = max(len(k) for k in (set(self.lines) | set(self.points)))
        for k, v in self.lines.items():
            print(f'{k.ljust(max_len)} | {v}')
    
    def show_points(self):
        max_len = max(len(k) for k in (set(self.lines) | set(self.points)))
        for k, v in self.points.items():
            print(f'{k.ljust(max_len)} | {v}') 

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
    grid = Grid(bm)
    mu = Moulage()
    mu.create(bm)
    mu.show_points()
    mu.show_lines()

    grid.graph_thing(mu)