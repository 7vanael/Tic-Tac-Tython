import unittest
from unittest.mock import patch, call, Mock

from main import main


class TestMain(unittest.TestCase):
    @patch('main.Board')
    @patch('main.render_board')
    @patch('main.render_welcome')
    def test_main_calls_functions_in_order(self, mock_welcome, mock_render_board, mock_board_class):
        mock_board_instance = mock_board_class.return_value

        main()

        mock_welcome.assert_called_once()
        mock_board_class.assert_called_once()
        mock_render_board.assert_called_once_with(mock_board_instance)

    def test_main_call_order(self):
        with patch('main.render_welcome') as mock_welcome, \
                patch('main.Board') as mock_board_class, \
                patch('main.render_board') as mock_render_board:
            mock_board_instance = mock_board_class.return_value
            manager = Mock()
            manager.attach_mock(mock_welcome, 'render_welcome')
            manager.attach_mock(mock_board_class, 'Board')
            manager.attach_mock(mock_render_board, 'render_board')

            main()
            expected_calls = [
                call.render_welcome(),
                call.Board(),
                call.render_board(mock_board_instance)
            ]
            assert manager.mock_calls == expected_calls
