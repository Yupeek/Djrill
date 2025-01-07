import sys

from django import setup
from django.conf import settings
from django.test.utils import get_runner

APP = "djrill"


def runtests():
    test_runner_class = get_runner(settings)
    test_runner = test_runner_class()
    failures = test_runner.run_tests([APP])
    sys.exit(failures)


if __name__ == "__main__":
    settings.configure(
        SECRET_KEY="secret",
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        ROOT_URLCONF=APP + ".urls",
        INSTALLED_APPS=(APP,),
    )
    setup()
    runtests()
