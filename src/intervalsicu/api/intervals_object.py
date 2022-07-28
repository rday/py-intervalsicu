import pprint
import logging
from typing import Type


class IntervalsObject(dict):
    def validate(expected, remote):
        new_fields = remote - expected
        deprecated_fields = expected - remote

        if new_fields or deprecated_fields:
            logging.debug("Remove {}".format(deprecated_fields))
            logging.debug("Add {}".format(new_fields))
            logging.debug((expected - deprecated_fields) | new_fields)
            raise TypeError("Validation failed")