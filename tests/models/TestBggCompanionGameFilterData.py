from src.models.BoardGame import BoardGame
from src.models.GameFilter import GameFilter


class TestGameMatchesFilterData:
    board_games = [
        BoardGame(
            id=187645,
            name="Star Wars: Rebellion",
            type="boardgame",
            description="StarWars:Rebellion is a board game of epic conflict.",
            minplayers=2,
            maxplayers=4,
            yearpublished=2016,
            averagerating=8.41956,
            complexity=3.733,
            overallrank=8,
            thumbnail="https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__thumb/img"
            "/gAxzddRVQiRdjZHYFUZ2xc5Jlbw=/fit-in/200x150/filters:strip_icc()/pic4325841.jpg",
            image="https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__original/img/GKueTbkCk2Ramf6ai8mDj-BP6cI=/0x0/"
            "filters:format(jpeg)/pic4325841.jpg",
        ),
        BoardGame(
            id=148228,
            name="Splendor",
            type="boardgame",
            description="Splendor is a game of chip-collecting and card development.",
            minplayers=2,
            maxplayers=4,
            yearpublished=2014,
            averagerating=7.43335,
            complexity=1.7896,
            overallrank=193.0,
            thumbnail="https://cf.geekdo-images.com/rwOMxx4q5yuElIvo-1-OFw__thumb/img/D4hkkHfOgu22PwgJomjplWAveuo"
            "=/fit-in/200x150/filters:strip_icc()/pic1904079.jpg",
            image="https://cf.geekdo-images.com/rwOMxx4q5yuElIvo-1-OFw__original/img/Y2tUGY2nPTGd_epJYKQXPkQD8AM=/0x0"
            "/filters:format(jpeg)/pic1904079.jpg",
        ),
        BoardGame(
            id=266192,
            name="Wingspan",
            type="boardgame",
            description="Wingspan is a competitive, medium-weight, card-driven, engine-building board game.",
            minplayers=1,
            maxplayers=5,
            yearpublished=2019,
            averagerating=8.08769,
            complexity=2.4474,
            overallrank=24.0,
            thumbnail="https://cf.geekdo-images.com/yLZJCVLlIx4c7eJEWUNJ7w__thumb/img/VNToqgS2-pOGU6MuvIkMPKn_y-s"
            "=/fit-in/200x150/filters:strip_icc()/pic4458123.jpg",
            image="https://cf.geekdo-images.com/yLZJCVLlIx4c7eJEWUNJ7w__original/img/cI782Zis9cT66j2MjSHKJGnFPNw=/0x0"
            "/filters:format(jpeg)/pic4458123.jpg",
        ),
        BoardGame(
            id=2655,
            name="Hive",
            type="boardgame",
            description="Hive is a highly addictive strategic game for two players.",
            minplayers=2,
            maxplayers=2,
            yearpublished=2000,
            averagerating=7.32193,
            complexity=2.3243,
            overallrank=267.0,
            thumbnail="https://cf.geekdo-images.com/fQe85tsBZoH6ibPnm1k1UA__thumb/img/8ULXa8v7095ohgXMMmNlCGrC7zU"
            "=/fit-in/200x150/filters:strip_icc()/pic791151.jpg",
            image="https://cf.geekdo-images.com/fQe85tsBZoH6ibPnm1k1UA__original/img/eqUVrCJKcMBGBhw4Gfc9_9JabYE=/0x0"
            "/filters:format(jpeg)/pic791151.jpg",
        ),
        BoardGame(
            id=6902,
            name="Tetris",
            type="boardgame",
            description="The ultimate test of advanced territorial strategy.",
            minplayers=2,
            maxplayers=2,
            yearpublished=1989,
            averagerating=5.63488,
            complexity=1.625,
            overallrank=17645,
            thumbnail=None,
            image=None,
        ),
        BoardGame(
            id=196421,
            name="Aeon's End: The Depths",
            type="boardgameexpansion",
            description="Deep within the earth, lost in the labyrinth of shadows, the Horde-Crone has awakened.",
            minplayers=1,
            maxplayers=4,
            yearpublished=2016,
            averagerating=8.33706,
            complexity=2.7333,
            overallrank="Not Ranked",
            thumbnail=None,
            image=None,
        ),
        BoardGame(
            id=12345,
            name="FooBar",
            type="boardgameexpansion",
            description="Baz",
            minplayers=2,
            maxplayers=2,
            yearpublished=1234,
            averagerating=1234.0,
            complexity=1234.0,
            overallrank=1234.0,
            thumbnail=None,
            image=None,
        ),
    ]
    default_filter = GameFilter(
        minimum_maxplayers=None,
        exactplayers=None,
    )
    expected_default_filter = [
        BoardGame(
            id=187645,
            name="Star Wars: Rebellion",
            type="boardgame",
            description="StarWars:Rebellion is a board game of epic conflict.",
            minplayers=2,
            maxplayers=4,
            yearpublished=2016,
            averagerating=8.41956,
            complexity=3.733,
            overallrank=8,
            thumbnail="https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__thumb/img"
            "/gAxzddRVQiRdjZHYFUZ2xc5Jlbw=/fit-in/200x150/filters:strip_icc()/pic4325841.jpg",
            image="https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__original/img/GKueTbkCk2Ramf6ai8mDj-BP6cI=/0x0/"
            "filters:format(jpeg)/pic4325841.jpg",
        ),
        BoardGame(
            id=148228,
            name="Splendor",
            type="boardgame",
            description="Splendor is a game of chip-collecting and card development.",
            minplayers=2,
            maxplayers=4,
            yearpublished=2014,
            averagerating=7.43335,
            complexity=1.7896,
            overallrank=193.0,
            thumbnail="https://cf.geekdo-images.com/rwOMxx4q5yuElIvo-1-OFw__thumb/img/D4hkkHfOgu22PwgJomjplWAveuo"
            "=/fit-in/200x150/filters:strip_icc()/pic1904079.jpg",
            image="https://cf.geekdo-images.com/rwOMxx4q5yuElIvo-1-OFw__original/img/Y2tUGY2nPTGd_epJYKQXPkQD8AM=/0x0"
            "/filters:format(jpeg)/pic1904079.jpg",
        ),
        BoardGame(
            id=266192,
            name="Wingspan",
            type="boardgame",
            description="Wingspan is a competitive, medium-weight, card-driven, engine-building board game.",
            minplayers=1,
            maxplayers=5,
            yearpublished=2019,
            averagerating=8.08769,
            complexity=2.4474,
            overallrank=24.0,
            thumbnail="https://cf.geekdo-images.com/yLZJCVLlIx4c7eJEWUNJ7w__thumb/img/VNToqgS2-pOGU6MuvIkMPKn_y-s"
            "=/fit-in/200x150/filters:strip_icc()/pic4458123.jpg",
            image="https://cf.geekdo-images.com/yLZJCVLlIx4c7eJEWUNJ7w__original/img/cI782Zis9cT66j2MjSHKJGnFPNw=/0x0"
            "/filters:format(jpeg)/pic4458123.jpg",
        ),
        BoardGame(
            id=2655,
            name="Hive",
            type="boardgame",
            description="Hive is a highly addictive strategic game for two players.",
            minplayers=2,
            maxplayers=2,
            yearpublished=2000,
            averagerating=7.32193,
            complexity=2.3243,
            overallrank=267.0,
            thumbnail="https://cf.geekdo-images.com/fQe85tsBZoH6ibPnm1k1UA__thumb/img/8ULXa8v7095ohgXMMmNlCGrC7zU"
            "=/fit-in/200x150/filters:strip_icc()/pic791151.jpg",
            image="https://cf.geekdo-images.com/fQe85tsBZoH6ibPnm1k1UA__original/img/eqUVrCJKcMBGBhw4Gfc9_9JabYE=/0x0"
            "/filters:format(jpeg)/pic791151.jpg",
        ),
        BoardGame(
            id=6902,
            name="Tetris",
            type="boardgame",
            description="The ultimate test of advanced territorial strategy.",
            minplayers=2,
            maxplayers=2,
            yearpublished=1989,
            averagerating=5.63488,
            complexity=1.625,
            overallrank=17645,
            thumbnail=None,
            image=None,
        ),
    ]
    minimum_maxplayers_filter = GameFilter(
        minimum_maxplayers=4,
        exactplayers=None,
    )
    expected_minimum_maxplayers_filter = [
        BoardGame(
            id=187645,
            name="Star Wars: Rebellion",
            type="boardgame",
            description="StarWars:Rebellion is a board game of epic conflict.",
            minplayers=2,
            maxplayers=4,
            yearpublished=2016,
            averagerating=8.41956,
            complexity=3.733,
            overallrank=8,
            thumbnail="https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__thumb/img"
            "/gAxzddRVQiRdjZHYFUZ2xc5Jlbw=/fit-in/200x150/filters:strip_icc()/pic4325841.jpg",
            image="https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__original/img/GKueTbkCk2Ramf6ai8mDj-BP6cI=/0x0/"
            "filters:format(jpeg)/pic4325841.jpg",
        ),
        BoardGame(
            id=148228,
            name="Splendor",
            type="boardgame",
            description="Splendor is a game of chip-collecting and card development.",
            minplayers=2,
            maxplayers=4,
            yearpublished=2014,
            averagerating=7.43335,
            complexity=1.7896,
            overallrank=193.0,
            thumbnail="https://cf.geekdo-images.com/rwOMxx4q5yuElIvo-1-OFw__thumb/img/D4hkkHfOgu22PwgJomjplWAveuo"
            "=/fit-in/200x150/filters:strip_icc()/pic1904079.jpg",
            image="https://cf.geekdo-images.com/rwOMxx4q5yuElIvo-1-OFw__original/img/Y2tUGY2nPTGd_epJYKQXPkQD8AM=/0x0"
            "/filters:format(jpeg)/pic1904079.jpg",
        ),
        BoardGame(
            id=266192,
            name="Wingspan",
            type="boardgame",
            description="Wingspan is a competitive, medium-weight, card-driven, engine-building board game.",
            minplayers=1,
            maxplayers=5,
            yearpublished=2019,
            averagerating=8.08769,
            complexity=2.4474,
            overallrank=24.0,
            thumbnail="https://cf.geekdo-images.com/yLZJCVLlIx4c7eJEWUNJ7w__thumb/img/VNToqgS2-pOGU6MuvIkMPKn_y-s"
            "=/fit-in/200x150/filters:strip_icc()/pic4458123.jpg",
            image="https://cf.geekdo-images.com/yLZJCVLlIx4c7eJEWUNJ7w__original/img/cI782Zis9cT66j2MjSHKJGnFPNw=/0x0"
            "/filters:format(jpeg)/pic4458123.jpg",
        ),
    ]
    exact_players_filter = GameFilter(
        minimum_maxplayers=None,
        exactplayers=2,
    )
    expected_exact_players_filter = [
        BoardGame(
            id=2655,
            name="Hive",
            type="boardgame",
            description="Hive is a highly addictive strategic game for two players.",
            minplayers=2,
            maxplayers=2,
            yearpublished=2000,
            averagerating=7.32193,
            complexity=2.3243,
            overallrank=267.0,
            thumbnail="https://cf.geekdo-images.com/fQe85tsBZoH6ibPnm1k1UA__thumb/img/8ULXa8v7095ohgXMMmNlCGrC7zU"
            "=/fit-in/200x150/filters:strip_icc()/pic791151.jpg",
            image="https://cf.geekdo-images.com/fQe85tsBZoH6ibPnm1k1UA__original/img/eqUVrCJKcMBGBhw4Gfc9_9JabYE=/0x0"
            "/filters:format(jpeg)/pic791151.jpg",
        ),
        BoardGame(
            id=6902,
            name="Tetris",
            type="boardgame",
            description="The ultimate test of advanced territorial strategy.",
            minplayers=2,
            maxplayers=2,
            yearpublished=1989,
            averagerating=5.63488,
            complexity=1.625,
            overallrank=17645,
            thumbnail=None,
            image=None,
        ),
    ]
