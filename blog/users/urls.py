#进行users子应用的视图路由
from django.urls import path
from users.views import RegisterView

urlpatterns=[
    #path的第一个参数就是：路由
    path('register/',RegisterView.as_view(),name='register'),
]