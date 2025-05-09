import unittest
import mathematics

class TestMathematicsMethods(unittest.TestCase):
    # Passing in two numbers should return sum
    def test_add(self):
        self.assertEqual(mathematics.add(1,2), 3)

    # Passing in two numbers as strings should return sum
    def test_add_strings(self):
        self.assertEqual(mathematics.add("1","2"), 3)

if __name__ == '__main__':
    unittest.main()