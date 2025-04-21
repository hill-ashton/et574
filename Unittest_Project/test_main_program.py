import unittest
from unittest.mock import patch
import main_program

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '85', '90', '95'])
    @patch('builtins.print')
    def test_main_valid_input(self, mock_print, mock_input):
        main_program.main()
        #adjusted last print call to work with updated main_program
        mock_print.assert_called_with('Number of students failed: 0')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )
        #additional asserts for updated main_program
        self.assertIn(
            unittest.mock.call('Highest grade: 95.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Lowest grade: 85.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students passed: 3'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students failed: 0'), 
            mock_print.mock_calls
        )
        

    @patch('builtins.input', side_effect=['0','3', '85', '90', '95'])
    @patch('builtins.print')
    def test_invalid_number_of_students(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('Number of students failed: 0')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Highest grade: 95.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Lowest grade: 85.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students passed: 3'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students failed: 0'), 
            mock_print.mock_calls
        )

    @patch('builtins.input', side_effect=['3', '105', '85', '-5', '90', '95'])
    @patch('builtins.print')
    def test_invalid_grades(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('Number of students failed: 0')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Highest grade: 95.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Lowest grade: 85.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students passed: 3'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students failed: 0'), 
            mock_print.mock_calls
        )

    #test case assignment 1: non numeric input for number of students
    @patch('builtins.input', side_effect=['abc','3', '85', '90', '95'])
    @patch('builtins.print')
    def test_non_numeric_input_for_student_count(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('Number of students failed: 0')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Highest grade: 95.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Lowest grade: 85.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students passed: 3'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students failed: 0'), 
            mock_print.mock_calls
        )

    #test case assignment 2: handling a single student
    #the mock input, as well as some asserts in this case were adjusted to be able to handle a single student
    @patch('builtins.input', side_effect=['1','85'])
    @patch('builtins.print')
    def test_single_student(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('Number of students failed: 0')
        self.assertIn(
            unittest.mock.call('The class average is: 85.00'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Highest grade: 85.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Lowest grade: 85.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students passed: 1'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students failed: 0'), 
            mock_print.mock_calls
        )

    #test case assignment 3: non numeric grade input
    #this is my original testing case, which should test the handling of ValueError during the grade entry
    @patch('builtins.input', side_effect=['3','A+','eightyfive','85', '90', '95'])
    @patch('builtins.print')
    def test_non_numeric_grade_input(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('Number of students failed: 0')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Highest grade: 95.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Lowest grade: 85.0'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students passed: 3'), 
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Number of students failed: 0'), 
            mock_print.mock_calls
        )


if __name__ == "__main__":
    unittest.main()
