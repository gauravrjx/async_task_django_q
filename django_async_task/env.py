SECRET_KEY = 'django-insecure-7r6jdon5fhj*8kk*zy3izxr7p9%!+womm2ihb_9fsm_iys9yrw'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoasyncdb',
        'USER': 'postgres',
        'PASSWORD': 'root@123',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': 600,
    },
    
}