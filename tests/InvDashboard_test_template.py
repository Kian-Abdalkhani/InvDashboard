import unittest

class BaseTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Code that runs once before all tests (e.g., connect to a database)
        pass
    
class Test(BaseTestClass):

    @classmethod
    def setUpClass(cls):
        # Code that runs once before all tests (e.g., connect to a database)
        pass

    def setUp(self):
        # Initialize objects or variables used in your tests here.
        # This method runs before each test case.
        #symbols to run tests on
        pass

    def tearDown(self):
        # Clean up any resources used in your tests here.
        # This method runs after each test case.
        pass

    def test_function_name(self):
        """
        This docstring describes what your test case is verifying.

        Args:
        self: The test case object.
        """
        # Arrange (Set up the test data and conditions)
        # Act (Call the function or method you're testing)
        # Assert (Verify the expected outcome using assertions)

        # # Example: Test if a function adds numbers correctly
        # expected_result = 10
        # actual_result = your_function(5, 5)
        # self.assertEqual(expected_result, actual_result)
        pass



if __name__ == '__main__':
  unittest.main()
