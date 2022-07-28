from intervalsicu.api.intervals_object import IntervalsObject


class Wellness(dict):
    fields = [
        'id',
        'ctl',
        'atl',
        'rampRate',
        'ctlLoad',
        'atlLoad',
        'sportInfo',
        'updated',
        'weight',
        'restingHR',
        'hrv',
        'hrvSDNN',
        'menstrualPhase',
        'menstrualPhasePredicted',
        'kcalConsumed',
        'sleepSecs',
        'sleepScore',
        'sleepQuality',
        'avgSleepingHR',
        'soreness',
        'fatigue',
        'stress',
        'mood',
        'motivation',
        'injury',
        'spO2',
        'systolic',
        'diastolic',
        'hydration',
        'hydrationVolume',
        'readiness',
        'baevskySI',
        'bloodGlucose',
        'lactate',
        'bodyFat',
        'abdomen',
        'vo2max',
        'comments',
        ]

    def __init__(self, **kwargs):
        IntervalsObject.validate(set(Wellness.fields), set(kwargs.keys()))

        dict.__init__(self, **kwargs)

    def __setitem__(self, key, value):
        if key not in Wellness.fields:
            raise TypeError(f'Unknown property {key}')

        dict.__setitem__(self, key, value)
