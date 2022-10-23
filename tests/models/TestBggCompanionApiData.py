from dataclasses import dataclass
from collections import OrderedDict

from src.models.BoardGame import BoardGame


class TestGetCollectionData:
    user_collection_response = (
        '<?xml version="1.0" encoding="utf-8" standalone="yes"?><items totalitems="2"><item '
        'objecttype="thing" objectid="275213" subtype="boardgame" collid="92810535"><name '
        'sortindex="1">7 Summits</name><yearpublished>2021</yearpublished></item><item '
        'objecttype="thing" objectid="68448" subtype="boardgame" collid="87368605"><name '
        'sortindex="1">7 Wonders</name><yearpublished>2010</yearpublished></item></items> '
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
            ]
        ),
    ]
    invalid_user_response = (
        '<?xml version="1.0" encoding="utf-8" standalone="yes" '
        "?><errors><error><message>Invalid username "
        "specified</message></error></errors> "
    )
    user_no_collection_response = (
        '<?xml version="1.0" encoding="utf-8" standalone="yes"?><items totalitems="0" '
        'termsofuse="https://boardgamegeek.com/xmlapi/termsofuse" pubdate="Fri, 03 Jun 2022 03:52:05 +0000"> </items> '
    )


class TestGetBoardGamesData:
    two_ids_response = (
        '<?xml version="1.0" encoding="utf-8"?><items termsofuse="https://boardgamegeek.com/xmlapi/termsofuse">'
        '<item type="boardgame" id="187645"><thumbnail>https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__thumb/img'
        "/gAxzddRVQiRdjZHYFUZ2xc5Jlbw=/fit-in/200x150/filters:strip_icc()/pic4325841.jpg</thumbnail><image>"
        "https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__original/img/GKueTbkCk2Ramf6ai8mDj-BP6cI=/0x0/filters:"
        'format(jpeg)/pic4325841.jpg</image><name type = "primary" sortindex = "1" value = "Star Wars: Rebellion"/>'
        '<name type="alternate" sortindex="1" value="Star Wars: Lázadás"/><description>StarWars:Rebellion is a board game'
        ' of epic conflict.</description><yearpublished value="2016"/><minplayers value="2"/><maxplayers value="4"/>'
        '<link type="boardgamemechanic" id="2057" value="Chit-Pull System"/><link type="boardgamemechanic" id="2023" value="Cooperative Game"/>'
        ' <statistics page="1"><ratings><average value="8.41956"/><ranks><rank type="subtype" id="1" name="boardgame" value="8"/>'
        ' </ranks><averageweight value="3.733" /></ratings></statistics></item>'
        '<item type="boardgame" id="6902"><name type="primary" sortindex="1" value="Tetris"/><description>'
        'The ultimate test of advanced territorial strategy.</description><yearpublished value="1989"/>'
        '<minplayers value="2"/><maxplayers value="2"/><link type="boardgamemechanic" id="2057" value="Chit-Pull System"/>'
        '<statistics page="1"><ratings><average value="5.63488" /><ranks>'
        ' <rank type="subtype" id="1" name="boardgame" value="17645"/></ranks><averageweight value="1.625"/>'
        " </ratings></statistics></item></items>"
    )
    expected_two_ids = [
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
            playstyle="cooperative",
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
            playstyle="competitive",
        ),
    ]
    one_id_response = (
        '<?xml version="1.0" encoding="utf-8"?><items termsofuse="https://boardgamegeek.com/xmlapi/termsofuse">'
        '<item type="boardgame" id="187645"><thumbnail>https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__thumb/img'
        "/gAxzddRVQiRdjZHYFUZ2xc5Jlbw=/fit-in/200x150/filters:strip_icc()/pic4325841.jpg</thumbnail><image>"
        "https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__original/img/GKueTbkCk2Ramf6ai8mDj-BP6cI=/0x0/filters:"
        'format(jpeg)/pic4325841.jpg</image><name type = "primary" sortindex = "1" value = "Star Wars: Rebellion"/>'
        '<name type="alternate" sortindex="1" value="Star Wars: Lázadás"/><description>StarWars:Rebellion is a board game'
        ' of epic conflict.</description><yearpublished value="2016"/><minplayers value="2"/><maxplayers value="4"/>'
        ' <statistics page="1"><ratings><average value="8.41956"/><ranks><rank type="subtype" id="1" name="boardgame" value="8"/>'
        ' </ranks><averageweight value="3.733" /></ratings></statistics></item></items>'
    )
    expected_one_id = [
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
            playstyle="competitive",
        )
    ]
    invalid_id_response = '<?xml version="1.0" encoding="utf-8"?><items termsofuse="https://boardgamegeek.com/xmlapi/termsofuse"></items>'
