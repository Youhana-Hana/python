import sys
sys.path.append('./')
import unittest
from Added import Added

class AddedTest(unittest.TestCase):
    def test_add(self):
        added = Added()
        expected = added.add(1,2)
        self.assertEqual(3, expected)

if __name__ == '__main__':
  unittest.main()
