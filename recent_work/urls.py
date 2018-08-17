from django.conf.urls import url, include
from recent_work.views import recent_work


urlpatterns = [
    url(r'^$', recent_work, name='recent_work'),

]





