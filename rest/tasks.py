# Create your tasks here
from __future__ import absolute_import, unicode_literals

import logging
from time import sleep

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task(name="print_msg_with_name")
def print_message(name, *args, **kwargs):
    for i in range(3):
        sleep(1)
        print(f'{i} seconds')
    print("Celery is working!! {} have implemented it correctly.".format(name))
