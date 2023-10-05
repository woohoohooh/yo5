from a.yoomoney_api.examples import history


def my_scheduled_job():
    history.check()
