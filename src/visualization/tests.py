import unittest

from click.testing import CliRunner

from .visualize import main


class TestVisualization(unittest.TestCase):

    def test_main_runs(self):
        self.assertTrue(main())
