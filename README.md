# Intervals.ICU Python API

This API provides a basic interface to work with the Intervals.ICU.
You can obtain further documentation for the Intervals.ICU site by
following the instructions from [this post](https://forum.intervals.icu/t/api-access-to-intervals-icu/609).

API functionality is described in the thread above. This API aims to provide all functionality, but there are gaps. Please open an issue (or a PR) for any missing functionality.

Full documentation can be found [here](https://py-intervalsicu.readthedocs.io)

# Examples

Update a field in your wellness document

```python
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
```

Write all your activities to a CSV file

```python
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
```

Download a list of events in JSON.

```python
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
```
