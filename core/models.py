from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    User = models. OneToOneField(User, on_delete=models. CASCADE, null=True, blank=True)
    name =models. CharField(max_length= 200, null= True)
    email= models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class UploadedForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"


class OCRDocument(models.Model):
    file = models.FileField(upload_to='uploads/')
    extracted_text = models.TextField()
    extracted_headings = models.JSONField(blank=True, null=True)
    structured_data = models.JSONField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document {self.id} - {self.file.name}"