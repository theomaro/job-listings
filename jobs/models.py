from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.FileField(null=True, blank=True)
    overview = RichTextField()
    description = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "companies"
        ordering = ["name"]

    def __str__(self):
        return self.name


class JobCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = RichTextField(blank=True, null=True)
    featured_job = models.ForeignKey(
        "Job", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Job(models.Model):
    EMPLOYMENT_TYPE_FULL = "full-time"
    EMPLOYMENT_TYPE_PART = "part-time"
    EMPLOYMENT_TYPE_INTERN = "internship"
    EMPLOYMENT_TYPE_VOLUNTEER = "volunteer"
    EMPLOYMENT_TYPE_FREELANCE = "freelance"
    EMPLOYMENT_TYPE_CONTRACT = "contract"
    EMPLOYMENT_TYPE_TEMPO = "temporary"

    EMPLOYMENT_TYPE_CHOICES = [
        (EMPLOYMENT_TYPE_FULL, "Full-time"),
        (EMPLOYMENT_TYPE_PART, "Part-time"),
        (EMPLOYMENT_TYPE_INTERN, "Internship"),
        (EMPLOYMENT_TYPE_VOLUNTEER, "Volunteer"),
        (EMPLOYMENT_TYPE_FREELANCE, "Freelance"),
        (EMPLOYMENT_TYPE_CONTRACT, "Contract"),
        (EMPLOYMENT_TYPE_TEMPO, "Temporary"),
    ]

    JOB_TYPE_REMOTE = "remote"
    JOB_TYPE_ONSITE = "on-site"
    JOB_TYPE_HYBRID = "hybrid"

    JOB_TYPE_CHOICES = [
        (JOB_TYPE_REMOTE, "Remote"),
        (JOB_TYPE_ONSITE, "On-site"),
        (JOB_TYPE_HYBRID, "Hybrid"),
    ]

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    categories = models.ManyToManyField(JobCategory)
    title = models.CharField(max_length=255)
    overview = RichTextField()
    description = RichTextField()
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employment_type = models.CharField(
        max_length=255, choices=EMPLOYMENT_TYPE_CHOICES, default=EMPLOYMENT_TYPE_FULL
    )
    job_type = models.CharField(
        max_length=255, choices=JOB_TYPE_CHOICES, default=JOB_TYPE_ONSITE
    )
    is_urgent = models.BooleanField(default=False)
    submission_deadline = models.DateTimeField()
    posted_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        unique_together = ["title", "company"]

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    cover_letter = RichTextField()
    resume = models.FileField(upload_to="downloads/", null=True, blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["job", "user"]

    def __str__(self):
        return f"{self.user} - {self.job}"
