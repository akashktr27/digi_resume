from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    subject = models.TextField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class ClientMetadata(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    region_name = models.CharField(max_length=100, null=True, blank=True)
    referrer = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp}"

class PostRequestMetadata(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    referrer = models.URLField(blank=True, null=True)
    post_data = models.TextField()  # Store POST data if needed
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp} (POST)"

from django.db import models

class ResumeViewMetadata(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    referrer = models.URLField(blank=True, null=True)
    view_name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    resume_region_name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f"{self.ip_address} - {self.view_name} - {self.timestamp}"
