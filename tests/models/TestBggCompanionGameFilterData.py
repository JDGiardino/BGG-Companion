from src.models.BoardGame import BoardGame
from src.models.GameFilter import GameFilter


class TestFilterGamesData:
    board_games = [
        BoardGame(
            id=1,
            name="Foo",
            type="boardgame",
            minplayers=1,
            maxplayers=4,
            yearpublished=1,
            averagerating=1,
            complexity=1,
            overallrank=1,
            cooperative=True,
        ),
        BoardGame(
            id=2,
            name="Bar",
            type="boardgame",
            minplayers=2,
            maxplayers=4,
            yearpublished=2,
            averagerating=2,
            complexity=2,
            overallrank=2,
            cooperative=True,
        ),
        BoardGame(
            id=3,
            name="Baz",
            type="boardgame",
            minplayers=1,
            maxplayers=5,
            yearpublished=3,
            averagerating=3,
            complexity=3,
            overallrank=3,
            cooperative=False,
        ),
        BoardGame(
            id=4,
            name="Qux",
            type="boardgame",
            minplayers=2,
            maxplayers=2,
            yearpublished=4,
            averagerating=4,
            complexity=4,
            overallrank=4,
            cooperative=False,
        ),
        BoardGame(
            id=5,
            name="Quux",
            type="boardgameexpansion",
            minplayers=2,
            maxplayers=2,
            yearpublished=5,
            averagerating=5,
            complexity=5,
            overallrank=5,
            cooperative=False,
        ),
    ]
    default_filter = GameFilter(minplayers=None, maxplayers=None, playerrangetype=None)
    expected_default_filter_list = [
        BoardGame(
            id=1,
            name="Foo",
            type="boardgame",
            minplayers=1,
            maxplayers=4,
            yearpublished=1,
            averagerating=1,
            complexity=1,
            overallrank=1,
            cooperative=True,
        ),
        BoardGame(
            id=2,
            name="Bar",
            type="boardgame",
            minplayers=2,
            maxplayers=4,
            yearpublished=2,
            averagerating=2,
            complexity=2,
            overallrank=2,
            cooperative=True,
        ),
        BoardGame(
            id=3,
            name="Baz",
            type="boardgame",
            minplayers=1,
            maxplayers=5,
            yearpublished=3,
            averagerating=3,
            complexity=3,
            overallrank=3,
            cooperative=False,
        ),
        BoardGame(
            id=4,
            name="Qux",
            type="boardgame",
            minplayers=2,
            maxplayers=2,
            yearpublished=4,
            averagerating=4,
            complexity=4,
            overallrank=4,
            cooperative=False,
        ),
    ]
    minplayers_in_range_filter_01 = GameFilter(
        minplayers=1, maxplayers=None, playerrangetype="normal"
    )
    expected_minplayers_in_range_filter_list_01 = [
        BoardGame(
            id=1,
            name="Foo",
            type="boardgame",
            minplayers=1,
            maxplayers=4,
            yearpublished=1,
            averagerating=1,
            complexity=1,
            overallrank=1,
            cooperative=True,
        ),
        BoardGame(
            id=3,
            name="Baz",
            type="boardgame",
            minplayers=1,
            maxplayers=5,
            yearpublished=3,
            averagerating=3,
            complexity=3,
            overallrank=3,
            cooperative=False,
        ),
    ]
    minplayers_in_range_filter_02 = GameFilter(
        minplayers=2, maxplayers=None, playerrangetype="normal"
    )
    expected_minplayers_in_range_filter_list_02 = [
        BoardGame(
            id=1,
            name="Foo",
            type="boardgame",
            minplayers=1,
            maxplayers=4,
            yearpublished=1,
            averagerating=1,
            complexity=1,
            overallrank=1,
            cooperative=True,
        ),
        BoardGame(
            id=2,
            name="Bar",
            type="boardgame",
            minplayers=2,
            maxplayers=4,
            yearpublished=2,
            averagerating=2,
            complexity=2,
            overallrank=2,
            cooperative=True,
        ),
        BoardGame(
            id=3,
            name="Baz",
            type="boardgame",
            minplayers=1,
            maxplayers=5,
            yearpublished=3,
            averagerating=3,
            complexity=3,
            overallrank=3,
            cooperative=False,
        ),
        BoardGame(
            id=4,
            name="Qux",
            type="boardgame",
            minplayers=2,
            maxplayers=2,
            yearpublished=4,
            averagerating=4,
            complexity=4,
            overallrank=4,
            cooperative=False,
        ),
    ]
    maxplayers_in_range_filter_01 = GameFilter(
        minplayers=None, maxplayers=5, playerrangetype="normal"
    )
    expected_maxplayers_in_range_filter_list_01 = [
        BoardGame(
            id=3,
            name="Baz",
            type="boardgame",
            minplayers=1,
            maxplayers=5,
            yearpublished=3,
            averagerating=3,
            complexity=3,
            overallrank=3,
            cooperative=False,
        ),
    ]
    maxplayers_in_range_filter_02 = GameFilter(
        minplayers=None, maxplayers=4, playerrangetype="normal"
    )
    expected_maxplayers_in_range_filter_list_02 = [
        BoardGame(
            id=1,
            name="Foo",
            type="boardgame",
            minplayers=1,
            maxplayers=4,
            yearpublished=1,
            averagerating=1,
            complexity=1,
            overallrank=1,
            cooperative=True,
        ),
        BoardGame(
            id=2,
            name="Bar",
            type="boardgame",
            minplayers=2,
            maxplayers=4,
            yearpublished=2,
            averagerating=2,
            complexity=2,
            overallrank=2,
            cooperative=True,
        ),
        BoardGame(
            id=3,
            name="Baz",
            type="boardgame",
            minplayers=1,
            maxplayers=5,
            yearpublished=3,
            averagerating=3,
            complexity=3,
            overallrank=3,
            cooperative=False,
        ),
    ]
    minplayers_exact_filter = GameFilter(minplayers=2, maxplayers=None, playerrangetype="exact")
    minplayers_exact_filter_list = [
        BoardGame(
            id=2,
            name="Bar",
            type="boardgame",
            minplayers=2,
            maxplayers=4,
            yearpublished=2,
            averagerating=2,
            complexity=2,
            overallrank=2,
            cooperative=True,
        ),
        BoardGame(
            id=4,
            name="Qux",
            type="boardgame",
            minplayers=2,
            maxplayers=2,
            yearpublished=4,
            averagerating=4,
            complexity=4,
            overallrank=4,
            cooperative=False,
        ),
    ]
    maxplayers_exact_filter = GameFilter(minplayers=None, maxplayers=4, playerrangetype="exact")
    maxplayers_exact_filter_list = [
        BoardGame(
            id=1,
            name="Foo",
            type="boardgame",
            minplayers=1,
            maxplayers=4,
            yearpublished=1,
            averagerating=1,
            complexity=1,
            overallrank=1,
            cooperative=True,
        ),
        BoardGame(
            id=2,
            name="Bar",
            type="boardgame",
            minplayers=2,
            maxplayers=4,
            yearpublished=2,
            averagerating=2,
            complexity=2,
            overallrank=2,
            cooperative=True,
        ),
    ]
