import requests
import datetime

from .error import CredentialError, ClientError
from .workout import Workout, Folder
from .activity import Activity
from .event import Event
from .wellness import Wellness
from .calendar import Calendar


class Intervals(object):
    """
    This is the API class that applications interact with.
    Pass your athlete_id and api_key, and then make calls.
    """
    URL = "https://intervals.icu"

    def __init__(self, athlete_id, api_key, session=None):
        """
        Create a new IntervalsICU API object

        :param athlete_id: Your athlete_id
        :type athlete_id: int
        :rtype: :class:Intervals
        """
        self.athlete_id = athlete_id
        self.password = api_key
        self.session = session

    def _get_session(self):
        if self.session is not None:
            return self.session

        self.session = requests.Session()

        self.session.auth = ('API_KEY', self.password)
        return self.session

    def _make_request(self, method, url, params=None, json=None):
        session = self._get_session()
        res = session.request(method, url, params=params, json=json)

        if res.status_code == 401:
            raise CredentialError(
                status=res.status_code,
                message="Unauthorized",
                url=res.url)
        if res.status_code == 403:
            raise ClientError(
                status=res.status_code,
                message="Error accessing resource",
                url=res.url)
        if res.status_code == 404:
            raise ClientError(
                status=res.status_code,
                message="Resource not found",
                url=res.url)

        return res

    def activities(self):
        """
        Returns all your activities formatted in CSV

        :return: Text data in CSV format
        :rtype: str
        """
        url = "{}/api/v1/athlete/{}/activities.csv".format(
            Intervals.URL, self.athlete_id)
        res = self._make_request("get", url)
        return res.text

    def activity(self, activity_id):
        """
        Returns an :class:`Activity` by ID

        :param activity_id: Activity id number
        :type activity_id: int
        :return: Activity Object
        :rtype: :class:`Activity`
        """
        url = "{}/api/v1/activity/{}".format(Intervals.URL, activity_id)
        res = self._make_request("get", url)
        return Activity(**res.json())

    def calendars(self):
        """
        Returns a list of :class:`Calendar` objects

        :return: List of :class:`Calendar`
        :rtype: [:class:`Calendar`]
        """
        url = "{}/api/v1/athlete/{}/calendars".format(Intervals.URL, self.athlete_id)
        res = self._make_request("get", url)
        calendars = []
        for c in res.json():
            calendars.append(Calendar(**c))

        return calendars

    def events(self, start_date, end_date):
        """
        Returns a list of :class:`Event` objects over a range of dates.
        A single date will return an object for that day.

        :param start_date: Starting date
        :type start_date: datetime.date
        :param end_date: End date
        :type end_date: datetime.date
        :return: List of Event objects
        :rtype: [:class:`Event`]
        """
        if type(start_date) is not datetime.date:
            raise TypeError("datetime required")

        if type(end_date) is not datetime.date:
            raise TypeError("datetime required")

        params = {}

        params['oldest'] = start_date.isoformat()
        params['newest'] = end_date.isoformat()
        url = "{}/api/v1/athlete/{}/events".format(
            Intervals.URL, self.athlete_id)

        res = self._make_request("get", url, params=params)
        events = []
        for e in res.json():
            events.append(Event(**e))

        return events

    def folders(self):
        """
        Retrieve a list of workout folders

        :return: List of Folder objects
        :rtype: [:class:`Folder`]
        """
        url = "{}/api/v1/athlete/{}/folders".format(
            Intervals.URL, self.athlete_id)
        res = self._make_request("get", url)
        folders = []
        for f in res.json():
            folders.append(Folder(**f))

        return folders

    def wellness(self, start_date, end_date=None):
        """
        Wellness by date, or range of dates.
        A single date will return a wellness object for that day.
        Specifying two dates (start and end) will return all wellness
        objects within the range.

        :param start_date: Starting date (or single date)
        :type start_date: datetime.date
        :param end_date: End date (or omit if only requesting a single date)
        :type end_date: datetime.date
        :return: List of Wellness objects
        :rtype: [:class:`Wellness`]
        """
        if type(start_date) is not datetime.date:
            raise TypeError("datetime required")

        params = {}

        if end_date is not None:
            if type(end_date) is not datetime.date:
                raise TypeError("datetime required")

            params['oldest'] = start_date.isoformat()
            params['newest'] = end_date.isoformat()
            url = "{}/api/v1/athlete/{}/wellness".format(
                Intervals.URL, self.athlete_id)
        else:
            url = "{}/api/v1/athlete/{}/wellness/{}".format(
                Intervals.URL, self.athlete_id, start_date.isoformat())

        res = self._make_request("get", url, params)
        j = res.json()
        if type(j) is list:
            result = []
            for item in j:
                result.append(Wellness(**item))
            return result

        return Wellness(**j)

    def wellness_put(self, wellness):
        """
        Update a wellness object.

        :param wellness: :class:`Wellness` object
        :type wellness: :class:`Wellness`
        :return: The updated :class:`Wellness` object
        :rtype: :class:`Wellness`
        """
        if type(wellness) is not Wellness:
            raise TypeError("Expected Wellness object")

        date = wellness['id']
        url = "{}/api/v1/athlete/{}/wellness/{}".format(
            Intervals.URL, self.athlete_id, date)
        res = self._make_request("put", url, json=wellness)
        return Wellness(**res.json())

    def workouts(self):
        """
        Return a list of all :class:`Workout` objects

        :return: List of :class:`Workout` objects
        :rtype: [:class:`Workout`]
        """
        url = "{}/api/v1/athlete/{}/workouts".format(
            Intervals.URL, self.athlete_id)

        res = self._make_request("get", url)
        j = res.json()
        if type(j) is list:
            result = []
            for item in j:
                result.append(Workout(**item))
            return result

        raise TypeError('Unexpected result from server')

    def workout(self, workout_id):
        """
        Return a single :class:`Workout` by ID

        :param workout_id: Id of workout
        :type workout_id: int
        :return: :class:`Workout` object
        :rtype: :class:`Workout`
        """
        url = "{}/api/v1/athlete/{}/workouts/{}".format(
            Intervals.URL, self.athlete_id, workout_id)

        res = self._make_request("get", url)
        return Workout(**res.json())
