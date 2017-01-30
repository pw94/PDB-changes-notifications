import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from rnapdbeefetcher import get_RNA_secondary_structure_via_browser

def get_fixture(id):
    fixture_dir = os.path.join(current_dir, "fixtures")
    filename = [os.path.join(fixture_dir, file) for file in os.listdir(fixture_dir) if file.startswith(id)][0]
    with open(filename, "r") as content:
        return content.read()

class Test_rnapdbeefetcher(unittest.TestCase):
    def test_1VS9(self):
        id = "1VS9"
        fixture = get_fixture(id)
        
        result = get_RNA_secondary_structure_via_browser(id)

        self.assertEqual(fixture, result)

    def test_2WH4(self):
        id = "2WH4"
        fixture = get_fixture(id)
        
        result = get_RNA_secondary_structure_via_browser(id)

        self.assertEqual(fixture, result)

    def test_5TNA(self):
        id = "5TNA"
        fixture = get_fixture(id)
        
        result = get_RNA_secondary_structure_via_browser(id)

        self.assertEqual(fixture, result)

if __name__ == '__main__':
    unittest.main()
