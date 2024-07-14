import uuid
from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.functions import RandomUUID
from django.utils import timezone
import uuid


# Create your models here.
class AccountUser(models.Model):
    account_user_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    account_user_related_user = models.CharField(max_length=255, null=False, editable=False)
    account_user_fullname = models.CharField(max_length=255, null=False, editable=False)
    account_user_student_number = models.CharField(max_length=20, null=False)
    account_user_created_by = models.CharField(max_length=255, null=False)
    account_user_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    account_user_updated_by = models.CharField(max_length=255, null=True)
    account_user_updated_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.account_user_related_user

    def __unicode__(self):
        return '%s' % self.account_user_related_user

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.account_user_id), escape(self.account_user_related_user),           
            escape(self.account_user_fullname), escape(self.account_user_student_number),            
            escape(self.account_user_created_by), escape(self.account_user_created_date),            
            escape(self.account_user_updated_by), escape(self.account_user_updated_date)
        )

    class Meta:
        ordering = ('account_user_related_user',)
        indexes = [models.Index(
            fields=[
                'account_user_id',
                'account_user_related_user',
            ]),
        ]

class Course(models.Model):
    course_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    course_name = models.CharField(max_length=255, null=False, editable=False)
    course_created_by = models.CharField(max_length=255, null=False)
    course_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    course_updated_by = models.CharField(max_length=255, null=True)
    course_updated_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.course_id
    def __unicode__(self):
        return '%s' % self.course_id

    @property
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.course_id), escape(self.course_student_number),            escape(self.course_created_by), escape(self.course_created_date),            escape(self.course_updated_by), escape(self.course_updated_date)
        )

    class Meta:
        ordering = ('course_id',)
        indexes = [models.Index(
            fields=[
                'course_id']), ]


class AttendingCourse(models.Model):
    attending_course_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    attending_courseid = models.ForeignKey("Course", on_delete=models.CASCADE)
    attending_account_profile_id = models.CharField(max_length=255, null=False, editable=False)
    attending_course_created_by = models.CharField(max_length=255, null=False)
    attending_course_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    attending_course_updated_by = models.CharField(max_length=255, null=True)
    attending_course_updated_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.attending_account_profile_id

    def __unicode__(self):
        return '%s' % self.attending_account_profile_id

    @property    
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.attending_course_id), escape(self.attending_courseid),            escape(self.attending_account_profile_id),            escape(self.attending_course_created_by), escape(self.attending_course_created_date),            escape(self.attending_course_updated_by), escape(self.attending_course_updated_date)
        )

    class Meta:
        ordering = ('attending_course_id',)
        indexes = [models.Index(
            fields=[
                'attending_course_id', 'attending_courseid']), ]
        
