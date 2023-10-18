# setting_setup.py

def configure_project_settings(project_name, app_name):
    settings_file_path = f'{project_name}/settings.py'
    with open(settings_file_path, 'a') as settings_file:
        settings_file.write("\n")

        settings_file.write("import os\n")

        # Add MEDIA_ROOT and MEDIA_URL
        settings_file.write("MEDIA_ROOT = os.path.join(BASE_DIR, 'media')\n")
        settings_file.write("MEDIA_URL = '/media/'\n")

        # Add STATIC_URL and STATICFILES_DIRS
        settings_file.write("STATIC_URL = '/static/'\n")
        settings_file.write("STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]\n")

# add include statement for app urls in project urls
    with open(f"{project_name}/settings.py", "r") as f:
        content = f.read()
    content = content.replace(
        
        "'DIRS': [],",
        "'DIRS': [BASE_DIR / 'templates'],"
    )
    with open(f"{project_name}/settings.py", "w") as f:
        f.write(content)

    with open(f"{project_name}/settings.py", "r") as f:
        content = f.read()
    content = content.replace(
        "    'django.contrib.staticfiles',",
        f"    'django.contrib.staticfiles',\n    '{app_name}',"
    )
    with open(f"{project_name}/settings.py", "w") as f:
        f.write(content)
    return app_name

