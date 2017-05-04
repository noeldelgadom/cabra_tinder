from django.conf.urls import url
from django.contrib import admin
from app_one import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/goats/$',views.Goats.as_view()),
    url(r'^$', views.index, name='index')
]
