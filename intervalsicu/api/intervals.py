import requests
import datetime
from .workout import WorkoutDoc
from .activity import Activity
from .wellness import Wellness


class Intervals(object):
    URL = "https://intervals.icu"

    def __init__(self, athlete_id, api_key):
        self.athlete_id = athlete_id
        self.password = api_key
        self.session = None

    def _get_session(self):
        if self.session is not None:
            return self.session

        self.session = requests.Session()

        self.session.auth = ('API_KEY', self.password)
        return self.session

    def activities(self):
        """
        CSV formatted API call

        :return: Text data in CSV format
        """
        session = self._get_session()
        res = session.get("{}/api/v1/athlete/{}/activities.csv".format(Intervals.URL, self.athlete_id))
        return res.text

    def activity(self, activity_id):
        """
        Activity by ID

        :param: Activity id number
        :return: Activity Object
        """
        session = self._get_session()
        res = session.get("{}/api/v1/activity/{}".format(Intervals.URL, activity_id))
        return Activity(**res.json())

    def wellness(self, start_date, end_date=None):
        """
        Wellness by date, or range of dates.
        A single date will return a wellness object for that day.
        Specifying two dates (start and end) will return all wellness
        objects within the range.

        :param: Starting date (or single date)
        :param: End date (or omit if only requesting a single date)
        :return: List of Wellness objects
        """
        if type(start_date) is not datetime.date:
            raise TypeError("datetime required")

        params = {}

        if end_date is not None:
            if type(end_date) is not datetime.date:
                raise TypeError("datetime required")

            params['oldest'] = start_date.isoformat()
            params['newest'] = end_date.isoformat()
            url = "{}/api/v1/athlete/{}/wellness".format(Intervals.URL, self.athlete_id)
        else:
            url = "{}/api/v1/athlete/{}/wellness/{}".format(Intervals.URL, self.athlete_id, oldest)

        session = self._get_session()
        res = session.get(url, params=params)
        j = res.json()
        if type(j) is list:
            result = []
            for item in j:
                result.append(Wellness(**item))
            return result

        return Wellness(**j)

    def wellness_put(self, data):
        """
        Update a wellness object.

        :param: Wellness object
        :return: The updated wellness object
        """
        if type(data) is not Wellness:
            raise TypeError("Expected Wellness object")

        session = self._get_session()
        date = data['id']
        res = session.put("{}/api/v1/athlete/{}/wellness/{}".format(Intervals.URL, self.athlete_id, date), json=data)
        return Wellness(**res.json())

    def folders(self):
        """
        Retrieve a list of workout folders

        :return: List of Folder objects
        """
        session = self._get_session()
        res = session.get("{}/api/v1/athlete/{}/folders".format(Intervals.URL, self.athlete_id))
        folders = []
        for f in res.json():
            folders.append(Folder(**f))

        return folders


def recur(o, indent=0):
    for key, val in o.items():
        if type(val) is list:
            for item in val:
                recur(item, indent+1)
        elif type(val) is dict:
            recur(o[key], indent+1)
