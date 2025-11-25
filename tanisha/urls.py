"""
URL configuration for tanisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tanisha import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.hello_message, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("courses", views.courses, name="courses"),
    path("team", views.team, name="team"),
    path("testimonial", views.testimonial, name="testimonial"),    
    path("404", views.error404, name="404"),    
    path("blog", views.blog, name="blog"),
    path("mail/", views.test_mail, name="mail" ),
    path("send-mail/", views.send_mail, name="send-mail" ),
    path("api-product/", views.api_product, name="api-product" ),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)