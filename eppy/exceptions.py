from .doc import EppResponse


class EppException(Exception):
    def __init__(self, resp):
        if isinstance(resp, EppResponse):
            msg = "{%s} %s" % (resp.code, resp.message)
        else:
            msg = resp
        self.resp = resp
        super(EppException, self).__init__(msg)


class EppLoginError(EppException):
    pass