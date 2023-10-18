import os
import sys
import re

def link_app_to_settings(project_name, app_name):
    try:
        # Find the settings.py file in the project directory
        # project_directory = os.path.join(os.getcwd(), project_name) # add project_directory to setting_file if base project is setuped 
        settings_file = os.path.join( project_name, 'settings.py')

        if not os.path.exists(settings_file):
            print(f"Error: '{settings_file}' not found. Please make sure the project name is correct.")
            return

        # Read the settings.py file
        with open(settings_file, 'r') as f:
            content = f.read()

        # Check if the app is already in INSTALLED_APPS
        pattern = r"INSTALLED_APPS\s*=\s*\[([\s\S]*?)\]"
        installed_apps_match = re.search(pattern, content)
        if installed_apps_match:
            installed_apps_content = installed_apps_match.group(1)
            if f"'{app_name}'" in installed_apps_content:
                print(f"'{app_name}' is already in INSTALLED_APPS.")
                return

            # Append the app to INSTALLED_APPS
            new_installed_apps_content = installed_apps_content.strip() + f"\n    '{app_name}',"
            new_content = content.replace(installed_apps_match.group(0), f"INSTALLED_APPS = [\n{new_installed_apps_content}\n]")
        else:
            print("Error: 'INSTALLED_APPS' not found in settings.py.")
            return

        # Write the updated content back to settings.py
        with open(settings_file, 'w') as f:
            f.write(new_content)

        print(f"Linked '{app_name}' to INSTALLED_APPS in '{settings_file}' successfully.")
    except Exception as e:
        print(f"Error linking app to settings: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python link_app_to_settings.py <project_name> <app_name>")
    else:
        project_name = sys.argv[1]
        app_name = sys.argv[2]
        link_app_to_settings(project_name, app_name)
