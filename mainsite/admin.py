from django.contrib import admin
from .models import Post, Skill, UserSkill, Profile, Difficulty, Sphere_of_life, Achivement, UserAchivement, User_affirmation, Comment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'email',)
    search_fields = ('user', 'email')


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Skill)
admin.site.register(UserSkill)
admin.site.register(Difficulty)
admin.site.register(Sphere_of_life)
admin.site.register(User_affirmation)
admin.site.register(Achivement)
admin.site.register(UserAchivement)
