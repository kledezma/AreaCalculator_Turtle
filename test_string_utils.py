import unittest
from AssertExercises import reverse_string,capitalize_string,is_capitalized

class TestStringUtils(unittest.TestCase):
  
    def test_reverse(self):
         result = reverse_string('Nivek')
         self.assertTrue('keviN' in result)

    def test_capitalize(self):
        result = capitalize_string('nivek')
        self.assertEqual(result,'Nivek')

    def test_IsCapitalize(self):
        result = is_capitalized('kevin')
        self.assertTrue(result,True)

if __name__ == '__main__':
  unittest.main()