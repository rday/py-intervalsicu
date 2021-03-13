.. toctree::
    :hidden:

    autoapi/intervalsicu/index

=================
Intervals.icu API
=================

This is a Python API for interacting with the https://intervals.icu training site.
The goal is provide an API exposing all functionality of Intervals.icu. This is not
complete, and features are prioritized by customer need.

Find documentation for API calls in the :class:`intervalsicu.Intervals` class.
Other classes contain objects that are sent or received from Intervals.icu.

Installation
------------

.. code:: bash

    pip install intervalsicu

Examples
--------

Update a field in your wellness document

.. code:: python

    import pprint
    from datetime import date

    from intervalsicu import Intervals


    def wellness():
        svc = Intervals("MY ATHLETE ID", "MY API KEY")

        start = date.fromisoformat("2021-03-10")
        wellness = svc.wellness(start)
        wellness['restingHR'] = 57
        wellness = svc.wellness_put(wellness)
        pprint.pprint(wellness)


    if __name__ == "__main__":
        wellness()

Write all your activities to a CSV file

.. code:: python

    import csv
    import io

    from intervalsicu import Intervals


    def activities_to_csv():
        svc = Intervals("MY ATHLETE ID", "MY API KEY")

        activities_csv = io.StringIO(svc.activities())

        with open('example/activities.csv', 'w') as w:
            reader = csv.reader(activities_csv)
            writer = csv.writer(w)
            
            for row in reader:
                writer.writerow(row)


    if __name__ == "__main__":
        activities_to_csv()

Download a list of events in JSON.

.. code:: python

    import pprint
    from datetime import date

    from intervalsicu import Intervals


    def events():
        svc = Intervals("MY ATHLETE ID", "MY API KEY")

        start = date.fromisoformat("2021-03-08")
        end = date.fromisoformat("2021-03-09")
        events = svc.events(start, end)
        pprint.pprint(events)


    if __name__ == "__main__":
        events()
