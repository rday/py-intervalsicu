import logging
from ..api import config


class IntervalsObject(dict):
    """
    Allows validation of responses from the server.
    If the module's configuration enforces strict
    validation, then an error is raised and details
    are logged.
    """
    def validate(expected, remote):
        if config['strict_validation'] is False:
            return

        new_fields = remote - expected
        deprecated_fields = expected - remote

        if new_fields or deprecated_fields:
            logging.debug("Remove {}".format(deprecated_fields))
            logging.debug("Add {}".format(new_fields))
            logging.debug((expected - deprecated_fields) | new_fields)
            raise TypeError("Validation failed")
