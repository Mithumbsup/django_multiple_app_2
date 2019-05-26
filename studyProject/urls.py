from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import Portfolio.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.main, name='main'),
    path('Portfolio/',Portfolio.views.portfolio, name='Portfolio'),
    path('blog/', include('blog.urls')),
    path('Portfolio/', include('Portfolio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)