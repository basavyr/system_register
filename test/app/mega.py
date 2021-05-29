from datetime import date, datetime
from . import app


def Give_Mega():
    return datetime.utcnow()


def Reverse_Mega():
    return f'{Give_Mega()} -> {app.SayHi()}'
