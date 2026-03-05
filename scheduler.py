from datetime import date
from predictor import predict_next_period
from database import get_latest
from notifier import send_notification


def check_cycle():

    data = get_latest()

    if data is None:
        print("No cycle data found")
        return

    last_period, cycle_length = data

    next_period = predict_next_period(last_period, cycle_length)

    today = date.today()

    days_left = (next_period - today).days

    print("Days left:", days_left)

    if days_left == 2:
        send_notification("Reminder: Your period may start in 2 days")

    elif days_left == 1:
        send_notification("Reminder: Your period may start tomorrow")

    elif days_left == 0:
        send_notification("Your period may start today")

    else:
        print("No notification today")


if __name__ == "__main__":
    check_cycle()