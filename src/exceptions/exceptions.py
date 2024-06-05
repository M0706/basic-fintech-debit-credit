class InvalidPayloadException(Exception):
    pass


class AuthenticationException(Exception):
    pass


class ConnectionError(Exception):
    pass


class UpstreamConnectError(Exception):
    pass

class InternalServerError(Exception):
    pass
