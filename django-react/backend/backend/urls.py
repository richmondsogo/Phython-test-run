from django.contrib import admin
from django.urls import path , include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token", TokenObtainPairView.as_view(), name="token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
]

#  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3NTA0MzE3NiwiaWF0IjoxNzc0OTU2Nzc2LCJqdGkiOiIyNTM5ZmM0NjM5Nzk0ZDhmYWU2NGQ4MTgyMmJhMDQ4NiIsInVzZXJfaWQiOiIxIn0.gxfhCg_kuQA1qQH1diucDPhenf50y5aJEQQhLj1Az4w",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc0OTU4NTc2LCJpYXQiOjE3NzQ5NTY3NzYsImp0aSI6IjcxODI1ZTlmYTgyMjRjMDliYTg3NzAzNmY1YTA3OGYzIiwidXNlcl9pZCI6IjEifQ.kOImfj0OKZ-hz87vdSdQ1t_3pMBiouWS0gm3ynMZ4XA"
