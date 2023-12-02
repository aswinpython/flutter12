from.import views
from django.urls import path
app_name='androidapp'
urlpatterns = [

    path('',views.list,name='list'),
    path('android/<int:android_id>/',views.detail,name='detail'),
    path('add/',views.add_app,name='add_app'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')


]
