from django.db import models
from .tag import Tag
from .user import User


class Task(models.Model):
    class States(models.TextChoices):
        NEW_TASK = "new_task"
        IN_DEVELOPMENT = "in_development"
        IN_QA = "in_qa"
        IN_CODE_REVIEW = "in_code_review"
        READY_FOR_RELEASE = "ready_for_release"
        RELEASED = "released"
        ARCHIVED = "archived"

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        related_name="created_tasks",
        limit_choices_to={"role": User.Roles.MANAGER},
        on_delete=models.RESTRICT,
    )
    assignee = models.ForeignKey(
        User,
        related_name="assigned_tasks",
        limit_choices_to={"role": User.Roles.DEVELOPER},
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    description = models.TextField()
    deadline_on = models.DateField()
    priority = models.PositiveSmallIntegerField()
    state = models.CharField(
        max_length=20, default=States.NEW_TASK, choices=States.choices
    )
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
