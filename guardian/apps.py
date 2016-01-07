
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from . import monkey_patch_user
from .management import create_anonymous_user
from guardian.conf import settings


class GuardianConfig(AppConfig):
    name = 'guardian'

    def ready(self):
        if settings.MONKEY_PATCH:
            monkey_patch_user()

        if settings.ANONYMOUS_USER_ID is not None:
            post_migrate.connect(create_anonymous_user, sender=self)
