from django.db import models

# Create your models here.
# model for Post 
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)



#model Skills 
class Skill(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill_name = models.TextField()
    level = PositiveIntegerField(blank=True, null=True)


#model of userSKill
class UserSkill(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill_name = models.TextField(max_length=80)
    level = PositiveIntegerField(blank=True, null=True)