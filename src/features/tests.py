import unittest

from .build_features import main


class TestMain(unittest.TestCase):

    def test_main_runs(self):
        self.assertTrue(main())
