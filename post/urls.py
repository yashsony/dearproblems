#from django.views.generic import TemplateView
from django.conf.urls import url
from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

urlpatterns = [path('test/',views.ava),
               path('agreement/' ,views.agreement),
                path('', views.user_new),
               url(r'^login/$',views.loginView ),
               #url(r'^login/$', auth_views.login , {'template_name': 'registration/login.html'}),
               path('post/',views.formpost),
               path('list/', views.postlist),
               path('myacc/', views.profile),
               path('myacc1/', views.profile1),
               path('myacc2/', views.profile2),
               path('addcomment/<int:id>/', views.add_comment),
               path('ajax/add_like/', views.add_like),
               path('profile/<int:id>/', views.profile_others),
               path('profile1/<int:id>/', views.profile_others1),
               path('profile2/<int:id>/', views.profile_others2),
               path('<int:id>/', views.post_detail_view),
               path('search/', views.searchlist),
               path('logout/',views.logout_view),
               path('setting/',views.settings),
               url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),

               ]