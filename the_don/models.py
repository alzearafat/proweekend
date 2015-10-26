from django.db import models
from ckeditor.fields import RichTextField

class Team(models.Model):
	name = models.CharField(max_length=200)
	card_image_header = models.ImageField(upload_to='images/%Y/%m/%d', help_text='Ini gambar cover card profile nya. Kecil aja gambar nya.', blank=True)
	profile_pic = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
	quote = models.CharField(max_length=255, help_text='Singkat aja!', blank=True)
	facebook = models.URLField(max_length=255, help_text='(Opsional)', blank=True)
	instagram = models.URLField(max_length=255, help_text='(Opsional)', blank=True)
	twitter = models.URLField(max_length=255, help_text='(Opsional)', blank=True)
	googleplus = models.URLField(max_length=255, help_text='(Opsional)', blank=True)
	about = RichTextField(config_name='default')
	pubdate = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name