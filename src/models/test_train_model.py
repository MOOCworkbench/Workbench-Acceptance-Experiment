import unittest

from .train_model import main


class TestTrainModel(unittest.TestCase):

    def test_main_runs(self):
        self.assertTrue(main())
