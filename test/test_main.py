"""Test file for testing the main.py file"""

import unittest # for creating the test case
from unittest.mock import patch # for mocking the input
import io # for capturing the output
import sys # for restoring the stdout and removing the main module from the cache
import importlib # for importing the main.py file
from pathlib import Path # for getting the path of the main.py file

class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Sets up the test environment by removing the main module from the cache"""
        super().setUp()
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="2")
    def test_prime_2(self, _mock_input):
        """Testa se o programa responde primo quando a entrada é 2"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Primo", captured_output.getvalue().strip())
        self.assertNotIn("Não primo", captured_output.getvalue().strip())
        self.assertNotIn("Número inválido", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="5")
    def test_prime_5(self, _mock_input):
        """Testa se o programa responde primo quando a entrada é 5"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Primo", captured_output.getvalue().strip())
        self.assertNotIn("Não primo", captured_output.getvalue().strip())
        self.assertNotIn("Número inválido", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="71")
    def test_prime_71(self, _mock_input):
        """Testa se o programa responde primo quando a entrada é 71"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Primo", captured_output.getvalue().strip())
        self.assertNotIn("Não primo", captured_output.getvalue().strip())
        self.assertNotIn("Número inválido", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="1")
    def test_not_prime_1(self, _mock_input):
        """Testa se o programa responde não primo quando a entrada é 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Não primo", captured_output.getvalue().strip())
        self.assertNotIn("Primo", captured_output.getvalue().strip())
        self.assertNotIn("Número inválido", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="4")
    def test_not_prime_4(self, _mock_input):
        """Testa se o programa responde não primo quando a entrada é 4"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Não primo", captured_output.getvalue().strip())
        self.assertNotIn("Primo", captured_output.getvalue().strip())
        self.assertNotIn("Número inválido", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="289")
    def test_not_prime_289(self, _mock_input):
        """Testa se o programa responde não primo quando a entrada é 289"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Não primo", captured_output.getvalue().strip())
        self.assertNotIn("Primo", captured_output.getvalue().strip())
        self.assertNotIn("Número inválido", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="-3")
    def test_invalid(self, _mock_input):
        """Testa se o programa responde número inválido quando a entrada é -3"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Número inválido", captured_output.getvalue().strip())
        self.assertNotIn("Primo", captured_output.getvalue().strip())
        self.assertNotIn("Não primo", captured_output.getvalue().strip())


if __name__ == "__main__":
    # add the parent directory to the path in order to run it from the run command in vscode
    main_file_folder = Path(__file__).parents[1].as_posix() # pylint: disable=invalid-name
    sys.path.insert(0, main_file_folder)
    unittest.main()
