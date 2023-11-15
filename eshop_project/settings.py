"""
Django setting's for eshop_project project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path
import locale
from django.conf.global_settings import SESSION_COOKIE_AGE
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
#  python-decople
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
	# 'adminlte3',
	# # Optional: Django admin theme (must be before django.contrib.admin)
	# 'adminlte3_theme',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# internal apps
	'product_module.apps.ProductModuleConfig',
	'home_module.apps.HomeModuleConfig',
	'contact_module.apps.ContactModuleConfig',
	'account_module.apps.AccountModuleConfig',
	'site_module.apps.SiteSettingModelConfig',
	'article_module.apps.ArticleModuleConfig',
	'polls',
	'user_panel_module.apps.UserPanelModuleConfig',
	'order_module.apps.OrderModuleConfig',
	'admin_panel',
	'zarinpal.apps.ZarinpalConfig',
	# external apps
	'django_render_partial',
	'sorl.thumbnail',
	'jalali_date',
	'widget_tweaks',
	'crispy_forms',
	'crispy_bootstrap4',
	'ckeditor',
	'django.contrib.postgres',
	'star_ratings',
	# time
	'django.contrib.humanize'
	# 'jsoneditor'
	# 'ckeditor_uploader',
	# 'django_webp',
	# 'webp_converter',
	# 'captcha',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'article_module.middleware.SaveIPAddress',
]

ROOT_URLCONF = 'eshop_project.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')]
		,
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django_webp.context_processors.webp',
				# 'webp_converter.context_processors.webp_support'
			],
		},
	},
]

WSGI_APPLICATION = 'eshop_project.wsgi.application'
MERCHANT = 'dc390599-5705-43d6-b5ad-14a1008971d9'
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
AUTH_USER_MODEL = 'account_module.User'
LOGIN_URL = 'account:login_page'
#
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}
# DATABASES = {
#     'default': {
#         'HOST': '127.0.0.1',
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '',
#         'USER': 'root',
#         'PASSWORD': '',
#         'PORT': '3306'
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fa-IR'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static-cdn')  # static-cdn

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

MEDIA_ALLOWED_EXTENSIONS = [
	'jpg', 'jpeg', 'png', 'gif', 'webp'
]
# c
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SESSION_COOKIE_AGE = 120  s
# EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
# EMAIL_USE_SSL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# default settings (optional)
JALALI_DATE_DEFAULTS = {
	'Strftime': {
		'date': '%y/%m/%d',
		'datetime': '%H:%M:%S _ %y/%m/%d',
	},
	'Static': {
		'js': [
			# loading datepicker
			'admin/js/django_jalali.min.js',
			# OR
			# 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
			# 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
			# 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
			# 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
			# 'admin/js/main.js',
		],
		'css': {
			'all': [
				'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
			]
		}
	},
}
SANDBOX = None

locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")

# crispy forms --------------------------------------------------------------------------------
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

# ckeditor -----------------------------------------------------------
# CKEDITOR_BASEPATH = "/static-cdn/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
	"default": {
		'toolbar': [["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
					['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
					 'JustifyRight', 'JustifyBlock'],
					["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"],
					['Undo', 'Redo'], ["Source"],
					["Maximize"]],
		# 'toolbar_Custom': [
		#     ['Bold', "Italic", "Underline"],
		#     ['NumberedList', "BulletedList"],
		#     ['Link', "Unlink"],
		#     ['RemoveFormat', "Source"]
		# ],
		'height': 100,
	},
	'full': {
		'toolbar': [["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
					['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
					 'JustifyRight', 'JustifyBlock'],
					["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"],
					['Undo', 'Redo'], ["Source"],
					["Maximize"]
					],
		'height': 150,
		'width': "auto"
	}
}

# star ratings ------------------------------------
STAR_RATINGS_STAR_HEIGHT = 16
# STAR_RATINGS_STAR_SPRITE = os.path.join(BASE_DIR, 'static/images/blog/star.png')
