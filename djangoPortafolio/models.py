from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    # A short, catchy tagline for the card
    tagline = models.CharField(max_length=200)
    # The image/GIF for the card's initial state
    thumbnail = models.ImageField(upload_to='project_thumbnails/')
    # The detailed case study, can use Markdown here
    case_study = models.TextField()
    github_link = models.URLField()
    live_demo_link = models.URLField(blank=True, null=True)
    # For clean URLs like /projects/chaotic-password-generator
    slug = models.SlugField(unique=True, max_length=100)
    # To order projects on the page
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title