from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/playbooks/', views.list_playbooks, name='list_playbooks'),
    path('api/playbooks/create/', views.create_playbook, name='create_playbook'),
    path('api/playbooks/file/', views.get_file, name='get_file'),
    path('api/playbooks/save/', views.save_file, name='save_file'),
    path('api/playbooks/delete/', views.delete_playbook, name='delete_playbook'),
    path('api/queue/', views.get_queue, name='get_queue'),
    path('api/queue/add/', views.add_to_queue, name='add_to_queue'),
    path('api/queue/remove/', views.remove_from_queue, name='remove_from_queue'),
    path('api/run/stream/', views.stream_run, name='stream_run'),
    path('api/stats/', views.get_stats, name='get_stats'),
    path('api/stats/export/', views.export_stats_excel, name='export_stats_excel'),
    path('api/fs/create-file/', views.fs_create_file, name='fs_create_file'),
    path('api/fs/create-folder/', views.fs_create_folder, name='fs_create_folder'),
    path('api/fs/rename/', views.fs_rename, name='fs_rename'),
    path('api/fs/delete/', views.fs_delete, name='fs_delete'),
    path('api/schedule/', views.list_schedules, name='list_schedules'),
    path('api/schedule/add/', views.add_schedule, name='add_schedule'),
    path('api/schedule/remove/', views.remove_schedule, name='remove_schedule'),
    path("api/chat/", views.chat, name="chat")
]
