import unittest

from click.testing import CliRunner

from .make_dataset import main


class TestMain(unittest.TestCase):

    def test_main_runs(self):
        runner = CliRunner()
        result = runner.invoke(main, ['.', '.'])
        assert result.exit_code == 0

