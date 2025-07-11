from django.urls import path
from . import views # Import views from the current app

urlpatterns = [
    # The root URL of the site (e.g., yoursite.com/)
    path('', views.homepage, name='homepage'),

    # The URL for a specific project's case study page
    # e.g., yoursite.com/projects/chaotic-password-generator/
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),

    # You could add an about page URL here too
    # path('about/', views.about_page, name='about'),
]