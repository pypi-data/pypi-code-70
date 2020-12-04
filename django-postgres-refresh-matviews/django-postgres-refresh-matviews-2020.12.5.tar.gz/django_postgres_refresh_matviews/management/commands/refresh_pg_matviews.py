from django.core.management.base import BaseCommand

from django_postgres_refresh_matviews.utils import refresh_pg_matviews


class Command(BaseCommand):

    def handle(self, *args, **options):
        refresh_pg_matviews()
