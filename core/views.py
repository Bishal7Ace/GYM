from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.models import *
from core.serializers import *
from core.permissions import IsOwner

class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        return self.request.user.profile

class ExerciseListCreate(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class WorkoutListCreate(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class WorkoutExerciseList(generics.ListAPIView):
    serializer_class = WorkoutExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        workout_id = self.kwargs['workout_id']
        return WorkoutExercise.objects.filter(workout_id=workout_id)
    
class WorkoutExerciseDetailList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutExerciseDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'workout_exercise_id'

    def get_queryset(self):
        workout_exercise_id = self.kwargs['workout_exercise_id']
        return WorkoutExerciseDetail.objects.filter(workout_exercise_id=workout_exercise_id)
 