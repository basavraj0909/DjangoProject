
from django.contrib import admin
from django.urls import path, include

# from watchmate import watchlist_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('watchlist_app.api.urls')),
]