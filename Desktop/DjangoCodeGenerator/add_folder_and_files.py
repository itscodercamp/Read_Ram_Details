import os
import shutil

def create_templates_and_static_folders(app_name):
    try:
        # Create a 'templates' folder inside the app folder if it doesn't exist
        templates_directory = os.path.join(app_name, 'templates')
        if not os.path.exists(templates_directory):
            os.makedirs(templates_directory)
            print(f"Created 'templates' folder inside '{app_name}' successfully.")
        else:
            print(f"'templates' folder already exists inside '{app_name}'.")

        # Copy 'base.html' and 'index.html' from source_templates folder to app's 'templates' folder
        source_template_folder = os.path.join(os.path.dirname(__file__), 'basic_requirements_addons', 'html')  # Adjust 'source_templates' folder path as needed
        for html_file in ['base.html', 'index.html']:
            source_file = os.path.join(source_template_folder, html_file)
            destination_file = os.path.join(templates_directory, html_file)
            shutil.copyfile(source_file, destination_file)
            print(f"Copied '{html_file}' to 'templates' folder inside '{app_name}'.")

        # Create a 'static' folder inside the app folder if it doesn't exist
        static_directory = os.path.join(app_name, 'static')
        if not os.path.exists(static_directory):
            os.makedirs(static_directory)
            print(f"Created 'static' folder inside '{app_name}' successfully.")
        else:
            print(f"'static' folder already exists inside '{app_name}'.")

        # Copy specific folders from basic_requirements_addons\asset to the app's 'static' folder
        source_asset_folder = os.path.join(os.path.dirname(__file__), 'basic_requirements_addons', 'asset')  # Adjust the path as needed
        folders_to_copy = ['css', 'js', 'images','FontAwesome']  # Specify the folders you want to copy

        for folder in folders_to_copy:
            source_folder = os.path.join(source_asset_folder, folder)
            destination_folder = os.path.join(static_directory, folder)
            
            if not os.path.exists(destination_folder):
                shutil.copytree(source_folder, destination_folder)
                print(f"Copied folder '{folder}' to 'static' folder inside '{app_name}'.")
            else:
                print(f"'{folder}' folder already exists inside '{app_name}'.")

    except Exception as e:
        print(f"Error creating folders: {e}")
