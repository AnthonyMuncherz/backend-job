import unittest
import json
from main import get_data, main
import io
import sys

class TestGeneral(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)
    
    def test_json_parsing_success(self):
        """Test that JSON parsing now works correctly"""
        # This should not raise an error anymore
        data = json.loads(get_data())
        self.assertIsInstance(data, dict)
        self.assertEqual(data['tiam'], 'bibendum')
        self.assertEqual(data['lacus'], 23.5)
        self.assertEqual(data['sellus'], False)
    
    def test_main_function_success(self):
        """Test that main function runs without error"""
        # Capture stdout to verify the function runs without error
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            main()  # Should not raise an error
            output = captured_output.getvalue()
            self.assertIn('tiam', output)
            self.assertIn('bibendum', output)
        finally:
            sys.stdout = sys.__stdout__
