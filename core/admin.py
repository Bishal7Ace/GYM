from django.contrib import admin
from core.models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'weight', 'weight_system')
    search_fields = ('user__username', 'user__email')  # Example search fields
    list_filter = ('weight_system',)  # Example filter options


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'body_part', 'name', 'equipment', 'user')
    list_filter = ('body_part', 'equipment')  # Example filter options
    search_fields = ('name', 'description')  # Example search fields


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created', 'modified')
    list_filter = ('status', 'created', 'modified')  # Example filter options
    date_hierarchy = 'created'  # Example date hierarchy


class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout', 'exercise')
    list_filter = ('workout', 'exercise')  # Example filter options
    search_fields = ('workout__user__username', 'exercise__name')  # Example search fields


class WorkoutExerciseDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout_exercise', 'sets', 'reps', 'weight')
    list_filter = ('workout_exercise__workout',)  # Example filter options
    search_fields = ('workout_exercise__exercise__name',)  # Example search fields


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutExercise, WorkoutExerciseAdmin)
admin.site.register(WorkoutExerciseDetail, WorkoutExerciseDetailAdmin)

# from django.contrib import admin

# from core.models import *


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'weight_system')


# class ExerciseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'body_part', 'name', 'equipment', 'description', 'user')


# class WorkoutAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'status', 'created', 'modified')


# class WorkoutExerciseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'workout', 'exercise')


# class WorkoutExerciseDetailAdmin(admin.ModelAdmin):
#     list_display = ('id', 'workout_exercise', 'sets', 'reps', 'weight')


# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Exercise, ExerciseAdmin)
# admin.site.register(Workout, WorkoutAdmin)
# admin.site.register(WorkoutExercise, WorkoutExerciseAdmin)
# admin.site.register(WorkoutExerciseDetail, WorkoutExerciseDetailAdmin)