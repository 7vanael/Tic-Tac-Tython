import pytest
from unittest.mock import patch
from tic_tac_toe.main import main
from tests.conftest import FakePlayer


@pytest.fixture
def mock_notifier():
    with patch('tic_tac_toe.main.CliNotifier') as MockNotifier:
        yield MockNotifier

@pytest.fixture
def mock_game_class():
    with patch('tic_tac_toe.main.Game') as MockGame:
        yield MockGame

@pytest.fixture
def mock_player_factory():
    with patch('tic_tac_toe.main.PlayerFactory') as MockPlayerFactory:
        yield MockPlayerFactory

@pytest.fixture
def mock_board():
    with patch('tic_tac_toe.main.Board') as MockBoard:
        yield MockBoard

class TestMain:
    def test_main_calls_render_welcome_and_game_play(self, mock_notifier, mock_game_class, mock_player_factory, mock_board):
        mock_notifier_instance = mock_notifier.return_value
        mock_game_instance = mock_game_class.return_value
        mock_factory_instance = mock_player_factory.return_value
        mock_board_instance = mock_board.return_value

        fake_player_x = FakePlayer("X",mock_notifier_instance, [1, 2, 3])
        fake_player_o = FakePlayer("O", mock_notifier_instance,[4, 5, 6])
        mock_factory_instance.create_players.return_value = {"X": fake_player_x, "O": fake_player_o}

        main()

        mock_notifier_instance.render_welcome.assert_called_once()
        mock_factory_instance.create_players.assert_called_once()
        mock_game_class.assert_called_once_with(
            mock_board_instance,
            mock_factory_instance.create_players.return_value,
            mock_notifier_instance,
        )
        mock_game_instance.play.assert_called_once()
