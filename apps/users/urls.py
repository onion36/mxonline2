#-*- coding:utf-8 -*-
from django.conf.urls import url

from .views import UserinfoView, UploadImageView

urlpatterns = [
    #用户信息
    url(r"^list/$", UserinfoView.as_view(), name="user_info"),

    #修改头像
    url(r"^image/uoload/$", UploadImageView.as_view(), name="image_upload"),
]