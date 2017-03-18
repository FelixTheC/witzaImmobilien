from django.conf.urls import include, url


urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    ]