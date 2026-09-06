# test_omenyarn.py
"""
Tests for OmenYarn module.
"""

import unittest
from omenyarn import OmenYarn

class TestOmenYarn(unittest.TestCase):
    """Test cases for OmenYarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OmenYarn()
        self.assertIsInstance(instance, OmenYarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OmenYarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
