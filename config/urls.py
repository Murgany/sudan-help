from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    # path('rosetta/', include('rosetta.urls')),
    path('', include('sudan_help.urls')),
)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('sudan_help.urls')),
# ]
