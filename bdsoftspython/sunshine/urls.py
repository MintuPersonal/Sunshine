from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('demo/', views.demo, name='demo')
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
