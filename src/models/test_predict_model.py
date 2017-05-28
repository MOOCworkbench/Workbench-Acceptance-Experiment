import unittest

from .predict_model import main


class TestPredictModel(unittest.TestCase):

    def test_main_runs(self):
        self.assertTrue(main())
