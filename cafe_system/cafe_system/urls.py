from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('order.urls', namespace='order')),
    path('api/', include('api.urls'))
]


handler500 = 'pages.views.server_error'
handler404 = 'pages.views.page_not_found'
handler403 = 'pages.views.csrf_failure'
