from helpers import Measurement

class BodyMeasurement():
    keys = [
        'neck', 'shoulder', 
        'front length', 'back length', 
        'figure length', 'figure breadth',
        'cross front', 'cross back',
        'bust', 'underbust',
        'side', 'armhole',
        'waist', 'high hip', 'low hip',
        ]

    cup_ref = {
        'AA': ('0 0/1', '0 1/2'),
        'A': ('0 1/2', '1 0/1'),
        'B': ('1 0/1', '2 1/2'),
        'C': ('2 1/2', '3 1/2'),
        'D': ('3 1/2', '4 1/2'),
        'E': ('4 1/2', '6 0/1'),
        'F': ('6 0/1', '7 0/1'),
        'G': ('7 0/1', '8 0/1'),
    }

    def __init__(self, raw=None):
        if raw is None:
            raw = self.prompt()
        self.raw = raw
        self.calc = self.make_calcs(raw)

    def prompt(self):
        output = {}
        print('Input measurements as fractions: whole_num numerator/denominator')
        print('Use 0 for whole number if fraction only')
        print('Example: 4 3/8" -> 4 3/8')
        for key in self.keys:
            raw_str = input(f'{key}: ')
            output[key] = Measurement(dimstr=raw_str)
            print(output)
        return output

    def make_calcs(self, raw):
        output = {}

        # intermediates
        neck = raw['neck'] / 6
        bust = raw['bust'] / 4
        waist = raw['waist'] / 4
        hip_high = raw['high hip'] / 4
        hip_low = raw['low hip'] / 4

        # final calcs
        output['ne fr'] = neck + (1 / 4)
        output['ne ba'] = neck + (3 / 8)
        output['sh'] = raw['shoulder']
        output['le fr'] = raw['front length']
        output['le ba'] = raw['back length']
        output['le fi'] = raw['figure length']
        output['br fi'] = raw['figure breadth'] / 2
        output['cr fr'] = raw['cross front'] / 2
        output['cr ba'] = raw['cross back'] / 2
        output['bu fr'] = bust + (1 / 4)
        output['bu ba'] = bust - (1 / 4)
        output['cu'] = self.cup_lookup(raw)
        output['wa fr'] = waist + (1 / 4)
        output['wa ba'] = waist - (1 / 4)
        output['hh fr'] = hip_high + (1 / 4)
        output['hh ba'] = hip_high - (1 / 4)
        output['lh fr'] = hip_low + (1 / 4)
        output['lh ba'] = hip_low - (1 / 4)
        output['si'] = raw['side']
        return output

    def cup_lookup(self, raw):
        diff = raw['bust'] - raw['underbust'] - 4
        for cup, (low, high) in self.cup_ref.items():
            mlow = Measurement(low)
            mhigh = Measurement(high)
            if mlow <= diff < mhigh:
                return cup 
        raise Exception('Cup lookup error | ' + diff)

    def show(self):
        max_len = max(len(k) for k in (set(self.raw) | set(self.calc)))
        for k, v in self.raw.items():
            print(f'{k.ljust(max_len)} | {v}')
        print(' --- ')
        for k, v in self.calc.items():
            print(f'{k.ljust(max_len)} | {v}')


    def __getitem__(self, key):
        try:
            return self.raw[key]
        except:
            pass
        
        try:
            return self.calc[key]
        except:
            pass
        
        raise KeyError('Could not find specified measurement')



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