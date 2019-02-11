# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from instapy import InstaPy


@shared_task()
def check_session(username, password):
    bot = InstaPy(username=username, password=password,
                  selenium_local_session=False)
    bot.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
    bot.login()
    bot.end()

@shared_task()
def like_by_tags(*args, **kwargs):
    bot = InstaPy(username=kwargs.get('username'),
                  password=kwargs.get('password'),
                  selenium_local_session=False)
    bot.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
    bot.login()
    bot.set_relationship_bounds(enabled=kwargs.get('enabled'),
                                potency_ratio=kwargs.get('potency_ratio'),
                                delimit_by_numbers=kwargs.get('delimit_by_numbers'),
                                max_followers=kwargs.get('max_followers'),
                                max_following=kwargs.get('max_following'),
                                min_followers=kwargs.get('min_followers'),
                                min_following=kwargs.get('min_following'))
    bot.like_by_tags(tags=kwargs.get('tags'),
                     amount=kwargs.get('amount'),
                     skip_top_posts=kwargs.get('skip_top_posts'),
                     use_smart_hashtags=kwargs.get('use_smart_hashtags'),
                     interact=kwargs.get('interact'),
                     randomize=kwargs.get('randomize'),
                     media=kwargs.get('media'))
    bot.end()
