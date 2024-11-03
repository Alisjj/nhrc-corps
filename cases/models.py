import uuid
from django.db import models
from django.utils import timezone

class Case(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    fullname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=20)
    address = models.TextField()
    sex = models.CharField(max_length=10, choices=SEX)
    email = models.EmailField()
    occupation = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    evidence = models.FileField(upload_to='evidence/', blank=True, null=True)
    case_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('Received', 'Case Received'), ('Review', 'Initial Review Completed'), ('Investigation', 'Investigation In Progress'), ('Resolution', 'Resolution')], default='Received')
    code = models.CharField(max_length=20, unique=True)

    # Date fields for each stage
    case_received_date = models.DateField(null=True, blank=True)
    initial_review_date = models.DateField(null=True, blank=True)
    investigation_start_date = models.DateField(null=True, blank=True)
    resolution_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.fullname} ({self.phonenumber})"
    

    def save(self, *args, **kwargs):
        # Automatically set the date fields based on status
        if self.status == 'Received' and not self.case_received_date:
            self.case_received_date = timezone.now()
        elif self.status == 'Review' and not self.initial_review_date:
            self.initial_review_date = timezone.now()
        elif self.status == 'Investigation' and not self.investigation_start_date:
            self.investigation_start_date = timezone.now()
        elif self.status == 'Resolution' and not self.resolution_date:
            self.resolution_date = timezone.now()
        
        self.code = uuid.uuid4().hex[:8].upper() 
        super().save(*args, **kwargs)
