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
        for field in kwargs.keys():
            if field not in Workout.fields:
                raise TypeError("Unknown property {}".format(field))

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
        for field in kwargs.keys():
            if field not in WorkoutDoc.fields:
                raise TypeError("Unknown property {}".format(field))

        if kwargs.get('steps') is not None:
            steps = []
            for s in kwargs['steps']:
                steps.append(Step(**s))
            kwargs['steps'] = steps

        dict.__init__(self, **kwargs)


class Step(dict):
    fields = [
        'ramp',
        'power',
        'warmup',
        'duration',
        'reps',
        'text',
        'steps',
        'cooldown',
        'cadence']

    def __init__(self, **kwargs):
        for field in kwargs.keys():
            if field not in Step.fields:
                raise TypeError("Unknown property {}".format(field))

        if kwargs.get('steps') is not None:
            steps = []
            for s in kwargs['steps']:
                steps.append(Step(**s))
            kwargs['steps'] = steps

        if kwargs.get('power') is not None:
            kwargs['power'] = Power(**kwargs['power'])

        dict.__init__(self, **kwargs)


class Power(dict):
    fields = ['end', 'start', 'units', 'value']

    def __init__(self, **kwargs):
        for field in kwargs.keys():
            if field not in Power.fields:
                raise TypeError("Unknown property {}".format(field))

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
        for field in kwargs.keys():
            if field not in Folder.fields:
                raise TypeError("Unknown property {}".format(field))

        if kwargs.get('children') is not None:
            workouts = []
            for c in kwargs['children']:
                workouts.append(Workout(**c))
            kwargs['children'] = workouts

        dict.__init__(self, **kwargs)
