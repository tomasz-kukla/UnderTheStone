import datetime

from django.core.validators import ValidationError
from django.utils.dateparse import parse_datetime


start_reservation_time = datetime.datetime.strptime('10:00', "%H:%M").time()
end_reservation_time = datetime.datetime.strptime('23:59', "%H:%M").time()


def validate_start(value_start):
    if isinstance(value_start, str):
        value_start = parse_datetime(value_start)

    value_start_time = value_start.time()
    value_start_date = value_start.replace(tzinfo=None)
    if(value_start_date < datetime.datetime.now()):
        raise ValidationError("The selected time is in the past.")
    if not (value_start_time.minute in [0, 30]):
        raise ValidationError(f"The only minutes selection possibilities are: 00 or 30. Your minutes selected: {value_start_time.minute}")
    if(value_start_time >= start_reservation_time):
        return value_start
    else:
        raise ValidationError("Start time is below restaurants' opening hour.")


def validate_end(value_start, value_end):

    if isinstance(value_start, str):
        value_start = parse_datetime(value_start)
    if isinstance(value_end, str):
        value_end = parse_datetime(value_end)

    value_end_time = value_end.time()

    value_start_date = value_start.replace(tzinfo=None)
    value_end_date = value_end.replace(tzinfo=None)

    duration = value_end_date - value_start_date

    if value_end_date < datetime.datetime.now():
        raise ValidationError("The selected time is in the past.")

    if end_reservation_time >= value_end_time >= start_reservation_time:
        if(datetime.timedelta(hours=4) < duration or duration < datetime.timedelta(minutes=30)):
            if(end_reservation_time.minute == datetime.timedelta()):
                raise ValidationError(f"End reservation time cannot be before start reeservation time")
            if(duration > datetime.timedelta(days=1)):
                raise ValidationError(f"Different days (dates).")
            if not (value_end_time == end_reservation_time):
                raise ValidationError(f"Minimum reservation time: 30 minutes, max: 4h. Selected duration: {duration}")
        if duration % datetime.timedelta(seconds=1800) != datetime.timedelta():
            if(value_end_time != end_reservation_time):

                if not value_end_time.minute in [0, 30]:
                    raise ValidationError(f"The only minutes selection possibilities are: 00 or 30. Your minutes selected: {value_end_time.minute}")
                raise ValidationError(f"The time unit is 30 minutes. Your selected time: {duration}")
        return value_end
    else:
        raise ValidationError(f"End time is past restaurants' closing hour.{duration > datetime.timedelta(hours=4)}")
