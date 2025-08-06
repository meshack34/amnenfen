

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('destinations/', views.all_destinations, name='all_destinations'),  # This is the fix
    path('destination_list', views.destination_list, name='destination_list'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('destination/<int:id>/', views.destination_detail, name='destination_detail'),
    path('accommodation_summary_view', views.accommodation_summary_view, name='accommodation_summary_view'),
    path('destination/add/', views.add_destination_view, name='add_destination'),
    path('register/', views.register_view, name='register'), 
    path('destination/<int:destination_id>/upload/', views.upload_images, name='upload_image'),
    
    path('destination/<int:destination_id>/upload/gallery/', views.upload_gallery_image, name='upload_gallery'),
    path('destination/<int:destination_id>/upload/room/', views.upload_room, name='upload_room'),
    path('destination/<int:destination_id>/upload/restaurant/', views.upload_restaurant, name='upload_restaurant'),

    path('destination/<int:id>/edit/', views.edit_destination, name='edit_destination'),
    path('destination/<int:id>/delete/', views.delete_destination, name='delete_destination'),
    
    
    path('destination/<int:destination_id>/upload-activity/', views.upload_activity, name='upload_activity'),
    path('destination/<int:destination_id>/upload-information/', views.upload_information, name='upload_information'),


    path('accommodation-summary/', views.accommodation_summary_view, name='accommodation_summary'),
    path('export-summary/excel/', views.export_summary_excel, name='export_summary_excel'),
    path('export-summary/pdf/', views.export_summary_pdf, name='export_summary_pdf'),
    path('explore/', views.public_dashboard_view, name='public_dashboard'),
]