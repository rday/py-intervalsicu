# Intervals.ICO Python API

This is a basic API to work with the Intervals.ICU Rest API.
You can obtain an API for the Intervals.ICU site by following the
instructions from (this post)[https://forum.intervals.icu/t/api-access-to-intervals-icu/609].

API functionality is described in the thread above. This API tries to provide all functionality,
but there are gaps. Please open an issue (or a PR) for any missing functionality.



# Example

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
