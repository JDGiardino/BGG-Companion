from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import InputRequired, Optional, NumberRange, AnyOf


def convert_empty_string_to_none(arg):
    if arg == "":
        return None
    else:
        return arg


class RandomGameForm(FlaskForm):
    class Meta:
        csrf = False

    user = StringField(
        "user", validators=[InputRequired(message="A BoardGameGeek username is required")]
    )
    minplayers = IntegerField(
        "minplayers",
        filters=[convert_empty_string_to_none],
        validators=[
            Optional(),
            NumberRange(
                min=0,
                max=12,
                message="Number of players out of range.  Please only select between 0 - 12.",
            ),
        ],
    )
    maxplayers = IntegerField(
        "maxplayers",
        filters=[convert_empty_string_to_none],
        validators=[
            Optional(),
            NumberRange(
                min=0,
                max=12,
                message="Number of players out of range.  Please only select between 0 - 12.",
            ),
        ],
    )
    playerrangetype = StringField(
        "playerrangetype", filters=[convert_empty_string_to_none], validators=[Optional()]
    )
    playstyle = StringField(
        "playstyle", filters=[convert_empty_string_to_none], validators=[Optional()]
    )
    mincomplexity = DecimalField(
        "mincomplexity",
        filters=[convert_empty_string_to_none],
        validators=[
            Optional(),
            NumberRange(
                min=1,
                max=5,
                message="Complexity level out of range.  Please only select a value (with decimals) between 1 - 5.",
            ),
        ],
    )
    maxcomplexity = DecimalField(
        "maxcomplexity",
        filters=[convert_empty_string_to_none],
        validators=[
            Optional(),
            NumberRange(
                min=1,
                max=5,
                message="Complexity level out of range.  Please only select a value (with decimals) between 1 - 5.",
            ),
        ],
    )
