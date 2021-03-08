class CredentialError(IOError):
    def __init__(self, *args, **kwargs):
        self.status = kwargs['status']
        self.message = kwargs['message']
        self.url = kwargs['url']
