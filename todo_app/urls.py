from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.login, name='login'),
    path('entry', views.entry, name='entry'),
    path('logind',views.logind, name='logind'),
    path('user_created', views.user_creation, name='user_creation'),
    path('workspace/<str:username>', views.workspace, name='workspace'),
    path('workspaceHome/<str:username>', views.workspaceHome, name='workspaceHome'),
    path('workspaceTask/<str:username>', views.workspaceTask, name='workspaceTask'),
    path('workspaceTask/taskSaved/<str:username>', views.taskSaved, name='taskSaved'),
    path('workspaceTask/taskDelete/<int:title_id>',views.taskDelete, name='taskDelete'),
    path('workspaceTask/taskEdit/<int:title_id>',views.taskEdit, name='taskEdit'),
]