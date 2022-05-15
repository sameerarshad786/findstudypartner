from django.urls import path
from . import views
from .views import RoomListView, RoomCreateView, RoomDetailView, RoomUpdateView, RoomDeleteView

urlpatterns = [
    path('', RoomListView.as_view(), name='home'),
    path('create_room/', RoomCreateView.as_view(), name='createroom'),
    path('room/<int:pk>/detail/', RoomDetailView.as_view(), name='room'),
    path('room/<int:pk>/update/', RoomUpdateView.as_view(), name='room-update'),
    path('room/<int:pk>/delete/?next=/your_profile/', RoomDeleteView.as_view(), name='room-delete'),
    path('topics/', views.topics, name='topics'),
]