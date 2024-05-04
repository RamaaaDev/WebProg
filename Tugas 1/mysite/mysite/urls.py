<<<<<<< HEAD:mysite/mysite/urls.py
from django.urls import path
from polls import views

urlpatterns = [
    path("", views.index, name="index"),
]
=======
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
]
>>>>>>> 669a287246c7461e674983080a9f2b7dff42678f:Tugas 1/mysite/mysite/urls.py
