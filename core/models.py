import datetime
from hashlib import md5

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class BaseModel(models.Model):
    class Meta:
        abstract=True
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Camp(BaseModel):
    name = models.CharField(max_length=255)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    # TODO: Enable timezone support
    venue_address = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    def create_slug(self):
        # TODO
        pass

    def save(self, *args, **kwargs):
        # TODO: generate slug
        super(Camp, self).save(*args, **kwargs)

    def clean(self):
        # TODO:
        # end datetime > start datetime
        pass

class UserProfileManager(models.Manager):
    def exists(self, email):
        return User.objects.filter(email__iexact=email).exists()

class UserProfile(BaseModel):
    class Meta:
        app_label = 'core'

    objects = models.Manager()
    profiles = UserProfileManager()

    user = models.OneToOneField(User, related_name="profile")
    name = models.CharField(null=False, blank=False, max_length=30)

    def __unicode__(self):
        return self.name

class Session(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    speaker = models.ForeignKey(UserProfile, related_name="sessions")
    camp = models.ForeignKey(Camp, related_name="sessions")
    enabled = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255)

    def __unicode__(self):
        return self.title

    def create_slug(self):
        slug = slugify(self.title)[:100]
        if len(slug.strip()) == 0:
            slug = md5(str(datetime.datetime.now())).hexdigest()
        while Session.objects.filter(slug=slug).exists():
            slug = "{random}-{slug}".format(
                    random=md5(str(datetime.datetime.now())).hexdigest()[:5],
                    slug=slug
                    )
        self.slug = slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_slug()
        super(Session, self).save(*args, **kwargs)
