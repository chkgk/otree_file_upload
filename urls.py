from otree.urls import urlpatterns
from django.conf.urls.static import static
import settings

# additional url pattern for media url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)