#pylint: skip-file
"""tests firstscreen_text. Mostly just checks that the function returns a string"""
import unittest
from texts import firstscreen_text as texts

class TestText(unittest.TestCase):
    def test_phase0_11_returns_string(self):
        self.assertIsInstance(texts.phase0_11(),str)
    def test_phase0_12_returns_string(self):
        self.assertIsInstance(texts.phase0_12(),str)
    def test_phase0_13_returns_string(self):
        self.assertIsInstance(texts.phase0_13(),str)
    def test_phase2_1_returns_string(self):
        self.assertIsInstance(texts.phase2_1(),str)
    def test_phase1_11_returns_string(self):
        self.assertIsInstance(texts.phase1_11(),str)
    def test_phase1_12_returns_string(self):
        self.assertIsInstance(texts.phase1_12(),str)
    def test_phase1_13_returns_string(self):
        self.assertIsInstance(texts.phase1_13(),str)
    def test_phase2_1_returns_string(self):
        self.assertIsInstance(texts.phase2_1(),str)
    def test_phase3_1_returns_string(self):
        self.assertIsInstance(texts.phase3_1(),str)
    def test_phase3_2_returns_string(self):
        self.assertIsInstance(texts.phase3_2(),str)
    def test_phase3_3_returns_string(self):
        self.assertIsInstance(texts.phase3_3(),str)
    def test_phase3_4_returns_string(self):
        self.assertIsInstance(texts.phase3_4(),str)
    def test_phase3_5_returns_string(self):
        self.assertIsInstance(texts.phase3_5(),str)
    def test_phase3_6_returns_string(self):
        self.assertIsInstance(texts.phase3_6(),str)
    def test_phase3_7_returns_string(self):
        self.assertIsInstance(texts.phase3_7(),str)
    def test_phase4_1_returns_correct_string(self):
        self.assertEqual(texts.phase4_1("Matti"),"Hei Matti!")