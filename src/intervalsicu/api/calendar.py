class Calendar(dict):
    fields = [
        'id',
        'name',
        'type',
        'uid',
        'url',
        'updated',
        'enabled',
        'defaultCategory',
        'external',
    ]

    def __init__(self, **kwargs):
        for field in kwargs.keys():
            if field not in Calendar.fields:
                raise TypeError("Unknown property {}".format(field))

        dict.__init__(self, **kwargs)
