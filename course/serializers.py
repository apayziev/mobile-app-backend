from rest_framework import serializers
from course.models import Course,Category,CourseAuthor
from common.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username')


class CourseAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAuthor
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = CourseAuthorSerializer()
    class Meta:
        model = Course
        fields = '__all__'
