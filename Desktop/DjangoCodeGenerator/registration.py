import os
import shutil

def copy_code_to_views(app_name):
    try:
        # Get the directory of the current script (main.py)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the source file path based on the script directory
        source_file = os.path.join(script_dir, 'Registration_data', 'views.txt')
        
        # Define the destination file based on the app name
        destination_file = f'{app_name}/views.py'

        # Read the content from the source file (views.txt)
        with open(source_file, 'r') as source:
            new_content = source.read()

        # Append the new content to the destination file (app's views.py)
        with open(destination_file, 'a') as destination:
            destination.write('\n\n')  # Add some separation
            destination.write(new_content)

        print(f"Content from '{source_file}' appended to '{destination_file}' successfully.")
    except Exception as e:
        print(f"Error appending content: {e}")


def add_code_to_models(app_name):
    try:
        # Get the directory of the current script (main.py)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the source file path based on the script directory
        source_file = os.path.join(script_dir, 'Registration_data','models.txt')
        
        # Define the destination file based on the app name
        destination_file = f'{app_name}/models.py'

        # Read the content from the source file (models.txt)
        with open(source_file, 'r') as source:
            new_content = source.read()

        # Append the new content to the destination file (app's models.py)
        with open(destination_file, 'a') as destination:
            destination.write('\n\n')  # Add some separation
            destination.write(new_content)

        print(f"Content from '{source_file}' added to '{destination_file}' successfully.")
    except Exception as e:
        print(f"Error adding content to models.py: {e}")


def add_code_to_admin(app_name):
    try:
        # Get the directory of the current script (main.py)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the source file path based on the script directory
        source_file = os.path.join(script_dir, 'Registration_data','admin.txt')
        
        # Define the destination file based on the app name
        destination_file = f'{app_name}/admin.py'

        # Read the content from the source file (models.txt)
        with open(source_file, 'r') as source:
            new_content = source.read()

        # Append the new content to the destination file (app's models.py)
        with open(destination_file, 'a') as destination:
            destination.write('\n\n')  # Add some separation
            destination.write(new_content)

        print(f"Content from '{source_file}' added to '{destination_file}' successfully.")
    except Exception as e:
        print(f"Error adding content to admin.py: {e}")


import os

def append_code_to_urls(app_name):
    try:
        # Get the directory of the current script (main.py)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the source file path based on the script directory
        source_file = os.path.join(script_dir, 'Registration_data','urls.txt')
        
        # Define the destination file based on the app name
        destination_file = f'{app_name}/urls.py'

        # Read the content from the source file (urls.txt)
        with open(source_file, 'r') as source:
            new_code = source.read()

        # Read the content from the destination file (app's urls.py)
        with open(destination_file, 'r') as destination:
            existing_code = destination.read()

        # Search for a specific comment in the existing code
        comment_to_search = "# Add values here this section"
        if comment_to_search in existing_code:
            # Replace the comment with the new code
            new_content = existing_code.replace(comment_to_search, new_code)

            # Write the updated content back to the destination file
            with open(destination_file, 'w') as destination:
                destination.write(new_content)

            print(f"Code from '{source_file}' added to '{destination_file}' urlpatterns successfully.")
        else:
            print(f"Comment '{comment_to_search}' not found in '{destination_file}'. Please add it manually.")

    except Exception as e:
        print(f"Error adding code to urls.py: {e}")


def copy_login_signup_templates(app_name):
    try:
        # Get the directory of the current script (main.py)
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the source directory where login.html and signup.html are located
        source_templates_dir = os.path.join(script_dir, 'Registration_data')

        # Define the destination directory where app's templates are located
        destination_templates_dir = os.path.join(app_name, 'templates')

        # Define the filenames to copy
        files_to_copy = ['login.html', 'signup.html']

        # Check if the destination templates directory exists, create it if not
        if not os.path.exists(destination_templates_dir):
            os.makedirs(destination_templates_dir)

        # Copy login.html and signup.html from source to destination
        for file_name in files_to_copy:
            source_file_path = os.path.join(source_templates_dir, file_name)
            destination_file_path = os.path.join(destination_templates_dir, file_name)
            shutil.copyfile(source_file_path, destination_file_path)
            print(f"Copied '{file_name}' to 'templates' folder inside '{app_name}'.")

        print("Templates copied successfully.")
    except Exception as e:
        print(f"Error copying templates: {e}")


