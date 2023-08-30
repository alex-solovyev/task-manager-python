from rest_framework import serializers
from .models import Tag, Task, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone",
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")


class TaskSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    assignee = UserSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "author",
            "assignee",
            "deadline_on",
            "priority",
            "state",
            "tags",
            "created_at",
            "updated_at",
        )
