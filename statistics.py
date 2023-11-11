import os
import sys
import datetime

from collections import defaultdict
from garminconnect import Garmin


ABSOLUTE_START_DATE = datetime.date(2020, 7, 31)
ABSOLUTE_END_DATE = datetime.date.today()
API_DATE_FORMAT = '%Y-%m-%d'
PAD = 4 * ' '


def main() -> int:
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    garmin = Garmin(email, password)
    garmin.login()

    activities = garmin.get_activities_by_date(ABSOLUTE_START_DATE.strftime(API_DATE_FORMAT),
                                               ABSOLUTE_END_DATE.strftime(API_DATE_FORMAT))

    activity_counts = defaultdict(int)
    for activity in activities:
        activity_counts[activity['activityType']['typeKey']] += 1

    print(f"Training statistics from {ABSOLUTE_START_DATE} to {ABSOLUTE_END_DATE}:")
    for key in sorted(activity_counts.keys(), key=lambda k: activity_counts[k], reverse=True):
        print(f'{PAD}{key}: {activity_counts[key]}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
