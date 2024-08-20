import datetime


def get_current_date_string():
    today = datetime.datetime.now()
    month = today.month
    if month < 10:
        month = '0'+str(month)
    day = today.day
    if day < 10:
        day = '0' + str(day)
    year = today.year - 2000
    DATE_STRING = "{}{}{}".format(year,month,day)
    return DATE_STRING