#-*- coding:utf-8 -*-
from django.conf.urls import url

from .views import CourseListView


urlpatterns = [
    url('^list/$', CourseListView.as_view(), name="course_list"),
]