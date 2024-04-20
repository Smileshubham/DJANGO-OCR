"""
URL configuration for mycam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from camer.views import capture_image
# from django.conf import settings
# from django.conf.urls.static import static


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('capture/', capture_image, name='capture_image'),
# ]
# urlpatterns+=static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
# )

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from camer.views import capture_image, home,open_camera,opencam  # Import the home view
# from camer.views import home, camera


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home, name='home'),  # Define a URL pattern for the root URL
#     path('camera/', capture_image, name='capture_image'),
# ]



urlpatterns = [
    path('', home, name='index'),
    path('open_camera/', open_camera, name='open_camera'),
    path('capture/', capture_image, name='capture'),
    path('opencam/', opencam, name='opencam'),
]

# urlpatterns = [
#     path('', home, name='index'),
#     path('camera/', camera, name='camera'),
# ]



# Add URL patterns for serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
