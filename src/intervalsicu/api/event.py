from .workout import WorkoutDoc
from intervalsicu.api.intervals_object import IntervalsObject


class Event(dict):
    fields = [
        'joules',
        'icu_training_load',
        'icu_intensity',
        'category',
        'description', 'plan_applied', 'id', 'moving_time',
        'plan_workout_id', 'workout_doc', 'target', 'calendar_id',
        'ctl_days', 'color', 'uid', 'indoor', 'load_target', 'type',
        'push_errors', 'distance_target', 'joules_above_ftp', 'time_target',
        'not_on_fitness_chart', 'plan_folder_id', 'atl_days', 'icu_ctl',
        'updated', 'plan_athlete_id', 'icu_ftp', 'end_date_local',
        'start_date_local', 'icu_atl', 'name',
        'distance', 'athlete_cannot_edit', 'hide_from_athlete',
        'created_by_id']

    def __init__(self, **kwargs):
        IntervalsObject.validate(set(Event.fields), set(kwargs.keys()))

        if kwargs.get('workout_doc') is not None:
            kwargs['workout_doc'] = WorkoutDoc(**kwargs['workout_doc'])

        dict.__init__(self, **kwargs)

    def __setitem__(self, key, value):
        if key not in Event.fields:
            raise TypeError("Unknown property {}".format(key))

        dict.__setitem__(self, key, value)
