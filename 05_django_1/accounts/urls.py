from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles', include('articles.urls')),
    path('accounts', include('accounts.urls')),
]

