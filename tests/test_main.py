import pytest
from unittest.mock import patch, call, Mock

from tic_tac_toe.main import main


@pytest.fixture
def mock_notifier():
    with patch('tic_tac_toe.main.CliNotifier') as MockNotifier:
        yield MockNotifier

@pytest.fixture
def mock_game_class():
    with patch('tic_tac_toe.main.Game') as MockGame:
        yield MockGame

class TestMain:
    def test_main_calls_render_welcome_and_game_play(self, mock_notifier, mock_game_class):
        mock_notifier_instance = mock_notifier.return_value
        mock_game_instance = mock_game_class.return_value

        main()

        mock_notifier_instance.render_welcome.assert_called_once()
        mock_game_instance.play.assert_called_once()
