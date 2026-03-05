from datetime import datetime, timedelta

def predict_next_period(last_period, cycle_length):

    last_date = datetime.strptime(last_period, "%Y-%m-%d")

    next_period = last_date + timedelta(days=cycle_length)

    return next_period.date()


def fertile_window(last_period, cycle_length):

    last_date = datetime.strptime(last_period, "%Y-%m-%d")

    ovulation = last_date + timedelta(days=(cycle_length - 14))

    fertile_start = ovulation - timedelta(days=5)
    fertile_end = ovulation + timedelta(days=1)

    return fertile_start.date(), fertile_end.date()