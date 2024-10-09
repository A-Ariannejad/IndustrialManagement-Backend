from django.db import models
from Projects.models import Project
from django.core.validators import MaxValueValidator, MinValueValidator

class PieScale(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    pending_percentage = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(100), MinValueValidator(0)], default=0.00) 
    doing_percentage = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(100), MinValueValidator(0)], default=0.00) 
    finished_percentage = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(100), MinValueValidator(0)], default=0.00) 
    date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name