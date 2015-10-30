<img src="http://i65.tinypic.com/30d87xi.jpg" align="left" width="220px" height="220px"/>
<img align="left" width="0" height="192px" hspace="10"/>

> The <a href="http://pewedemo.zealab.com/">Proffesional Weekend</a> Official Code Base

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE.md) [![Pewe Version](https://img.shields.io/pypi/pyversions/Django.svg)](http://pewedemo.zealab.com/) [![Pewe Build Status](https://img.shields.io/badge/pewe--v1.0-90%25-orange.svg)](https://travis-ci.org/oh-my-fish/oh-my-fish) [![App Status](https://img.shields.io/pypi/status/Django.svg)](http://pewedemo.zealab.com/)

<div align="justify">
	Professional Weekend is a Python/Django web application with a video blog (vblog) and portal format, also with user authentication. I made this web app for fun only on my spare time, so don't expect too much ;)
</div>

<br><br>

<p align="center">
  <b>Official Website</b> &raquo;
  <a href="http://pewedemo.zealab.com/">PEWE</a>
</p>

SCREENSHOT
---------------
<div align="center">
	<img src="http://i68.tinypic.com/2hdazoh.jpg" align="center" style="border-radius: 3px;" />
</div>

TECHNOLOGY STACK
---------------

- Python 2.7.8
- MySQL 5.0.11
- Django 1.8.5
- Bootstrap 3.5.5

INSTALL
---------------

I assume you already setup your django development enviroment (pip, virtualenv, git, etc...). If not yet, then Google is your friend.

1 Create virtual enviroment :
```
virtualenv .
source bin/activate
```

2 Git clone the project inside created enviroment :
```
git clone https://github.com/alzearafat/pewe-web.git
```

3 Install all requirements :
```
pip install -r requirements.txt
```

4 Create migration
```
python manage.py makemigrations
python manage.py migrate
```

5 Run the local dev server
```
python manage.py runserver
```

TO-DO LIST
---------------

1. Add search engine
2. Add pagination
3. ...

CODE TREE
---------------

```
.
├── db.sqlite3
├── manage.py
├── media
│   └── images
│       └── 2015
│           └── 10
│               ├── 23
│               │   ├── office.jpg
│               │   └── office_YgqWP2Y.jpg
│               └── 24
│
├── proffesionalweekend
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── requirements.txt
├── static
│   ├── css
│   │   ├── animate.css
│   │   ├── bootstrap.min.css
│   │   ├── custom.css
│   │   ├── default.css
│   │   ├── eden.css
│   │   ├── font-awesome.min.css
│   │   ├── lightbox.css
│   │   └── please-wait.css
│   ├── fonts
│   │   ├── FontAwesome.otf
│   │   ├── fontawesome-webfont.eot
│   │   ├── fontawesome-webfont.svg
│   │   ├── fontawesome-webfont.ttf
│   │   ├── fontawesome-webfont.woff
│   │   └── fontawesome-webfont.woff2
│   ├── img
│   │   ├── bg_teaser.svg
│   │   ├── card.jpg
│   │   ├── close.png
│   │   ├── jogja-bg.png
│   │   ├── loading.gif
│   │   ├── next.png
│   │   ├── pattern-black.png
│   │   ├── pattern-white.png
│   │   ├── prev.png
│   │   ├── sirphone-orange.png
│   │   └── sirphone.png
│   └── js
│       ├── bootstrap.min.js
│       ├── jquery-1.11.3.min.js
│       ├── lightbox.min.js
│       └── please-wait.min.js
├── the_don
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20151024_1657.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── the_don
│   │       ├── about-detail.html
│   │       ├── about.html
│   │       ├── base-detail.html
│   │       └── base.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── vblog
    ├── admin.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_video_location.py
    │   ├── 0003_video_gallery_image_4.py
    │   ├── 0004_video_gmap_iframe.py
    │   ├── 0005_auto_20151025_1329.py
    │   └── __init__.py
    ├── models.py
    ├── templates
    │   ├── registration
    │   │   ├── activate.html
    │   │   ├── activation_complete.html
    │   │   ├── activation_email_subject.txt
    │   │   ├── activation_email.txt
    │   │   ├── base.html
    │   │   ├── login_error.html
    │   │   ├── login.html
    │   │   ├── logout.html
    │   │   ├── password_change_done.html
    │   │   ├── password_change_form.html
    │   │   ├── password_reset_complete.html
    │   │   ├── password_reset_confirm.html
    │   │   ├── password_reset_done.html
    │   │   ├── password_reset_email.html
    │   │   ├── password_reset_form.html
    │   │   ├── registration_complete.html
    │   │   └── registration_form.html
    │   └── vblog
    │       ├── base-archive.html
    │       ├── base.html
    │       ├── base-single.html
    │       ├── homepage.html
    │       ├── video-detail.html
    │       └── video-list.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

LICENSE
---------------

- <a href="https://opensource.org/licenses/MIT">MIT</a>

CHANGELOG
---------------

**Version 1.0**
- Initial launch

THANKS TO
---------------

الله سُبْحَانَهُ وتَعَالَى