from django.urls import path
from .views import HomePageView, ClubListView, TourListView, MemListView, ClubDetailView, ClubCreateView, TGListView, query1, query2

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('clublist/', ClubListView.as_view(), name='c_list'),
    path('memlist/', MemListView.as_view(), name='m_list'),
    path('tourlist/', TourListView.as_view(), name='t_list'),
    path('<int:pk>/', ClubDetailView.as_view(), name='c_detail'),
    path('tglist/', TGListView.as_view(), name='tg_list'),
    path('new/', ClubCreateView.as_view(), name='c_new'),
    path('query1/', query1, name='query1'),
    path('query2/', query2, name='query2'),
]