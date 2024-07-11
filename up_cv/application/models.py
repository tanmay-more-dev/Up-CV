from django.db import models
from accounts.models import User


class PersonalInformation(models.Model):
    """
    Model to store personal information of a user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    profile_picture_url = models.URLField(blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"
        db_table = "personal_information"
        ordering = ["-id"]  # Newest records first based on creation date


class Education(models.Model):
    """
    Model to store education details of a user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} at {self.institution}"

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        db_table = "education"
        ordering = ["-start_date"]  # Newest education first


class WorkExperience(models.Model):
    """
    Model to store work experience details of a user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.employer}"

    class Meta:
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experience"
        db_table = "work_experience"
        ordering = ["-start_date"]  # Newest work experience first


class Skill(models.Model):
    """
    Model to store skills of a user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        db_table = "skill"
        ordering = ["skill_name"]  # Alphabetical order by skill name


class Certification(models.Model):
    """
    Model to store certifications of a user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=255)
    certifying_authority = models.CharField(max_length=255)
    date_received = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.certification_name

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        db_table = "certification"
        ordering = ["-date_received"]  # Newest certifications first


class Project(models.Model):
    """
    Model to store projects of a user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    project_url = models.URLField(blank=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        db_table = "project"
        ordering = ["-start_date"]  # Newest projects first
