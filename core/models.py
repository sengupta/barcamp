from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    class Meta:
        abstract=True
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Camp(BaseModel):
    name = models.CharField(max_length=255)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    venue_address = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255)

    def __unicode__(self):
        return self.name

    def create_slug(self):
        # TODO
        pass

    def save(self, *args, **kwargs):
        # TODO: generate slug
        super(Camp, self).save(*args, **kwargs)

class UserProfile(BaseModel):
    user = models.OneToOneField(User)
    name = models.CharField(
            null=False,
            blank=False,
            max_length=30
            )

    def __unicode__(self):
        return self.name

class Session(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    speaker = models.ManyToManyField(UserProfile, related_name="speakers")
    camp = models.ForeignKey(Camp)
    enabled = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255)

    def __unicode__(self):
        return self.title

    def create_slug(self):
        # TODO
        pass

    def save(self, *args, **kwargs):
        # TODO: generate slug
        super(Camp, self).save(*args, **kwargs)
