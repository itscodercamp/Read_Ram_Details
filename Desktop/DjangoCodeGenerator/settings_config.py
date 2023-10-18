# settings_config.py

def configure_installed_apps(settings_file_path):
    try:
        with open(settings_file_path, 'r') as f:
            content = f.read()

        # Check if 'jazzmin' is already in INSTALLED_APPS
        if "'jazzmin'" not in content:
            new_content = content.replace(
                "'django.contrib.admin',",
                "'jazzmin',\n    'django.contrib.admin',"
            )

            # Write the updated content back to settings.py
            with open(settings_file_path, 'w') as f:
                f.write(new_content)

            print("Added 'jazzmin' to INSTALLED_APPS successfully.")
        else:
            print("'jazzmin' is already in INSTALLED_APPS.")

    except Exception as e:
        print(f"Error configuring INSTALLED_APPS setting: {e}")

def configure_templates(settings_file_path):
    try:
        with open(settings_file_path, 'r') as f:
            content = f.read()

        # Check if BASE_DIR is already added to the templates setting
        if "BASE_DIR / 'templates'" not in content:
            new_content = content.replace(
                'TEMPLATES = [',
                '\nTEMPLATES = ['
            )
            new_content = new_content.replace(
                "'DIRS': [],",
                f"'DIRS': [BASE_DIR / 'templates'],"
            )

            # Write the updated content back to settings.py
            with open(settings_file_path, 'w') as f:
                f.write(new_content)

            print("Added BASE_DIR to the templates setting successfully.")
        else:
            print("BASE_DIR is already in the templates setting.")

    except Exception as e:
        print(f"Error configuring templates setting: {e}")


def configure_allowed_hosts(settings_file_path):
    try:
        with open(settings_file_path, 'r') as f:
            content = f.read()

        # Check if '*' is already in ALLOWED_HOSTS
        if "'*'" not in content:
            new_content = content.replace(
                "ALLOWED_HOSTS = []",
                "ALLOWED_HOSTS = ['*']"
            )

            # Write the updated content back to settings.py
            with open(settings_file_path, 'w') as f:
                f.write(new_content)

            print("Allowed all hosts by adding '*' to ALLOWED_HOSTS successfully.")
        else:
            print("'*' is already in ALLOWED_HOSTS.")

    except Exception as e:
        print(f"Error configuring ALLOWED_HOSTS setting: {e}")

def EmailSmtp(settings_file_path):
    try:
        smtp_content = """
# Smtp Email configuration setup here
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'Your-Smtp-Email-Here'
EMAIL_HOST_PASSWORD = 'Your-Smtp-Password-Here'
"""
        with open(settings_file_path, 'a') as f:
            f.write(smtp_content)    
        print(f'SMTP Email config Added Successfully in settings ')
    except Exception as e:
        print(f'error while adding smtp : {e}')