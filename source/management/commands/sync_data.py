from django.core.management.base import BaseCommand
from jikanpy import Jikan

from source.forms import AnimeForm


class Command(BaseCommand):
    help = "Download data from site."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        jikan = Jikan()

        resp = jikan.top('anime')
        for data in resp['top']:
            print(data)
            form = AnimeForm(data=data)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
