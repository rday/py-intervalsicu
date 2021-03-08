from .api.workout import WorkoutDoc
from .api.activity import Activity
from .api.intervals import Intervals




class Error(dict):
    fields = [
        "status",
        "error",
        "message",

        "path",
        "timestamp",
    ]
