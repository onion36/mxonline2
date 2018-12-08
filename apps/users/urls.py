#-*- coding:utf-8 -*-
from django.conf.urls import url

from .views import UserinfoView, UploadImageView, UpdatePwdView, SendMailCodeView, UpdateEmailView
from .views import MyCourseView, MyFavOrgView, MyFavTeacher, MyFavCourseView, MyMessageView

urlpatterns = [
    #用户信息
    url(r"^list/$", UserinfoView.as_view(), name="user_info"),

    #修改头像上传
    url(r"^image/uoload/$", UploadImageView.as_view(), name="image_upload"),

    #用户个人中心修改密码
    url(r"^update/pwd/$", UpdatePwdView.as_view(), name="update_pwd"),

    #发送邮箱验证码
    url(r"^sendemail_code/$", SendMailCodeView.as_view(), name="sendemail_code"),

    #修改邮箱
    url(r"^update_email/$", UpdateEmailView.as_view(), name="update_email"),

    #我的课程
    url(r"^mycourse/$", MyCourseView.as_view(), name="mycourse"),

    #我收藏的课程机构
    url(r"^myfav/org/$", MyFavOrgView.as_view(), name="myfav_org"),

    # 我收藏的课程机构
    url(r"^myfav/teacher/$", MyFavTeacher.as_view(), name="myfav_teacher"),

    # 我收藏的课程机构
    url(r"^myfav/course/$", MyFavCourseView.as_view(), name="myfav_course"),

    # 我收藏的课程机构
    url(r"^mymessage/$", MyMessageView.as_view(), name="mymessage"),
]










