from django.db import models
from users.models import CustomUser
# Create your models here.
class Team(models.Model):
    name= models.CharField(max_length=100)
    members= models.ManyToManyField(CustomUser, through= 'TeamMembership', related_name='teams')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class TeamMemberhip(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team= models.ForeignKey(Team, on_delete=models.CASCADE)
    role_in_team= models.CharField(max_length=50, choices=[
        ('Lead', 'lead'),
        ('Member', 'member'),
        ('Intern', 'intern')
    ])
    joined_at= models.DateTimeField(auto_now_add=True)
    is_active= models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'team')

    def __str__(self):
        return f"{self.user.email} in {self.team.name} as {self.role_in_team}"
