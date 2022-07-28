from intervalsicu.api.intervals_object import IntervalsObject


class Workout(dict):
    fields = [
        'athlete_id',
        'id',
        'icu_training_load',
        'name',
        'description',
        'type',
        'indoor',
        'color',
        'moving_time',
        'updated',
        'workout_doc',
        'folder_id',
        'day',
        'days',
        'plan_applied']

    def __init__(self, **kwargs):
        IntervalsObject.validate(set(Workout.fields), set(kwargs.keys()))

        if kwargs.get('workout_doc') is not None:
            kwargs['workout_doc'] = WorkoutDoc(**kwargs['workout_doc'])

        dict.__init__(self, **kwargs)


class WorkoutDoc(dict):
    fields = [
        'steps',
        'duration',
        'zoneTimes',
        'hrZoneTimes']

    def __init__(self, **kwargs):
        IntervalsObject.validate(set(WorkoutDoc.fields), set(kwargs.keys()))

        if kwargs.get('steps') is not None:
            steps = []
            for s in kwargs['steps']:
                steps.append(Step(**s))
            kwargs['steps'] = steps

        dict.__init__(self, **kwargs)


class Step(dict):
    fields = [
        'power',
        'duration']

    def __init__(self, **kwargs):
        IntervalsObject.validate(set(Step.fields), set(kwargs.keys()))

        if kwargs.get('steps') is not None:
            steps = []
            for s in kwargs['steps']:
                steps.append(Step(**s))
            kwargs['steps'] = steps

        if kwargs.get('power') is not None:
            kwargs['power'] = Power(**kwargs['power'])

        dict.__init__(self, **kwargs)


class Power(dict):
    fields = ['units', 'value']

    def __init__(self, **kwargs):
        IntervalsObject.validate(set(Power.fields), set(kwargs.keys()))

        dict.__init__(self, **kwargs)


class Folder(dict):
    fields = [
        'athlete_id',
        'id',
        'type',
        'name',
        'description',
        'start_date_local',
        'children',
        'canEdit',
        'sharedWithCount',
        'shareToken',
        'owner',
        'sharedFolderId']

    def __init__(self, **kwargs):
        IntervalsObject.validate(set(Folder.fields), set(kwargs.keys()))

        if kwargs.get('children') is not None:
            workouts = []
            for c in kwargs['children']:
                workouts.append(Workout(**c))
            kwargs['children'] = workouts

        dict.__init__(self, **kwargs)
