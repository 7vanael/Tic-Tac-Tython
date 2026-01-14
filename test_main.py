import pytest
from unittest.mock import patch, call, Mock
from main import main


@pytest.fixture
def mock_welcome():
    with patch('main.render_welcome') as mock:
        yield mock

@pytest.fixture
def mock_game_class():
    with patch('main.Game') as mock:
        yield mock

class TestMain:
    def test_main_calls_functions_in_order(self, mock_welcome, mock_game_class):
        mock_game_instance = mock_game_class.return_value

        main()

        mock_welcome.assert_called_once()
        mock_game_class.assert_called_once()
        mock_game_instance.play.assert_called_once()


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
