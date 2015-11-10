from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.conf import settings
import datetime

class Post(models.Model):
	author = models.ForeignKey(User, related_name="user_posts", null=True, blank=True)
	title = models.CharField(max_length=200)
	featured_image = models.ImageField(upload_to='images/%Y/%m/%d', help_text='Ini gambar cover card profile nya. Kecil aja gambar nya.', blank=True)
	location = models.CharField(max_length=200)
	content = RichTextField(config_name='default')
	gallery_image_1 = models.ImageField(upload_to='images/%Y/%m/%d', help_text='Dimensi gambar maksimal 750x750p, dan minimal 350x350p! (Opsional)', blank=True)
	gallery_image_2 = models.ImageField(upload_to='images/%Y/%m/%d', help_text='Dimensi gambar maksimal 750x750p, dan minimal 350x350p! (Opsional)', blank=True)
	gallery_image_3 = models.ImageField(upload_to='images/%Y/%m/%d', help_text='Dimensi gambar maksimal 750x750p, dan minimal 350x350p! (Opsional)', blank=True)
	gallery_image_4 = models.ImageField(upload_to='images/%Y/%m/%d', help_text='Dimensi gambar maksimal 750x750p, dan minimal 350x350p! (Opsional)', blank=True)
	tanggal_publish = models.DateField(default=datetime.datetime.now, null=True, blank=True)

	def __str__(self):
		return str(self.title)