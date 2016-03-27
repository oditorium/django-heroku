"""
Useful Django decorators and mixins

- `ignore_failing` and `ignore_long` are decorators that can be used for unit tests

Copyright (c) Stefan LOESCH, oditorium 2016. All Rights Reserved.
Licensed under the MIT License <https://opensource.org/licenses/MIT>.
"""
from django.http import HttpResponse
from django.conf import settings



####################################################################
## ignore_failing (decorator)
def ignore_failing(function):
    """
    tests decorated with this are ignored if settings.TESTS_IGNORE_FAILING=True
    """
    def wrapped(*args, **kwargs):
        try: ignore = settings.TESTS_IGNORE_FAILING
        except: ignore = False
        if ignore: return
        return function(*args, **kwargs)

    if (function.__doc__ != None):
        wrapped.__doc__=function.__doc__+"\n\n[decorated by @ignore_failing]\n"
    wrapped.__name__=function.__name__
    return wrapped



####################################################################
## ignore_long (decorator)
def ignore_long(function):
    """
    tests decorated with this are ignored if settings.TESTS_IGNORE_FAILING=True
    """
    def wrapped(*args, **kwargs):
        try: ignore = settings.TESTS_IGNORE_LONG
        except: ignore = False
        if ignore: return
        return function(*args, **kwargs)

    if (function.__doc__ != None):
        wrapped.__doc__=function.__doc__+"\n\n[decorated by @ignore_long]\n"
    wrapped.__name__=function.__name__
    return wrapped