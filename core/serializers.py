from rest_framework import serializers
from core.models import *

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    created = serializers.DateTimeField(source='user.created', read_only=True)
    weight = serializers.FloatField(source='get_weight', read_only=True)
    
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email','weight', 'weight_system', 'created']

    def create(self, validated_data):
        request_user = self.context['request'].user
        try:
            instance = Profile.objects.get(user=request_user)
        except Profile.DoesNotExist:
            raise serializers.ValidationError("Profile does not exist for this user.")
        
        instance.weight_system = validated_data.get("weight_system", instance.weight_system)
        instance.save()
        return instance

    def get_weight(self, obj):
        # Assuming 'obj' is an instance of Profile
        return obj.weight


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

    def create(self, validated_data):
        request_user = self.context['request'].user
        instance = Exercise.objects.create(user=request_user, **validated_data)
        return instance

    def validate(self, attrs):
        #  Ensure body_part and equipment are valid choices
        if attrs['body_part'] not in dict(Exercise.BODY_PARTS).keys():
            raise serializers.ValidationError("Invalid body part choice.")
        if attrs['equipment'] not in dict(Exercise.EQUIPMENT).keys():
            raise serializers.ValidationError("Invalid equipment choice.")
        return attrs

class WorkoutExerciseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExerciseDetail
        fields = ['id', 'sets', 'reps', 'weight']


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='exercise.name', read_only=True)
    workout_exercise_details = WorkoutExerciseDetailSerializer(many=True, required=False)

    class Meta:
        model = WorkoutExercise
        fields = ['id', 'exercise', 'name', 'workout_exercise_details']
 
from rest_framework import serializers

class WorkoutSerializer(serializers.ModelSerializer):
    workout_exercises = WorkoutExerciseSerializer(many=True, required=False)

    class Meta:
        model = Workout
        fields = ['id', 'status', 'created', 'modified', 'workout_exercises']

    def create(self, validated_data):
        request_user = self.context['request'].user
        status = validated_data.get('status', 'default').strip()[:8]  # Ensure status value is within 8 characters
        instance = Workout.objects.create(user=request_user, status=status)

        workout_exercises = validated_data.pop('workout_exercises', [])
        for data in workout_exercises:
            exercise = data.get('exercise')
            workout_exercise = WorkoutExercise.objects.create(workout=instance, exercise=exercise)

            workout_exercise_details = data.get('workout_exercise_details', [])
            for exercise_details in workout_exercise_details:
                WorkoutExerciseDetail.objects.create(workout_exercise=workout_exercise, **exercise_details)

        return instance

       
# class WorkoutSerializer(serializers.ModelSerializer):
#     workout_exercises = WorkoutExerciseSerializer(many=True, required=False)

#     class Meta:
#         model = Workout
#         fields = ['id', 'status', 'created', 'modified', 'workout_exercises']

#     def create(self, validated_data):
#         request_user = self.context['request'].user
#         instance = Workout.objects.create(user=request_user, status=validated_data.pop('status'))

#         if 'workout_exercises' in validated_data:
#             for data in validated_data.pop('workout_exercises'):
#                 exercise = data.get('exercise')
#                 workout_exercise = WorkoutExercise.objects.create(workout=instance, exercise=exercise)

#                 if 'workout_exercise_details' in data:
#                     for exercise_details in data.get('workout_exercise_details'):
#                         WorkoutExerciseDetail.objects.create(workout_exercise=workout_exercise, **exercise_details)

#         return instance
