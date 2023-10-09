from django.urls import path
from . import views
app_name = 'movies'

urlpatterns = [
      # /movies/
      path('', views.index, name='index'),
      # /movies/id  e.g. /movies/1
      path('<int:movie_id>/', views.show, name='show'),
      path('update/<int:id>', views.update, name='update'),
      path('delete/<int:id>', views.delete, name='delete'),
      path('updaterecord/<int:id>', views.updaterecord),
      path('new/', views.new, name='new'),
      path('newrecord/', views.newRecord, name='newRecord')
  ]