from unittest.mock import MagicMock
import pytest
from tic_tac_toe.player.ai_player import HardAI
from tic_tac_toe.player.human_player import HumanPlayer
from tic_tac_toe.player_factory import PlayerFactory
from tic_tac_toe.board import Board

@pytest.fixture
def notifier():
    return MagicMock()


def test_get_player_type_options_returns_labels():
    factory = PlayerFactory(notifier=MagicMock())

    options = factory.get_player_type_options()

    assert options == {
        "human": "Human",
        "ai_hard": "Hard AI",
    }

def test_create_player_human():
    factory = PlayerFactory(notifier=MagicMock())

    player = factory._create_player(Board.PLAYER_X, "human")

    assert isinstance(player, HumanPlayer)
    assert player.character == Board.PLAYER_X

def test_create_player_hard_ai():
    factory = PlayerFactory(notifier=MagicMock())

    player = factory._create_player(Board.PLAYER_O, "ai_hard")

    assert isinstance(player, HardAI)
    assert player.character == Board.PLAYER_O

def test_create_player_unknown_type_raises():
    factory = PlayerFactory(notifier=MagicMock())

    with pytest.raises(ValueError, match="Unknown player type"):
        factory._create_player(Board.PLAYER_X, "foobar")

def test_create_players_human_vs_hard_ai(notifier):
    notifier.select_player_type.side_effect = ["human", "ai_hard"]

    factory = PlayerFactory(notifier)
    players = factory.create_players()
    options = {"human": "Human", "ai_hard": "Hard AI"}

    notifier.select_player_type.assert_any_call(Board.PLAYER_X, options)
    notifier.select_player_type.assert_any_call(Board.PLAYER_O, options)

    assert isinstance(players[Board.PLAYER_X], HumanPlayer)
    assert isinstance(players[Board.PLAYER_O], HardAI)
    assert players[Board.PLAYER_X].character == Board.PLAYER_X
    assert players[Board.PLAYER_O].character == Board.PLAYER_O