from django.urls import path
from community import views

urlpatterns = [
    path('write/', views.write),
    path('list/', views.list),
    path('view/<int:num>', views.view)
]
