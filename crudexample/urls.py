from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('salary/', views.salary),
    path('showsal/', views.showsal),
    path('editsal/<int:id>', views.editsal),
    path('updatesal/<int:id>', views.updatesal),
    # path('indexsal/', views.indexsal),
    path('indexsal1/', views.indexsal1, name='indexsal1'),
    path('deletesal/<int:id>', views.destroysal),
]
