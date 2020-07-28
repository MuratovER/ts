from django.contrib import admin
from .models import Post, Skill, UserSkill, Profile, Difficulty

admin.site.register(Post)
admin.site.register(Skill)
admin.site.register(UserSkill)
admin.site.register(Profile)
admin.site.register(Difficulty)