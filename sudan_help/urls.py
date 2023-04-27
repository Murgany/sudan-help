from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, search_request, medical_service_list, missing_persons_reports
from django.views.i18n import set_language

urlpatterns = [
                  path('', index, name='index'),
                  path('search/', search_request, name='search'),
                  path('medical_services/', medical_service_list, name='medical_services'),
                  path('missing_persons/', missing_persons_reports, name='missing_persons'),
                  path('set-language/', set_language, name='set_language'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
