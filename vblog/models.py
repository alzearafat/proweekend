from django.db import models
from ckeditor.fields import RichTextField

class Video(models.Model):
	title = models.CharField(max_length=200)
	featured_image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
	iframe_src = models.CharField(max_length=255)
	vimeo_page = models.URLField(max_length=255, blank=True)
	location = models.CharField(max_length=255, blank=True)
	HTM = models.CharField(max_length=100, blank=True)
	content = RichTextField(config_name='default')
	gmap_iframe = models.TextField(blank=True)
	gallery_image_1 = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
	gallery_image_2 = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
	gallery_image_3 = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
	gallery_image_4 = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
	pubdate = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title