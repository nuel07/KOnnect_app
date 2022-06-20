from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    # music
    path('', views.IndexView.as_view(), name='index'),

    # registration link
    path('register/', views.UserFormView.as_view(), name='register'),

    # music/id/
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    # /music/album/add/
    path('<int:album-add/pk>/', views.AlbumCreate.as_view(), name='album-add'),

    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

]
