from dataclasses import dataclass
from collections import OrderedDict

from src.models.BoardGame import BoardGame


class TestGetCollectionVariables:
    user_collection_response = (
        '<?xml version="1.0" encoding="utf-8" standalone="yes"?><items totalitems="2">\n\t\t<item '
        'objecttype="thing" objectid="275213" subtype="boardgame" collid="92810535">\n\t<name '
        'sortindex="1">7 Summits</name>\n\t\t<yearpublished>2021</yearpublished>         '
        "<image>https://cf.geekdo-images.com/F1wGooL0Vl_zrrSKmHmzYg__original/img"
        "/E_FId7SFLbBGZ5pwLK-jYDZwvn4=/0x0/filters:format("
        "jpeg)/pic4875153.jpg</image>\n\t\t<thumbnail>https://cf.geekdo-images.com"
        "/F1wGooL0Vl_zrrSKmHmzYg__thumb/img/DYU0FXwZedvcvRPRqEGB6G9RApw=/fit-in/200x150/filters"
        ':strip_icc()/pic4875153.jpg</thumbnail>\n\t\t\t<status own="1" prevowned="0" '
        'fortrade="0" want="0" '
        'wanttoplay="0" wanttobuy="0" wishlist="0"  preordered="0" lastmodified="2022-04-04 '
        '14:36:16" />\n\t  <numplays>0</numplays>                   </item>\n\t\t<item '
        'objecttype="thing" objectid="68448" subtype="boardgame" collid="87368605">\n\t<name '
        'sortindex="1">7 Wonders</name>\n\t\t<yearpublished>2010</yearpublished>         '
        "<image>https://cf.geekdo-images.com/RvFVTEpnbb4NM7k0IF8V7A__original/img"
        "/JQvRoz0xns9LZII74-ygKGDq_Es=/0x0/filters:format("
        "jpeg)/pic860217.jpg</image>\n\t\t<thumbnail>https://cf.geekdo-images.com"
        "/RvFVTEpnbb4NM7k0IF8V7A__thumb/img/ZlG_SRFChObHenw79fAve56_mnk=/fit-in/200x150/filters"
        ':strip_icc()/pic860217.jpg</thumbnail>\n\t\t\t<status own="1" prevowned="0" fortrade="0" '
        'want="0" wanttoplay="0" wanttobuy="0" wishlist="0"  preordered="0" '
        'lastmodified="2021-11-08 12:15:11" />\n\t<numplays>0</numplays>                  '
        "  </item>\n\n</items> "
    )
    expected_get_collection = [
        OrderedDict(
            [
                ("@objecttype", "thing"),
                ("@objectid", "275213"),
                ("@subtype", "boardgame"),
                ("@collid", "92810535"),
                (
                    "name",
                    OrderedDict([("@sortindex", "1"), ("#text", "7 Summits")]),
                ),
                ("yearpublished", "2021"),
                (
                    "image",
                    "https://cf.geekdo-images.com/F1wGooL0Vl_zrrSKmHmzYg__original/img/E_FId7SFLbBGZ5pwLK-jYDZwvn4=/0x0/filters:format(jpeg)/pic4875153.jpg",
                ),
                (
                    "thumbnail",
                    "https://cf.geekdo-images.com/F1wGooL0Vl_zrrSKmHmzYg__thumb/img/DYU0FXwZedvcvRPRqEGB6G9RApw=/fit-in/200x150/filters:strip_icc()/pic4875153.jpg",
                ),
                (
                    "status",
                    OrderedDict(
                        [
                            ("@own", "1"),
                            ("@prevowned", "0"),
                            ("@fortrade", "0"),
                            ("@want", "0"),
                            ("@wanttoplay", "0"),
                            ("@wanttobuy", "0"),
                            ("@wishlist", "0"),
                            ("@preordered", "0"),
                            ("@lastmodified", "2022-04-04 14:36:16"),
                        ]
                    ),
                ),
                ("numplays", "0"),
            ]
        ),
        OrderedDict(
            [
                ("@objecttype", "thing"),
                ("@objectid", "68448"),
                ("@subtype", "boardgame"),
                ("@collid", "87368605"),
                (
                    "name",
                    OrderedDict([("@sortindex", "1"), ("#text", "7 Wonders")]),
                ),
                ("yearpublished", "2010"),
                (
                    "image",
                    "https://cf.geekdo-images.com/RvFVTEpnbb4NM7k0IF8V7A__original/img/JQvRoz0xns9LZII74-ygKGDq_Es=/0x0/filters:format(jpeg)/pic860217.jpg",
                ),
                (
                    "thumbnail",
                    "https://cf.geekdo-images.com/RvFVTEpnbb4NM7k0IF8V7A__thumb/img/ZlG_SRFChObHenw79fAve56_mnk=/fit-in/200x150/filters:strip_icc()/pic860217.jpg",
                ),
                (
                    "status",
                    OrderedDict(
                        [
                            ("@own", "1"),
                            ("@prevowned", "0"),
                            ("@fortrade", "0"),
                            ("@want", "0"),
                            ("@wanttoplay", "0"),
                            ("@wanttobuy", "0"),
                            ("@wishlist", "0"),
                            ("@preordered", "0"),
                            ("@lastmodified", "2021-11-08 12:15:11"),
                        ]
                    ),
                ),
                ("numplays", "0"),
            ]
        ),
    ]
    invalid_user_response = (
        '<?xml version="1.0" encoding="utf-8" standalone="yes" '
        "?>\n<errors>\n\t<error>\n\t\t<message>Invalid username "
        "specified</message>\n\t</error>\n</errors> "
    )


class TestToBoardGameVariables:
    item_thumbnail_true = OrderedDict(
        [
            ("@type", "boardgame"),
            ("@id", "275213"),
            (
                "thumbnail",
                "https://cf.geekdo-images.com/F1wGooL0Vl_zrrSKmHmzYg__thumb/img/DYU0FXwZedvcvRPRqEGB6G9RApw=/fit-in/200x150/filters:strip_icc()/pic4875153.jpg",
            ),
            (
                "image",
                "https://cf.geekdo-images.com/F1wGooL0Vl_zrrSKmHmzYg__original/img/E_FId7SFLbBGZ5pwLK-jYDZwvn4=/0x0/filters:format(jpeg)/pic4875153.jpg",
            ),
            (
                "name",
                OrderedDict(
                    [
                        ("@type", "primary"),
                        ("@sortindex", "1"),
                        ("@value", "7 Summits"),
                    ]
                ),
            ),
            (
                "description",
                "In 7 Summits, you are a team of world class mountain climbers. Use the dice to your advantage to climb the tallest mountain on each of the seven continents, upgrade your equipment, and advance your skills. Will you be the first to climb them all?&#10;&#10;In this dice drafting game, you'll choose a die to climb its associated mountain; you can stop early to play it safe, or press on for the summit. But watch out &mdash; each time you press on, you run the risk of an avalanche!&#10;&#10;&mdash;description from the publisher&#10;&#10;",
            ),
            ("yearpublished", OrderedDict([("@value", "2021")])),
            ("minplayers", OrderedDict([("@value", "2")])),
            ("maxplayers", OrderedDict([("@value", "5")])),
            (
                "poll",
                [
                    OrderedDict(
                        [
                            ("@name", "suggested_numplayers"),
                            ("@title", "User Suggested Number of Players"),
                            ("@totalvotes", "2"),
                            (
                                "results",
                                [
                                    OrderedDict(
                                        [
                                            ("@numplayers", "1"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Recommended",
                                                            ),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "2"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "1"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Recommended",
                                                            ),
                                                            ("@numvotes", "1"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "3"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "2"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Recommended",
                                                            ),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "4"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Recommended",
                                                            ),
                                                            ("@numvotes", "2"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "5"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Recommended",
                                                            ),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "5+"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Recommended",
                                                            ),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "0"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@name", "suggested_playerage"),
                            ("@title", "User Suggested Player Age"),
                            ("@totalvotes", "2"),
                            (
                                "results",
                                OrderedDict(
                                    [
                                        (
                                            "result",
                                            [
                                                OrderedDict(
                                                    [
                                                        ("@value", "2"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "3"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "4"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "5"),
                                                        ("@numvotes", "1"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "6"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "8"),
                                                        ("@numvotes", "1"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "10"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "12"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "14"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "16"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "18"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "21 and up"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                            ],
                                        )
                                    ]
                                ),
                            ),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@name", "language_dependence"),
                            ("@title", "Language Dependence"),
                            ("@totalvotes", "0"),
                            (
                                "results",
                                OrderedDict(
                                    [
                                        (
                                            "result",
                                            [
                                                OrderedDict(
                                                    [
                                                        ("@level", "296"),
                                                        (
                                                            "@value",
                                                            "No necessary in-game text",
                                                        ),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@level", "297"),
                                                        (
                                                            "@value",
                                                            "Some necessary text - easily memorized or small crib sheet",
                                                        ),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@level", "298"),
                                                        (
                                                            "@value",
                                                            "Moderate in-game text - needs crib sheet or paste ups",
                                                        ),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@level", "299"),
                                                        (
                                                            "@value",
                                                            "Extensive use of text - massive conversion needed to be playable",
                                                        ),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@level", "300"),
                                                        (
                                                            "@value",
                                                            "Unplayable in another language",
                                                        ),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                            ],
                                        )
                                    ]
                                ),
                            ),
                        ]
                    ),
                ],
            ),
            ("playingtime", OrderedDict([("@value", "40")])),
            ("minplaytime", OrderedDict([("@value", "30")])),
            ("maxplaytime", OrderedDict([("@value", "40")])),
            ("minage", OrderedDict([("@value", "12")])),
            (
                "link",
                [
                    OrderedDict(
                        [
                            ("@type", "boardgamecategory"),
                            ("@id", "1017"),
                            ("@value", "Dice"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamecategory"),
                            ("@id", "1031"),
                            ("@value", "Racing"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2072"),
                            ("@value", "Dice Rolling"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2856"),
                            ("@value", "Die Icon Resolution"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2041"),
                            ("@value", "Open Drafting"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2661"),
                            ("@value", "Push Your Luck"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2939"),
                            ("@value", "Track Movement"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2828"),
                            ("@value", "Turn Order: Progressive"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamefamily"),
                            ("@id", "4705"),
                            (
                                "@value",
                                "Organizations: The Game Artisans of Canada",
                            ),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamefamily"),
                            ("@id", "6043"),
                            ("@value", "Sports: Mountain Climbing"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "331057"),
                            ("@value", "7 Summits: Launch Promos"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamedesigner"),
                            ("@id", "88370"),
                            ("@value", "Adrian Adamescu"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamedesigner"),
                            ("@id", "67502"),
                            ("@value", "Daryl Andrews"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameartist"),
                            ("@id", "81450"),
                            ("@value", "Megan Cheever"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameartist"),
                            ("@id", "28024"),
                            ("@value", "Kwanchai Moriya"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameartist"),
                            ("@id", "127486"),
                            ("@value", "Sean Seal"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "38131"),
                            ("@value", "Deep Water Games"),
                        ]
                    ),
                ],
            ),
        ]
    )
    boardgame_thumbnail_true = BoardGame(
        id=275213,
        name="7 Summits",
        type="boardgame",
        description="In 7 Summits, you are a team of world class mountain climbers. Use the dice to your advantage to climb the tallest mountain on each of the seven continents, upgrade your equipment, and advance your skills. Will you be the first to climb them all?&#10;&#10;In this dice drafting game, you'll choose a die to climb its associated mountain; you can stop early to play it safe, or press on for the summit. But watch out &mdash; each time you press on, you run the risk of an avalanche!&#10;&#10;&mdash;description from the publisher&#10;&#10;",
        minplayers=2,
        maxplayers=5,
        thumbnail="https://cf.geekdo-images.com/F1wGooL0Vl_zrrSKmHmzYg__thumb/img/DYU0FXwZedvcvRPRqEGB6G9RApw=/fit-in/200x150/filters:strip_icc()/pic4875153.jpg",
        image="https://cf.geekdo-images.com/F1wGooL0Vl_zrrSKmHmzYg__original/img/E_FId7SFLbBGZ5pwLK-jYDZwvn4=/0x0/filters:format(jpeg)/pic4875153.jpg",
    )
    item_thumbnail_false = OrderedDict(
        [
            ("@type", "boardgame"),
            ("@id", "68448"),
            (
                "name",
                [
                    OrderedDict(
                        [
                            ("@type", "primary"),
                            ("@sortindex", "1"),
                            ("@value", "7 Wonders"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "7 csoda"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "7 Cudów Świata"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "7 divů světa"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "7 Wonders"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "7 чудес"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "7 สิ่งมหัศจรรย์"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "7 원더스"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "Τα 7 θαύματα του κόσμου"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "七大奇蹟"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "七大奇迹"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "alternate"),
                            ("@sortindex", "1"),
                            ("@value", "世界の七不思議"),
                        ]
                    ),
                ],
            ),
            (
                "description",
                "You are the leader of one of the 7 great cities of the Ancient World. Gather resources, develop commercial routes, and affirm your military supremacy. Build your city and erect an architectural wonder which will transcend future times.&#10;&#10;7 Wonders lasts three ages. In each age, players receive seven cards from a particular deck, choose one of those cards, then pass the remainder to an adjacent player. Players reveal their cards simultaneously, paying resources if needed or collecting resources or interacting with other players in various ways. (Players have individual boards with special powers on which to organize their cards, and the boards are double-sided). Each player then chooses another card from the deck they were passed, and the process repeats until players have six cards in play from that age. After three ages, the game ends.&#10;&#10;In essence, 7 Wonders is a card development game. Some cards have immediate effects, while others provide bonuses or upgrades later in the game. Some cards provide discounts on future purchases. Some provide military strength to overpower your neighbors and others give nothing but victory points. Each card is played immediately after being drafted, so you'll know which cards your neighbor is receiving and how her choices might affect what you've already built up. Cards are passed left-right-left over the three ages, so you need to keep an eye on the neighbors in both directions.&#10;&#10;Though the box of earlier editions is listed as being for 3&ndash;7 players, there is an official 2-player variant included in the instructions.&#10;&#10;",
            ),
            ("yearpublished", OrderedDict([("@value", "2010")])),
            ("minplayers", OrderedDict([("@value", "2")])),
            ("maxplayers", OrderedDict([("@value", "7")])),
            (
                "poll",
                [
                    OrderedDict(
                        [
                            ("@name", "suggested_numplayers"),
                            ("@title", "User Suggested Number of Players"),
                            ("@totalvotes", "2201"),
                            (
                                "results",
                                [
                                    OrderedDict(
                                        [
                                            ("@numplayers", "1"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "4"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Recommended"),
                                                            ("@numvotes", "15"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "1329"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "2"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "117"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Recommended"),
                                                            ("@numvotes", "371"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "1130"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "3"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "475"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Recommended"),
                                                            ("@numvotes", "1154"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "199"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "4"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "1167"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Recommended"),
                                                            ("@numvotes", "739"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "41"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "5"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "1017"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Recommended"),
                                                            ("@numvotes", "816"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "57"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "6"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "458"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Recommended"),
                                                            ("@numvotes", "1123"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "164"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "7"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "383"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Recommended"),
                                                            ("@numvotes", "1047"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "290"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ("@numplayers", "7+"),
                                            (
                                                "result",
                                                [
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Best"),
                                                            ("@numvotes", "30"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            ("@value", "Recommended"),
                                                            ("@numvotes", "101"),
                                                        ]
                                                    ),
                                                    OrderedDict(
                                                        [
                                                            (
                                                                "@value",
                                                                "Not Recommended",
                                                            ),
                                                            ("@numvotes", "895"),
                                                        ]
                                                    ),
                                                ],
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@name", "suggested_playerage"),
                            ("@title", "User Suggested Player Age"),
                            ("@totalvotes", "504"),
                            (
                                "results",
                                OrderedDict(
                                    [
                                        (
                                            "result",
                                            [
                                                OrderedDict(
                                                    [
                                                        ("@value", "2"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "3"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "4"),
                                                        ("@numvotes", "1"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "5"),
                                                        ("@numvotes", "1"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "6"),
                                                        ("@numvotes", "19"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "8"),
                                                        ("@numvotes", "144"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "10"),
                                                        ("@numvotes", "197"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "12"),
                                                        ("@numvotes", "117"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "14"),
                                                        ("@numvotes", "21"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "16"),
                                                        ("@numvotes", "3"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "18"),
                                                        ("@numvotes", "1"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@value", "21 and up"),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                            ],
                                        )
                                    ]
                                ),
                            ),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@name", "language_dependence"),
                            ("@title", "Language Dependence"),
                            ("@totalvotes", "400"),
                            (
                                "results",
                                OrderedDict(
                                    [
                                        (
                                            "result",
                                            [
                                                OrderedDict(
                                                    [
                                                        ("@level", "336"),
                                                        (
                                                            "@value",
                                                            "No necessary in-game text",
                                                        ),
                                                        ("@numvotes", "306"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@level", "337"),
                                                        (
                                                            "@value",
                                                            "Some necessary text - easily memorized or small crib sheet",
                                                        ),
                                                        ("@numvotes", "89"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@level", "338"),
                                                        (
                                                            "@value",
                                                            "Moderate in-game text - needs crib sheet or paste ups",
                                                        ),
                                                        ("@numvotes", "4"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@level", "339"),
                                                        (
                                                            "@value",
                                                            "Extensive use of text - massive conversion needed to be playable",
                                                        ),
                                                        ("@numvotes", "1"),
                                                    ]
                                                ),
                                                OrderedDict(
                                                    [
                                                        ("@level", "340"),
                                                        (
                                                            "@value",
                                                            "Unplayable in another language",
                                                        ),
                                                        ("@numvotes", "0"),
                                                    ]
                                                ),
                                            ],
                                        )
                                    ]
                                ),
                            ),
                        ]
                    ),
                ],
            ),
            ("playingtime", OrderedDict([("@value", "30")])),
            ("minplaytime", OrderedDict([("@value", "30")])),
            ("maxplaytime", OrderedDict([("@value", "30")])),
            ("minage", OrderedDict([("@value", "10")])),
            (
                "link",
                [
                    OrderedDict(
                        [
                            ("@type", "boardgamecategory"),
                            ("@id", "1050"),
                            ("@value", "Ancient"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamecategory"),
                            ("@id", "1002"),
                            ("@value", "Card Game"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamecategory"),
                            ("@id", "1029"),
                            ("@value", "City Building"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamecategory"),
                            ("@id", "1015"),
                            ("@value", "Civilization"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamecategory"),
                            ("@id", "1021"),
                            ("@value", "Economic"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2984"),
                            ("@value", "Closed Drafting"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2040"),
                            ("@value", "Hand Management"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2004"),
                            ("@value", "Set Collection"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2020"),
                            ("@value", "Simultaneous Action Selection"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamemechanic"),
                            ("@id", "2015"),
                            ("@value", "Variable Player Powers"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamefamily"),
                            ("@id", "27524"),
                            ("@value", "Ancient: Babylon"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamefamily"),
                            ("@id", "72535"),
                            ("@value", "Ancient: Egypt"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamefamily"),
                            ("@id", "52373"),
                            ("@value", "Ancient: Greece"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamefamily"),
                            ("@id", "70360"),
                            ("@value", "Digital Implementations: Board Game Arena"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamefamily"),
                            ("@id", "17552"),
                            ("@value", "Game: 7 Wonders"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamefamily"),
                            ("@id", "71181"),
                            ("@value", "Mechanism: Artificial Player"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamefamily"),
                            ("@id", "27646"),
                            ("@value", "Mechanism: Tableau Building"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "247315"),
                            ("@value", "7 Wonders: Armada"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "154638"),
                            ("@value", "7 Wonders: Babel"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "110308"),
                            ("@value", "7 Wonders: Catan"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "111661"),
                            ("@value", "7 Wonders: Cities"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "92539"),
                            ("@value", "7 Wonders: Leaders"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "83445"),
                            ("@value", "7 Wonders: Manneken Pis"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "133993"),
                            ("@value", "7 Wonders: Wonder Pack"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "164649"),
                            ("@value", "Collection (fan expansion for 7 Wonders)"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "140098"),
                            ("@value", "Empires (fan expansion for 7 Wonders)"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "138187"),
                            ("@value", "Game Wonders (fan expansion for 7 Wonders)"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "134849"),
                            ("@value", "Lost Wonders (fan expansion for 7 Wonders)"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "329310"),
                            ("@value", "Modern Wonders (fan expansion for 7 Wonders)"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "131947"),
                            ("@value", "More Wonders... (fan expansion for 7 Wonders)"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "132146"),
                            ("@value", "Myths (fan expansion for 7 Wonders)"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "164648"),
                            ("@value", "Ruins (fan expansion for 7 Wonders)"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameexpansion"),
                            ("@id", "164647"),
                            ("@value", "Sailors (fan expansion for 7 Wonders)"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameimplementation"),
                            ("@id", "316377"),
                            ("@value", "7 Wonders (Second Edition)"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameimplementation"),
                            ("@id", "173346"),
                            ("@value", "7 Wonders Duel"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameimplementation"),
                            ("@id", "346703"),
                            ("@value", "7 Wonders: Architects"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamedesigner"),
                            ("@id", "9714"),
                            ("@value", "Antoine Bauza"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameartist"),
                            ("@id", "62528"),
                            ("@value", "Dimitri Chappuis"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameartist"),
                            ("@id", "12016"),
                            ("@value", "Miguel Coimbra"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameartist"),
                            ("@id", "100254"),
                            ("@value", "Etienne Hebinger"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgameartist"),
                            ("@id", "89045"),
                            ("@value", "Cyril Nouvel"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "4384"),
                            ("@value", "Repos Production"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "23043"),
                            ("@value", "ADC Blackfire Entertainment"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "157"),
                            ("@value", "Asmodee"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "15889"),
                            ("@value", "Asterion Press"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "15605"),
                            ("@value", "Galápagos Jogos"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "8820"),
                            ("@value", "Gém Klub Kft."),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "1391"),
                            ("@value", "Hobby Japan"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "6214"),
                            ("@value", "Kaissa Chess & Games"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "8291"),
                            ("@value", "Korea Boardgames Co., Ltd."),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "3218"),
                            ("@value", "Lautapelit.fi"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "9325"),
                            ("@value", "Lifestyle Boardgames Ltd"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "32395"),
                            ("@value", "NeoTroy Games"),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "7466"),
                            ("@value", "Rebel Sp. z o.o."),
                        ]
                    ),
                    OrderedDict(
                        [
                            ("@type", "boardgamepublisher"),
                            ("@id", "33998"),
                            ("@value", "Siam Board Games"),
                        ]
                    ),
                ],
            ),
        ]
    )
    boardgame_thumbnail_false = BoardGame(
        id=68448,
        name="7 Wonders",
        type="boardgame",
        description="You are the leader of one of the 7 great cities of the Ancient World. Gather resources, develop commercial routes, and affirm your military supremacy. Build your city and erect an architectural wonder which will transcend future times.&#10;&#10;7 Wonders lasts three ages. In each age, players receive seven cards from a particular deck, choose one of those cards, then pass the remainder to an adjacent player. Players reveal their cards simultaneously, paying resources if needed or collecting resources or interacting with other players in various ways. (Players have individual boards with special powers on which to organize their cards, and the boards are double-sided). Each player then chooses another card from the deck they were passed, and the process repeats until players have six cards in play from that age. After three ages, the game ends.&#10;&#10;In essence, 7 Wonders is a card development game. Some cards have immediate effects, while others provide bonuses or upgrades later in the game. Some cards provide discounts on future purchases. Some provide military strength to overpower your neighbors and others give nothing but victory points. Each card is played immediately after being drafted, so you'll know which cards your neighbor is receiving and how her choices might affect what you've already built up. Cards are passed left-right-left over the three ages, so you need to keep an eye on the neighbors in both directions.&#10;&#10;Though the box of earlier editions is listed as being for 3&ndash;7 players, there is an official 2-player variant included in the instructions.&#10;&#10;",
        minplayers=2,
        maxplayers=7,
        thumbnail=None,
        image=None,
    )
