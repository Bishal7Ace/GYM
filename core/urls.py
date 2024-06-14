from django.urls import path
from core import views

urlpatterns = [
    path('core/profile/', views.ProfileDetail.as_view(), name='profile-detail'),
    path('core/exercises/', views.ExerciseListCreate.as_view(), name='exercise-list-create'),
    path('core/workouts/', views.WorkoutListCreate.as_view(), name='workout-list-create'),
    path('core/workouts/<int:workout_id>/exercises/', views.WorkoutExerciseList.as_view(), name='workout-exercise-list'),
    path('core/workouts/<int:workout_id>/exercises/<int:workout_exercise_id>/details/',
         views.WorkoutExerciseDetailList.as_view(), name='workout-exercise-detail-list'),
]
