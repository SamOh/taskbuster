from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.task_homepage, name='home'),
    url(r'^add/$', views.add_task, name='add_task'),
]
