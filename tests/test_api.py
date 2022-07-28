import pytest
from datetime import date

from intervalsicu import Activity, Calendar, Event, Intervals, Folder, Wellness, Workout


def to_kwargs(l):
    """Hack to set a None value for all known fields in an API call"""
    d = {}
    for k in l:
        d[k] = None

    return d


class MockResponse(object):
    def __init__(self, status_code, url):
        self.text = ''
        self.status_code = status_code
        self.url = url
        self.headers = None

    def json(self):
        """
        Hack to detect which URL is being accessed and return a mock
        object to the test.
        """
        if 'activity' in self.url:
            return Activity(**to_kwargs(Activity.fields))
        if 'events' in self.url:
            return [Event(**to_kwargs(Event.fields))]
        if 'wellness' in self.url:
            return Wellness(**to_kwargs(Wellness.fields))
        if 'folders' in self.url:
            return Folder(**to_kwargs(Folder.fields))
        if self.url.endswith('workouts'):
            return [Workout(**to_kwargs(Workout.fields))]
        if 'workout' in self.url:
            return Workout(**to_kwargs(Workout.fields))
        if 'calendar' in self.url:
            return [Calendar()]


class MockSession(object):
    def __init__(self):
        pass

    def request(self, method, url, params=None, json=None, headers=None):
        return MockResponse(200, url)


@pytest.fixture
def intervals_svc():
    my_session = MockSession()
    return Intervals("TEST", "TEST", my_session)


def test_activities(intervals_svc):
    intervals_svc.activities()


def test_activity(intervals_svc):
    intervals_svc.activity(12345)


def test_activity_put(intervals_svc):
    with pytest.raises(TypeError):
        intervals_svc.activity_put(0)

    intervals_svc.activity_put(Activity(id="id"))


def test_calendars(intervals_svc):
    intervals_svc.calendars()


def test_events(intervals_svc):
    with pytest.raises(TypeError):
        intervals_svc.events(date.fromisoformat("2020-01-01"), "2020-01-01")

    with pytest.raises(TypeError):
        intervals_svc.events("2020-01-01", date.fromisoformat("2020-01-01"))

    intervals_svc.events(
        date.fromisoformat("2020-01-01"),
        date.fromisoformat("2020-01-01"))


def test_folders(intervals_svc):
    intervals_svc.folders()


def test_wellness(intervals_svc):
    with pytest.raises(TypeError):
        intervals_svc.wellness()

    with pytest.raises(TypeError):
        intervals_svc.wellness("2020-01-01")

    with pytest.raises(TypeError):
        intervals_svc.wellness(date.fromisoformat("2020-01-01"), "2020-01-01")

    intervals_svc.wellness(date.fromisoformat("2020-01-01"))


def test_wellness_put(intervals_svc):
    with pytest.raises(TypeError):
        intervals_svc.wellness_put(0)

    intervals_svc.wellness_put(Wellness(id="id"))


def test_workouts(intervals_svc):
    intervals_svc.workouts()


def test_workout(intervals_svc):
    intervals_svc.workout(1)
