from django.conf.urls import url,include
from contact.views import contact


urlpatterns = [
    url(r'^$', contact, name='contact'),

]


