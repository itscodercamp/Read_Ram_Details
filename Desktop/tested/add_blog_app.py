import os
import re
import sys
import shutil
import fileinput


def copy_blog_app_to_project(project_name):
    try:
        source_app_path = r"C:\Users\user\Desktop\newCGS\New_Setup_DCGS\tested\blog"  # Replace this with the actual path to the 'blog' app directory
        destination_app_path = os.path.join("blog")

        # Copy the 'blog' app folder to the project directory
        if not os.path.exists(destination_app_path):
            shutil.copytree(source_app_path, destination_app_path)
        else:
            print("'blog' app already exists in the project.")

        with open(f"{project_name}/urls.py", "r") as f:
            content = f.read()

        App_Urls_link_project = "urlpatterns = urlpatterns + [path('Blog/', include('blog.urls')),]"
        if App_Urls_link_project not in content:
            with open(f"{project_name}/urls.py", "a") as f:
                f.write(f"\n{App_Urls_link_project}\n")

    except Exception as e:
        print(f"An error occurred while copying the 'blog' app: {e}")

def link_blog_app_in_settings(project_name):
    try:
        settings_file_path = f'{project_name}/settings.py'
        with open(settings_file_path, 'r') as settings_file:
            content = settings_file.read()

        # Add 'blog' app to the 'INSTALLED_APPS' list
        if "'blog'," not in content:
            content = content.replace("'django.contrib.staticfiles',",
                                    "'django.contrib.staticfiles',\n    'blog',")

        with open(settings_file_path, 'w') as settings_file:
            settings_file.write(content)

    except IOError as e:
        print(f"Error occurred while linking 'blog' app in settings.py: {e}")

def main(project_name):
    try:
        # Ask if the user wants to add the 'blog' app
        add_blog_app = input("Do you want to add the 'blog' app to your project? (yes/no): ").lower()
        if add_blog_app == 'yes':
            copy_blog_app_to_project(project_name)
            link_blog_app_in_settings(project_name)
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python add_blog_app.py project_name")
        sys.exit(1)

    project_name = sys.argv[1]
    main(project_name)


