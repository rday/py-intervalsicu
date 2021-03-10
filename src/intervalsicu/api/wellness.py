class Wellness(dict):
    fields = [
        'diastolic',
        'fatigue',
        'hrv',
        'hrvSDNN',
        'hydration',
        'id',
        'kcalConsumed',
        'menstrualPhase',
        'menstrualPhasePredicted',
        'mood',
        'motivation',
        'restingHR',
        'sleepQuality',
        'sleepSecs',
        'soreness',
        'spO2',
        'stress',
        'systolic',
        'updated',
        'weight',
        ]

    def __init__(self, **kwargs):
        for field in kwargs.keys():
            if field not in Wellness.fields:
                raise TypeError("Unknown property {}".format(field))

        dict.__init__(self, **kwargs)

    def __setitem__(self, key, value):
        if key not in Wellness.fields:
            raise TypeError("Unknown property {}".format(key))

        dict.__setitem__(self, key, value)
