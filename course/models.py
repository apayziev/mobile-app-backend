from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from helpers.models import BaseModel

# Create your models here.
COURSE_LEVEL = (
    ("beginner", "Beginner"),
    ("intermediate", "Intermediate"),
    ("advanced", "Advanced"),
)

COURSE_STATUS = (
    ('free', 'Free'),
    ('premium', 'Premium'),
)

COURSE_DURATION = (
    ('0-1 Hour', '0-1 Hour'),
    ('1-3 Hour', '1-3 Hour'),
    ('3+ Hour', '3+ Hour'),
)

class CourseAuthor(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course/author')
    is_top = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(BaseModel):
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    image = models.ImageField(upload_to="category_images", null=True, blank=True)
    is_popular = models.BooleanField(default=False)
    is_most_viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Course(BaseModel):
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    image = models.ImageField(upload_to="course_images", null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    author = models.ForeignKey(CourseAuthor, on_delete=models.CASCADE, related_name="courses")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    enrolment_count = models.IntegerField(default=0)
    level = models.CharField(max_length=256, choices=COURSE_LEVEL, default="beginner")
    status = models.CharField(max_length=256, choices=COURSE_STATUS, default="free")
    duration = models.CharField(max_length=256, choices=COURSE_DURATION, default="0-1 Hour")
    is_best_seller = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.title