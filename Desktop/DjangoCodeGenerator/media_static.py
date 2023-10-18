import os

def configure_media_and_static(settings_file_path):
    try:
        with open(settings_file_path, 'r') as f:
            content = f.read()

        # Check if the media and static settings are already defined
        if 'MEDIA_URL' not in content:
            with open(settings_file_path, 'a') as f:
                f.write('\n')
                f.write('import os')
                f.write('\n')
                f.write("# Media files (uploads)\n")
                f.write("MEDIA_URL = '/media/'\n")
                f.write(f"MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')\n")

        if 'STATIC_URL' not in content:
            with open(settings_file_path, 'a') as f:
                f.write('\n')
                f.write("# Static files (CSS, JavaScript, etc.)\n")
                f.write("STATIC_URL = '/static/'\n")
                f.write(f"STATIC_ROOT = os.path.join(BASE_DIR, 'static/')\n")

        print("Media and static settings configured successfully.")
    except Exception as e:
        print(f"Error configuring media and static settings: {e}")
