from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.register, name='sign_up'),
    path('dashboard/admin/', views.adminpage, name='admin_page'),
    path('predict/result/', views.prediction2, name='predict_result'),
    path('exit/', views.exit, name='exit'),
    path('predict/', views.newprediction, name='new_predict'),
    path('match/', views.match, name='match'),
    path('match/result/', views.matchresult, name='match_result')
]

