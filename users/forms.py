import os
from django.core import management
from django import forms

from .models import CustomUser, ContentProvider
from objectid.models import Artwork

CHOICES = [('1', 'ContentProvider'),
           ('2', 'CustomUser'),
           ('3', 'ArtWork')]

MODELS = {'1': CustomUser, '2': ContentProvider, '3': Artwork}

app_names = {key: model._meta.app_label for key, model in MODELS.items()}


def get_exists_fixtures():
    fixture_files = dict()
    for root, dirs, files in os.walk("fixtures"):
        for file in files:
            app_set = set()
            for key, app in app_names.items():
                if app in app_set or app not in root:
                    continue
                if file.endswith(".json"):
                    print(os.path.join(root, file))
                    fixture = os.path.join(root, file)
                    if not fixture_files.get(key):
                        fixture_files[key] = []
                    fixture_files[key].append(fixture)
                    app_set.add(app)
    return fixture_files


def get_fixtures_choices():
    choices = []
    for key, values in get_exists_fixtures().items():
        if isinstance(values, list):
            for v in values:
                choices.append([v, v])
    print(choices)
    return choices


class FixtureDumpForm(forms.Form):
    available_model_for_dump = forms.MultipleChoiceField(choices=CHOICES,
                                                         widget=forms.CheckboxSelectMultiple(),
                                                         label='select models for dump')

    def clean(self):
        return super(FixtureDumpForm, self).clean()

    def create_fixtures(self, model, ext="json"):
        filename = "fixtures/{app_label}/{model_name}.{ext}".format(app_label=model._meta.app_label,
                                                                    model_name=model._meta.object_name,
                                                                    ext=ext)
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        with open(filename, 'w+', buffering=1024) as f:
            management.call_command('dumpdata', model._meta.app_label, indent=4, stdout=f)
        print("fixtures are created")


class FixtureLoadForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FixtureLoadForm, self).__init__(*args, **kwargs)
        self.fields['available_fixture'] = forms.MultipleChoiceField(choices=get_fixtures_choices(),
                                                                     widget=forms.CheckboxSelectMultiple(),
                                                                     label='select fixtures for load')

    @classmethod
    def loaddata_fixtures(cls, fixture):
        management.call_command('loaddata', fixture)
        print("fixture are load")


if __name__ == "__main__":
    print("Hello")
