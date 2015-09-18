
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "51225549-8f54-4d2a-8ec2-a60f2991a48466442ca6-8ca5-42b0-bb49-cf613fbd84a92fe5e279-1480-40a4-8f17-9c8daa497596"
NEVERCACHE_KEY = "96b5115f-2a94-46f6-919b-2c6d00757b8c7dc4356a-a067-4ed6-9aa2-74d82cc5c03959e36041-5a7d-4c1a-88d1-ffb150b0e2ec"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# Domains for public site
ALLOWED_HOSTS = ["*"]

FABRIC = {
    "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
    "SSH_USER": "nv",  # VPS SSH username
    "HOSTS": ["123.57.148.131"],  # The IP address of your VPS
    "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
    "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
    "DB_PASS": "postgres",  # Live database password
    "ADMIN_PASS": "0409izyH",  # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}