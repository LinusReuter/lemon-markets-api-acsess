
class LemonException(Exception):
    """Baseclass for exceptions raised by the sdk."""

    pass


class LemonConnectionException(LemonException):
    """Raised when there is a problem with the network connection."""

    pass


class LemonAPIException(LemonException):
    """
    Indicate an error with the status of an response.

    Parameters
    ----------
    status : int
        The response status that caused this error
    errormessage : str
        The human-readable error message

    Properties
    ----------
    status : int
        The response status that caused this error
    errormessage : str
        The human-readable error message

    """

    def __init__(self, status, errormessage):       # noqa
        self.status = status
        self.errormessage = errormessage
