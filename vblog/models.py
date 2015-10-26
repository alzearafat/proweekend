from django.db import models
from ckeditor.fields import RichTextField

class Video(models.Model):
	title = models.CharField(max_length=200)
	featured_image = models.ImageField(upload_to='images/%Y/%m/%d', help_text='<strong>Dimensi gambar maksimal 750x750p, dan minimal 350x350p!</strong>', blank=True)
	iframe_src = models.CharField(max_length=255, help_text='Cukup copy paste <strong>iframe src</strong> nya saja. Jangan semua embed code nya!')
	vimeo_page = models.URLField(max_length=255, help_text='URL ke video di vimeo nya (Opsional)', blank=True)
	location = models.CharField(max_length=255, help_text='Lokasi tempat jalan-jalan nya (Opsional)', blank=True)
	HTM = models.CharField(max_length=100, help_text='Harga Tiket Masuk, tempat jalan-jalan nya (Opsional)', blank=True)
	content = RichTextField(config_name='default')
	gmap_iframe = models.TextField(help_text='Copy paste embed code Google Maps nya disini (Opsional)', blank=True)
	gallery_image_1 = models.ImageField(upload_to='images/%Y/%m/%d', help_text='Dimensi gambar maksimal 750x750p, dan minimal 350x350p! (Opsional)', blank=True)
	gallery_image_2 = models.ImageField(upload_to='images/%Y/%m/%d', help_text='Dimensi gambar maksimal 750x750p, dan minimal 350x350p! (Opsional)', blank=True)
	gallery_image_3 = models.ImageField(upload_to='images/%Y/%m/%d', help_text='Dimensi gambar maksimal 750x750p, dan minimal 350x350p! (Opsional)', blank=True)
	gallery_image_4 = models.ImageField(upload_to='images/%Y/%m/%d', help_text='Dimensi gambar maksimal 750x750p, dan minimal 350x350p! (Opsional)', blank=True)
	pubdate = models.DateField(help_text='Publication Date', auto_now_add=True)

	def __str__(self):
		return self.title