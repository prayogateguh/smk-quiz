from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=50)
    nim = models.CharField(max_length=20)
    # post_pic = models.ImageField(upload_to='img/', null=True, blank=True)
    kelas = models.CharField(max_length=20)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.nama_lengkap

    def get_absolute_url(self):
        return reverse('siswa:profile', args=[self.slug, ])

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = str(self.id)
            self.save()


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
