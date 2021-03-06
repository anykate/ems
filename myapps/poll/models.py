from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey


# Create your models here.
class ObjectTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class Comment(models.Model):
    text = models.TextField(null=False, blank=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.text[:20]


class Tag(ObjectTracking):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class QuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="active")

    def all_objects(self):
        return super().get_queryset()

    def inactive(self):
        return self.all_objects().filter(status='inactive')


class Question(ObjectTracking):
    title = models.CharField(max_length=255)
    status = models.CharField(default='inactive', max_length=10)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    comments = GenericRelation(Comment, related_query_name="question")

    objects = QuestionManager()

    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()


class Choice(ObjectTracking):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()


class Answer(ObjectTracking):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    comments = GenericRelation(Comment, related_query_name="answer")

    def __str__(self):
        return self.user.first_name + '-' + self.choice.text
