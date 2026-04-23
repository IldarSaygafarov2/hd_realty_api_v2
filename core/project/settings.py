from pathlib import Path

import environs

env = environs.Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.constance",
    #
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # internal
    "core.apps.main.apps.MainConfig",
    "core.apps.categories.apps.CategoriesConfig",
    "core.apps.districts.apps.DistrictsConfig",
    "core.apps.advertisements.apps.AdvertisementsConfig",
    # external
    "constance",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB"),
        "HOST": env.str("POSTGRES_HOST"),
        "PORT": env.int("POSTGRES_PORT"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "USER": env.str("POSTGRES_USER"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CONSTANCE
CONSTANCE_BACKEND = "constance.backends.redisd.RedisBackend"

CONSTANCE_CONFIG = {
    "THE_ANSWER": (
        42,
        "Answer to the Ultimate Question of Life, " "The Universe, and Everything",
    ),
    "CURRENCY_RATE": (1.0, "Тут хранится курс доллара"),
}

CONSTANCE_REDIS_CONNECTION = {
    "host": env.str("CELERY_HOST"),
    "port": env.int("CELERY_PORT"),
    "db": 0,
}
CONSTANCE_REDIS_CACHE_TIMEOUT = 60


# CELERY
CELERY_TIMEZONE = "Asia/Tashkent"
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env.str("CELERY_RESULT_BACKEND")

CURRENCY_RATE_API = env.str("CURRENCY_RATE_API")


DISTRICTS_LIST = [
    "Мирабадский",
    "Мирзо-Улугбекский",
    "Алмазарский",
    "Бектемирский",
    "Сергелийский",
    "Чиланзарский",
    "Шайхантаурский",
    "Юнусабадский",
    "Яккасарайский",
    "Яшнабадский",
    "Учтепинский",
]

RENOVATION_TYPES = [
    "Черновая",
    "Предчистовая",
    "Чистовая",
    "Косметический",
    "Капитальный",
    "Дизайнерский",
]

CATEGORIES_LIST = [
    "Квартира",
    "Коттедж",
    "Участок",
    "Дом",
    "Для бизнеса",
    "Новостройка",
]

PROPERTY_TYPES_LIST = ["Новостройки", "Вторичный фонд"]
