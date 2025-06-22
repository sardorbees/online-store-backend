from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-#o$sxch!@l_6#g3h1s4wq3i)v2ss!f)ac!_nb5)s1-wep=ljot'
DEBUG = True
ALLOWED_HOSTS = [
    '*'
]
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os


class FrontendAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(
                "index.html not found, build your React app first", status=501,
            )

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'base',
    'category',
    'category_title',
    'category_title_text',
    'company',
    'contact',
    'language',
    'location',
    'myblogyourapp',
    'question_and_answer',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'corsheaders',
    'shop',
    'user',
    'logo',
    'slug_category',
    'video',
    'comment',
    'rest_framework_simplejwt',
    'locations',
    'jet',
    'card',
    'calendars'
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'rizotoha78@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'rizotoha78@gmail.com'       # 👈 замените
EMAIL_HOST_PASSWORD = 'rt2611931rt'     # 👈 используйте App Password (не обычный пароль!)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


AUTH_USER_MODEL = 'user.CustomUser'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
]

ROOT_URLCONF = 'my_cleaning.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # or [] if not using custom templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for admin sidebar
                'django.contrib.auth.context_processors.auth',  # Required for admin
                'django.contrib.messages.context_processors.messages',  # Required for admin
            ],
        },
    },
]

WSGI_APPLICATION = 'my_cleaning.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/


LANGUAGE_CODE = "ru-uz"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True
LOCALE_PATH = [BASE_DIR / "locale"]



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
                    'code', 'subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|', 'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable', ],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side', '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                               'tableProperties', 'tableCellProperties'],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'}
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "DEFAULT_THROTTLE_RATES": {
    "anon": "5/day",
    "user": "5/day"
    },
}

SESSION_EXPIRE_SECONDS = 3600  # 1 hour
SESSION_COOKIE_AGE = 3600  # 1 hour
SESSION_TIMEOUT_REDIRECT = "/"
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_SECONDS = 604800

from datetime import timedelta
AXES_FAILURE_LIMIT = 5
AXES_RESET_ON_SUCCESS = True
AXES_COOLOFF_TIME = timedelta(seconds=10)


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': True,
}


CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "https://online-store-backend-1mjy.onrender.com",
]
CORS_ALLOW_CREDENTIALS = True

CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_SAMESITE = "Lax"  
CSRF_COOKIE_SECURE = True 

CSRF_TRUSTED_ORIGINS = ["https://tash-cleaning-admin-one.vercel.app", "https://online-store-backend-1mjy.onrender.com"]

CSRF_COOKIE_HTTPONLY = False

CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'x-csrftoken',
    'x-requested-with',
]


CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

STATIC_URL = '/static/'

import os
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


JAZZMIN_SETTINGS = {
    "site_title": "Krafto-Agency",
    "site_header": "Krafto-Agency",
    "site_brand": "Krafto-Agency",
    "site_icon": "../media/assets/img/aaa.png",
    "copyright": "Krafto-Agency",
    
    "site_logo": "../media/assets/img/aaa.png",
    "language_chooser": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "welcome_sign": "Xush Kelibsiz Krafto-Agency",
    
    "copyright": "tash-cleaning-admin",
    "user_avatar": "../media/assets/img/1111.jpg",
    "dashboard": [
        {"type": "link", "title": "Documentation", "url": "http://127.0.0.1:8000/swagger/"},
    ],
    "topmenu_links": [
        {"name": "Xush Kelibsiz KRAFTO-AGENCY Admin", "url": "home", "permissions": ["auth.view_user"]},
        {"name": "krafot-agency.uz", "url": "https://tash-cleaning-admin.vercel.app/", "permissions": ["auth.view_user"]},
        {"name": "Локация-места", "url": "http://127.0.0.1:8000/admin/locations/location/", "permissions": ["auth.view_user"]},
        {"name": "Коментария", "url": "http://127.0.0.1:8000/admin/comment/comment/", "permissions": ["auth.view_user"]},
        {"name": "Web-sayt malumotlar", "title": "Swagger", "url": "http://127.0.0.1:8000/admin/shop/product/"},
        {"name": "Logo xizmati", "title": "Swagger", "url": "http://127.0.0.1:8000/admin/logo/category/"},
        {"name": "Banner xizmati", "title": "Swagger", "url": "http://127.0.0.1:8000/admin/base/mainpagecard/add/"},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True, "icon": "fa-solid fa-user"},
        {"name": "Помощь", "url": "https://t.me/ali_candaan", "new_window": True, "icon": "fa-solid fa-headset"},
        {"name": "Пользователь", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True, "icon": "fa-solid fa-user"},
        {"model": "auth.user"}
    ],
    "custom_links": {
        "your_app_name": [{
            "name": "Сбросить кэш",
            "url": "reset-cache-url",
            "icon": "fas fa-broom",
            "permissions": ["your_app_name.clear_cache"]
        }]
    },
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fa-solid fa-headset",
        "auth.user": "fa-solid fa-headset",
        "auth.Group": "fas fa-users",
        "your_app.ModelName": "fa-solid fa-headset",
    },
    "default_icon_parents": "fa-solid fa-headset",
    "default_icon_children": "fa-solid fa-solar-panel",

    "related_modal_active": True,
    "custom_js": True,

    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "your_app_name"],

    "show_ui_builder": True,
    "show_sidebar": True,

    "changeform_format": "collapsible",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books"],
"order_with_respect_to": ["auth", "books", "books.author", "books.book"],

"order_with_respect_to": ["auth"],

"order_with_respect_to": ["books.author", "books.book"],


"order_with_respect_to": ["books.author", "Make Messages"],


"order_with_respect_to": [],


"order_with_respect_to": ["doesnt_exist"],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": True,
    "brand_small_text": True,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "sticky_actions": True,
    "actions_sticky_top": True,
    "theme": "lux",
    'whitefooter': True,
    'hide_app': True,
    'hide_title': True,
    'show_logout': True,
    'show_user_avatar': True,
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "custom_links": {
        "books": [{
            # Any Name you like
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }],
        # Add/Or a new group (name must not conflict with an installed app)
        "custom_group": [{
            "name": "Custom Link",
            "url": "custom_link",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },
}

from datetime import timedelta


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=100),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'AUTH_HEADER_TYPES': ('Bearer',),
    "ROTATE_REFRESH_TOKENS": True,
    "SIGNING_KEY": os.environ.get("SIGNING_KEY"),
    "ALGORITHM": "HS512",
    "VERIFYING_KEY": None,
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": (
        "rest_framework_simplejwt.tokens.AccessToken",
    ),
    "TOKEN_TYPE_CLAIM": "token_type",
}