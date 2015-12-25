import datetime
from hashlib import md5

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.timezone import utc

class BaseModel(models.Model):
    class Meta:
        abstract=True
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class SlugMixin(models.Model):
    class Meta:
        abstract=True

    slug = models.SlugField(max_length=255, unique=True)

    def create_slug(self, title):
        slug = slugify(title)[:100]
        if len(slug.strip()) == 0:
            slug = md5(str(datetime.datetime.now())).hexdigest()
        while self.__class__.objects.filter(slug=slug).exists():
            slug = "{random}-{slug}".format(
                    random=md5(str(datetime.datetime.now())).hexdigest()[:5],
                    slug=slug
                    )
        self.slug = slug

class Camp(BaseModel, SlugMixin):
    name = models.CharField(max_length=255)
    # description = models.TextField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    # TODO: Enable timezone support
    venue_address = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug: # Created:
            self.create_slug(self.name)
        super(Camp, self).save(*args, **kwargs)

    def clean(self):
        # TODO:
        # end datetime > start datetime
        pass

    def is_over(self):
        return datetime.datetime.now().replace(tzinfo=utc) > self.end

    def html_venue_address(self):
        if self.venue_address:
            return '<br />'.join(self.venue_address.split('\n'))
        return None

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

class Session(BaseModel, SlugMixin):
    title = models.CharField(max_length=100)
    description = models.TextField()
    speaker = models.ForeignKey(UserProfile, related_name="sessions")
    camp = models.ForeignKey(Camp, related_name="sessions")
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_slug(self.title)
        super(Session, self).save(*args, **kwargs)
