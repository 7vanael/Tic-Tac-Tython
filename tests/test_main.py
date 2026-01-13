import unittest
from unittest.mock import patch, call, Mock

from tic_tac_toe.main import main


class TestMain(unittest.TestCase):
    @patch('tic_tac_toe.main.Game')
    @patch('tic_tac_toe.main.render_welcome')
    def test_main_calls_functions_in_order(self, mock_welcome, mock_game_class):
        mock_game_instance = mock_game_class.return_value

        main()

        mock_welcome.assert_called_once()
        mock_game_class.assert_called_once()
        mock_game_instance.play.assert_called_once()


    @patch('tic_tac_toe.main.Game')
    @patch('tic_tac_toe.main.render_welcome')
    def test_main_call_order(self, mock_welcome, mock_game_class):
            mock_game_instance = mock_game_class.return_value
            manager = Mock()
            manager.attach_mock(mock_welcome, 'render_welcome')
            manager.attach_mock(mock_game_class, 'Game')
            manager.attach_mock(mock_game_instance.play, 'play')

            main()
            expected_calls = [
                call.render_welcome(),
                call.Game(),
                call.play()
            ]
            assert manager.mock_calls == expected_calls
