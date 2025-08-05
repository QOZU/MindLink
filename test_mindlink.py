# test_mindlink.py
"""
Tests for MindLink module.
"""

import unittest
from mindlink import MindLink

class TestMindLink(unittest.TestCase):
    """Test cases for MindLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MindLink()
        self.assertIsInstance(instance, MindLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MindLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
