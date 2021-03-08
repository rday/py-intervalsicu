import pytest
from datetime import date

from intervalsicu import Intervals
from intervalsicu import Activity
from intervalsicu import Wellness
from intervalsicu import Folder


class MockResponse(object):
    def __init__(self, status_code, url):
        self.text = ''
        self.status_code = status_code
        self.url = url

    def json(self):
        if 'activity' in self.url:
            return Activity()
        if 'wellness' in self.url:
            return Wellness()
        if 'folders' in self.url:
            return Folder()


class MockSession(object):
    def __init__(self):
        pass

    def request(self, method, url, params=None, json=None):
        return MockResponse(200, url)


@pytest.fixture
def intervals_svc():
    my_session = MockSession()
    return Intervals("TEST", "TEST", my_session)


def test_activities(intervals_svc):
    intervals_svc.activities()


def test_activity(intervals_svc):
    intervals_svc.activity(12345)


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


def test_folders(intervals_svc):
    intervals_svc.folders()
