from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('audio/', views.audio, name='audio'),
    # path('document/', views.document, name='document'),

    path('document_analysis/', views.document_analysis, name='document_analysis'),
    path('reg/', views.reg, name='reg'),
    path('api/document/', views.document_upload_view, name='upload-api'),
    path('chat_zone/', views.upload_file, name='upload'),
    path('api/upload', views.upload_audio, name='upload-api'),


    path('document_analysis_api/', views.document_analysis_api, name='document_analysis_api'),
    path('chat/', views.chat, name='chat'),
    path('ask_document/', views.ask_document, name='ask_document'),


    path('login/', views.login_view, name='login'),
    path('signup/7c5ba237769129ef7a4a7ff40292fb7a/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

]
