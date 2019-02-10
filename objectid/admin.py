from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

from objectid.models import ContentProvider
from .models import Artwork


class ArtworkAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(ArtworkAdmin, self).get_urls()
        my_urls = [
            url(r'^fixartworkowner/$', self.fix_artwork_owner, name='fixartworkowner'),
        ]
        return my_urls + urls

    def fix_artwork_owner(self, request):
        default_content_provider = ContentProvider.objects.get(pk=1)
        artworks_query = Artwork.objects.all()
        for artwork in artworks_query:
            artwork.owner = default_content_provider
            artwork.save()
        message_body = 'Old database values of Artwork.owner changed to DefaultContentProvider: pk=1'
        messages.add_message(request, messages.INFO, message_body)
        return HttpResponseRedirect(self.get_admin_url())

    # https://stackoverflow.com/questions/10420271/django-how-to-get-admin-url-from-model-instance
    @staticmethod
    def get_admin_url():
        content_type = ContentType.objects.get_for_model(Artwork)
        return reverse("admin:%s_%s_changelist" % (content_type.app_label, content_type.model))


admin.site.register(Artwork, ArtworkAdmin)
