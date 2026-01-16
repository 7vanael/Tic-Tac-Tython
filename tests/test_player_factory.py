from unittest.mock import MagicMock, patch
import pytest
from player_ai import HardAI
from player_human import HumanPlayer
from player_easy_ai import EasyAi
from tests.conftest import EmptyFakePlayer
from player_factory import PlayerFactory
from board import Board


@pytest.fixture
def notifier():
    return MagicMock()

@pytest.fixture
def factory(notifier):
    return PlayerFactory(notifier=notifier)

def test_get_player_type_options_returns_labels(factory):
    options = factory.PLAYER_TYPES
    assert options == {
        "Human": HumanPlayer,
        "Easy AI": EasyAi,
        "Hard AI": HardAI,
    }

def test_create_player_human(factory):
    player = factory._create_player(Board.PLAYER_X, "Human")

    assert isinstance(player, HumanPlayer)
    assert player.character == Board.PLAYER_X

def test_create_player_hard_ai(factory):
    player = factory._create_player(Board.PLAYER_O, "Hard AI")

    assert isinstance(player, HardAI)
    assert player.character == Board.PLAYER_O

def test_create_player_unknown_type_raises(factory):
    with pytest.raises(ValueError, match="Unknown player type"):
        factory._create_player(Board.PLAYER_X, "foobar")

def test_create_players_human_vs_hard_ai(factory, notifier):
    notifier.select_player_type.side_effect = ["Human", "Fake Player"]
    options = {"Human": HumanPlayer, "Hard AI": HardAI, "Fake Player": EmptyFakePlayer}
    with patch('player_factory.PlayerFactory.PLAYER_TYPES', options):
        players = factory.create_players()

        notifier.select_player_type.assert_any_call(Board.PLAYER_X, options)
        notifier.select_player_type.assert_any_call(Board.PLAYER_O, options)

        assert isinstance(players[Board.PLAYER_X], HumanPlayer)
        assert isinstance(players[Board.PLAYER_O], EmptyFakePlayer)
        assert players[Board.PLAYER_X].character == Board.PLAYER_X
        assert players[Board.PLAYER_O].character == Board.PLAYER_O