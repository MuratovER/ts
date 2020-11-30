from django.contrib import admin
from .models import Post, Skill, UserSkill, Profile, Difficulty, Sphere_of_life, User_affirmation
from .models import Post, Skill, UserSkill, Profile, Difficulty, Sphere_of_life, Achivement, UserAchivement, User_affirmation


admin.site.register(Post)
admin.site.register(Skill)
admin.site.register(UserSkill)
admin.site.register(Profile)
admin.site.register(Difficulty)
admin.site.register(Sphere_of_life)
admin.site.register(User_affirmation)
admin.site.register(Achivement)
admin.site.register(UserAchivement)

