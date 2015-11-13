<img src="http://i65.tinypic.com/30d87xi.jpg" align="left" width="220px" height="220px"/>
<img align="left" width="0" height="192px" hspace="10"/>

> The <a href="http://pewedemo.zealab.com/">Proffesional Weekend v2.3</a> Official Code Base

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE.md) [![Pewe Version](https://img.shields.io/pypi/pyversions/Django.svg)](http://pewedemo.zealab.com/) [![Pewe Build Status](https://img.shields.io/badge/pewe--v2.4-90%25-orange.svg)](https://travis-ci.org/oh-my-fish/oh-my-fish) [![App Status](https://img.shields.io/pypi/status/Django.svg)](http://pewedemo.zealab.com/)

<div align="justify">
	Professional Weekend is a Python/Django web application with a video blog (vblog), multi-author, multi-blog and portal feature, also with user authentication. I made this web app for fun only on my spare time.
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

**1 Create virtual enviroment :**
```
virtualenv .
source bin/activate
```

**2 Git clone the project inside created enviroment :**
```
git clone https://github.com/alzearafat/pewe-web.git
```

**3 Install all requirements :**
```
pip install -r requirements.txt
```

**4 Create migration**
```
python manage.py makemigrations
python manage.py migrate
```

**5 Run the local dev server**
```
python manage.py runserver
```

Settings.py LOCATION
---------------

Template: https://github.com/alzearafat/pewe-web/wiki/Settings.py-Template


TO-DO LIST
---------------

1. Add search engine
2. Add pagination (DONE!)
3. Add Single Author Profile
4. ...

LICENSE
---------------

- <a href="https://opensource.org/licenses/MIT">MIT</a>

CHANGELOG
---------------

**Version 2.3**
- Add "Search" feature
- Minor styles tweak

**Version 2.2**
- Change Journey URL From PK to Slug!
- Add Single Journey Gallery
- Add Social Sharer
- Style Improvement

**Version 2.0**
- Add "Journey" feature!
- Add pagination

**Version 1.0**
- Initial launch

THANKS TO
---------------

الله سُبْحَانَهُ وتَعَالَى