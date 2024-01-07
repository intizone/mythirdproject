from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from MyApp.views import *

urlpatterns = [
    # path('', example, name='example'),
    # path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('MyApp.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)