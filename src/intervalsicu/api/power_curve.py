from intervalsicu.api.intervals_object import IntervalsObject


class PowerCurve(dict):
    fields = ["activities", "list"]

    def __init__(self, **kwargs):
        IntervalsObject.validate(set(PowerCurve.fields), set(kwargs.keys()))

        dict.__init__(self, **kwargs)
