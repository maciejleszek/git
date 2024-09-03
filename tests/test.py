import unittest
from src.main import MyClass, captured_output

class TestMyClass(unittest.TestCase):
    def setUp(self):
        self.obj = MyClass("Maciek")

    def test_greet(self):
        expected_output = "Hello, Maciek!"
        with captured_output() as (out, err):
            self.obj.greet()
        output = out.getvalue().strip()
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()