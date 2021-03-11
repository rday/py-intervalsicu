from .workout import WorkoutDoc


class Event(dict):
    fields = [
        'id',
        'start_date_local',
        'icu_training_load',
        'icu_atl',
        'icu_ctl',
        'calendar_id',
        'uid',
        'category',
        'end_date_local',
        'name',
        'description',
        'type',
        'indoor',
        'color',
        'moving_time',
        'icu_ftp',
        'atl_days',
        'ctl_days',
        'updated',
        'not_on_fitness_chart',
        'workout_doc',
        'push_errors',
        'plan_athlete_id',
        'plan_folder_id',
        'plan_workout_id',
        'plan_applied',
        'icu_intensity']

    def __init__(self, **kwargs):
        for field in kwargs.keys():
            if field not in Event.fields:
                raise TypeError("Unknown property {}".format(field))

        if kwargs.get('workout_doc') is not None:
            kwargs['workout_doc'] = WorkoutDoc(**kwargs['workout_doc'])

        dict.__init__(self, **kwargs)

    def __setitem__(self, key, value):
        if key not in Event.fields:
            raise TypeError("Unknown property {}".format(key))

        dict.__setitem__(self, key, value)
