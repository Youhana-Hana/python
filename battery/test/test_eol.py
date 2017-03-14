import sys;
import unittest

sys.path.append('./')

from battery import eol

class BatteryTest(unittest.TestCase):
    def test_processEmptyBuckets(self):
        actual = eol.calculate([])
        self.assertIsNone(actual)

    def test_processBucket(self):
        data = '[{"id": "battery1", "cycle": 20}, {"id": "battery 2", "cycle": 30}, {"id": "battery1", "cycle": 30}, {"id": "battery 2", "cycle": 40}]'

        actual = eol.calculate(data)
        self.assertDictEqual({'battery1': 25, 'battery 2': 35}, actual)

if __name__ == '__main__':
    unittest.main()
