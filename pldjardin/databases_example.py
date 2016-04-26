# Utiliser ce modèle pour le fichier databases.py qui est import dans settings.py
# Ce fichier est versionné pour servir d'exemple de structure
# Contrairement à databases.py qui n'est pas versionné

# MySQL
def getDatabaseConfig():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pldjardin',
            'HOST': '',
            'PASSWORD': '',
            'PORT': '',
            'USER': 'root',
        }
    }
    return DATABASES

# PostgreSQL
def getDatabaseConfig():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'pldjardin',
            'HOST': '',
            'PASSWORD': '',
            'PORT': '5432',
            'USER': 'postgres',
        }
    }
    return DATABASES

# SqlLite3
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def getDatabaseConfig():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    return DATABASES