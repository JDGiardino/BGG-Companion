class UserIsNoneError(Exception):
    """Raised when a user is passed that cannot be found by BoardGameGeek API"""


class BoardGameIsNoneError(Exception):
    """A board game was passed that does not exist within BoardGameGeek."""


class UserHasNoCollection(Exception):
    """Raised when a user is passed that doesn't have a game collection saved on BoardGameGeek."""
