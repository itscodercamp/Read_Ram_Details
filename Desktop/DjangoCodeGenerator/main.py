import os
import subprocess
import re
import sys
from colorama import Fore, Style

from media_static import configure_media_and_static
from link_project_to_app import link_app_to_settings
from url_utils import include_app_urls
from settings_config import configure_templates, configure_allowed_hosts, configure_installed_apps ,EmailSmtp
from add_folder_and_files import create_templates_and_static_folders
from view_config import configure_views
from directory_selector import select_directory
from registration import *  # Import the new module


def is_valid_name(name):
    return bool(re.match(r'^[A-Za-z][a-zA-Z0-9]*$', name))

def get_valid_project_name(selected_directory, project_name):
    while True:
        if not is_valid_name(project_name):
            print("Invalid project name. Project name must be in camelCase format.")
        elif os.path.exists(os.path.join(selected_directory, project_name)):
            print(f" {Fore.YELLOW}Project '{project_name}' already exists in the selected directory.{Style.RESET_ALL}")
        else:
            return project_name

        project_name = input(f" {Fore.CYAN}Enter a new project name (camelCase): {Style.RESET_ALL}")


def create_django_project(project_name, project_directory):
    try:
        if project_directory:
            os.chdir(project_directory)

        subprocess.run(['django-admin', 'startproject', project_name])
        print(f"{Fore.GREEN}Created Django project '{project_name}' successfully.{Style.RESET_ALL}")
    except Exception as e:
        print(f"Error creating Django project: {e}")

def create_django_app(project_name, app_name):
    try:
        project_directory = os.path.join(os.getcwd(), project_name)
        os.chdir(project_directory)

        subprocess.run(['python', 'manage.py', 'startapp', app_name])
        print(f"{Fore.GREEN}Created Django app '{app_name}' inside project '{project_name}' successfully.{Style.RESET_ALL}")

        link_app_to_settings(project_name, app_name)

        settings_file_path = os.path.join(project_directory, project_name, 'settings.py')

        EmailSmtp(settings_file_path)

        # Error handling for these configuration functions
        try:
            configure_media_and_static(settings_file_path)
            include_app_urls(project_name, app_name)
            configure_templates(settings_file_path)
            configure_allowed_hosts(settings_file_path)
            configure_installed_apps(settings_file_path)
        except Exception as e:
            print(f"Error configuring settings: {e}")

        create_templates_and_static_folders(app_name)
    except Exception as e:
        print(f"Error creating Django app: {e}")

if __name__ == "__main__":
    try:
        selected_directory = select_directory()
        
        if selected_directory:
            print(f"{Fore.BLUE}Selected directory in main.py: {selected_directory}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No directory selected in main.py.{Style.RESET_ALL}")
        
        try:
            project_name = input("Enter the Django project name: ")
            # Check if project name already exists and get a valid name if needed
            project_name = get_valid_project_name(selected_directory, project_name)

        except Exception as e:
            print(f"Error while taking input Project name: {e}")
        try:
            app_name = input("Enter the Django app name: ")
        except Exception as e:
            print(f"Error while taking input app name: {e}")

        create_django_project(project_name, selected_directory)
        create_django_app(project_name, app_name)

        try:
            configure_views(app_name)  # Call the configure_views function inside the try block
        except Exception as e:
            print(f"Error configuring views: {e}")


        add_registration = input("Do you want to add the registration system to your project? (yes/no): ").lower()
        if add_registration == "yes":
            try:
                # Call the function and pass the app_name
                copy_code_to_views(app_name)
                add_code_to_models(app_name)
                add_code_to_admin(app_name)
                append_code_to_urls(app_name)
                copy_login_signup_templates(app_name)
                
            except Exception as e:
                print(f"Error adding registration system: {e}")



    except KeyboardInterrupt:  # Handle Ctrl+C or Ctrl+Z gracefully
        print(f"\n\n{Fore.MAGENTA}Process terminated by user.{Style.RESET_ALL}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ensure the program exits gracefully
sys.exit(0)