import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
import io

from dicegame.cmdline import main


class TestAdd(unittest.TestCase):
    def test_1(self):
        input_values = ['1\n', '4\n']
        with patch(
            'builtins.input',
            side_effect=input_values,
        ):
            with io.StringIO() as captured_output:
                with redirect_stdout(captured_output):
                    main()

                self.assertEqual(captured_output.getvalue(), '5\n')
