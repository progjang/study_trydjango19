from django.db import models
from django.core.urlresolvers import reverse
from datetime import timezone, timedelta, datetime
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

def upload_location(instance, filename):
    tz = timezone(timedelta(hours=9)) # 9_timezone
    dt = datetime.now(timezone.utc).astimezone(tz)
    timestamp_month = dt.strftime("%Y-%m")
    filebase,extension = filename.split(".")
    filename = filebase + "_" + str(dt) + "." + extension
    return "{}/{}".format(timestamp_month, filename)

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(
        upload_to = upload_location,
        null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"slug":self.slug})

    class Meta:
        ordering = ["-updated_at"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    # "Thi is a new post" -> "This-is-a-new-post"   
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "{}-{}".format(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
     
pre_save.connect(pre_save_post_receiver, sender=Post)