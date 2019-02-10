from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

from .models import CustomUser, ContentProvider
from .forms import FixtureDumpForm, FixtureLoadForm, MODELS


@admin.register(CustomUser, ContentProvider)
class CustomUserAdmin(admin.ModelAdmin):
    # change_form_template = "admin/change_list.html"

    def get_urls(self):
        urls = super(CustomUserAdmin, self).get_urls()
        print(urls)
        my_urls = [
            url(r'^usercontentprovider/$', self.fix_user_contentprovider, name='usercontentprovider'),
        ]
        return my_urls + urls

    def fix_user_contentprovider(self, request):
        print("fix_contentprovider!!!")
        message_body = 'Old database values of User.content_provider changed to DefaultContentProvider'
        messages.add_message(request, messages.INFO, message_body)
        return HttpResponseRedirect(self.get_admin_url())

    # https://stackoverflow.com/questions/10420271/django-how-to-get-admin-url-from-model-instance
    @staticmethod
    def get_admin_url():
        content_type = ContentType.objects.get_for_model(ContentProvider)
        return reverse("admin:%s_%s_changelist" % (content_type.app_label, content_type.model))

    def changelist_view(self, request, extra_context=None):
        if request.method == "POST" and 'dumpdata' in request.POST:
            form = FixtureDumpForm(request.POST)
            if form.is_valid():
                selected_models = form.cleaned_data['available_model_for_dump']
                try:
                    for model in selected_models:
                        form.create_fixtures(model=MODELS[model])
                        print("dump for {}".format(MODELS[model]))
                except Exception:
                    message_body = 'Error! Dumpdata not executed'
                    messages.add_message(request, messages.ERROR, message_body)
                return super(CustomUserAdmin, self).changelist_view(request, {'form': FixtureDumpForm, 'formb': FixtureLoadForm})

        elif request.method == "POST" and 'loaddata' in request.POST:
            form = FixtureLoadForm(request.POST)
            if form.is_valid():
                selected_fixtures = form.cleaned_data['available_fixture']
                for sel in selected_fixtures:
                    try:
                        form.loaddata_fixtures(sel)
                    except Exception:
                        message_body = 'Error! Try loaddata later'
                        messages.add_message(request, messages.ERROR, message_body)
                return super(CustomUserAdmin, self).changelist_view(request, {'form': FixtureDumpForm, 'formb': FixtureLoadForm})
        else:
            extra_context = extra_context or {}
            extra_context['form'] = FixtureDumpForm
            return super(CustomUserAdmin, self).changelist_view(request, {'form': FixtureDumpForm, 'formb': FixtureLoadForm})
