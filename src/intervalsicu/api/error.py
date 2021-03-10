class CredentialError(IOError):
    def __init__(self, *args, **kwargs):
        self.status = kwargs['status']
        self.message = kwargs['message']
        self.url = kwargs['url']

    def __str__(self):
        return "Credentials Error: {}".format(
            self.message)


class ClientError(IOError):
    def __init__(self, *args, **kwargs):
        self.status = kwargs['status']
        self.message = kwargs['message']
        self.url = kwargs['url']

    def __str__(self):
        return "Client Error {}: {}: {}".format(
            self.status, self.url, self.message)
