from datetime import datetime


def today():
    return datetime.now().strftime("%Y-%m-%d")


def days_until(date_str):
    d = datetime.strptime(date_str, "%Y-%m-%d")
    return (d - datetime.now()).days
