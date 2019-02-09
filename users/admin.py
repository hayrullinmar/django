from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    # change_form_template = "admin/change_list.html"
    def response_change(self, request, obj):
        if "_make-unique" in request.GET:
            # matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            # matching_names_except_this.delete()
            # obj.is_unique = True
            # obj.save()
            print("response_change")
            self.message_user(request, "This villain is now unique")
            return HttpResponseRedirect(".")

        else:
            print("Not response_change")
        return super().response_change(request, obj)

admin.site.register(CustomUser, CustomUserAdmin)
