from django.urls import path
from .views import home_page

urlpatterns = [
    path('', home_page, name="home"),
    # path('create/', create_todo, name="create_todo"),
    # path('update/<int:id>/', update_view, name='update_view'),
    # path('delete/<int:id>/', delete_view, name='delete_view'),
    # path('show/<int:id>/', show_view, name='show_view'),

]
