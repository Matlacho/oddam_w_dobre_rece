# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'HOST': 'localhost',
        'PASSWORD': 'mate2391',
        'USER': 'postgres',
        'PORT': 5432
    }
}