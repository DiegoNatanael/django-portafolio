from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Project
import markdown2
from django.utils.safestring import mark_safe
import requests

def homepage(request):
    if request.method == 'POST':
        # Verify reCAPTCHA v3
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success'] and result.get('score', 0) > 0.5:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            # Send email
            send_mail(
                f'Portfolio Contact from {name}',
                f'From: {name} <{email}>\n\nMessage:\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                ['natanael.gonzalez.dev@gmail.com'],
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('homepage')
    
    featured_projects = Project.objects.all().order_by('display_order')
    context = {
        'projects': featured_projects,
        'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY
    }
    return render(request, 'index.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    # 1. Convert the Markdown from the project's case_study field into HTML.
    converted_html = markdown2.markdown(project.case_study)
    
    # 2. Build the context dictionary.
    # We pass the original project object AND our new HTML variable.
    context = {
        'project': project,
        'case_study_html': mark_safe(converted_html) # Mark as safe here
    }
    
    return render(request, 'project_detail.html', context)