import unittest
import io, sys
from separator import *

# Run this unittest file without passing any command-line arguments
# other than ones you want to pass to unittest such as -values

class Test_seperator(unittest.TestCase):

    def setUp(self):
        # Add a spot to argv that we can use to pass command-line 
        # arguments to the main function in the separator module
        argv.append(None) 

    def test_01(self):
        argv[1] = 6 # Simulates passing 6 on the command line
        sys.stdout = student_output = io.StringIO()        
        sys.stdin = io.StringIO("1 2 1.2 2.3\n3\n4\n7.8 garbage, 12\n")
        expected_out = "Integers: 1 2 3 4 \nFloats: 1.2 2.3 7.8"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_02(self):
        argv[1] = 4 # Simulates passing 4 on the command line
        sys.stdout = student_output = io.StringIO()        
        sys.stdin = io.StringIO("1 2 3\n4 5 6\n")
        expected_out = "Integers: 1 2 3 4 \nFloats:"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())


if __name__ == "__main__":
        unittest.main()
