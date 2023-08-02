from .views import user_list_view ,user_detail_view
from django.urls import path , include



urlpatterns = [
    
    path('list/' , user_list_view),
    path('detail/<id>' , user_detail_view)
]