from django.db import models

class Case(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Pending Review'),
        (3, 'Resolved'),
    )

    fullname = models.CharField(max_length=224)
    phonenumber = models.CharField(max_length=12)
    address = models.CharField(max_length=225)
    sex = models.CharField(max_length=1, choices=SEX)
    email = models.EmailField()
    occupation = models.CharField(max_length=128)
    state = models.CharField(max_length=64)
    evidence = models.FileField(upload_to="evidences", blank=True, null=True)
    case_type = models.CharField(max_length=128)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    code = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Case"
        verbose_name_plural = "Cases"

    def __str__(self):
        return f"{self.fullname} ({self.phonenumber})"
