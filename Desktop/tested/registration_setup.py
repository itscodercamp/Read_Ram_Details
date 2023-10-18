# registration_setup.py

import os
import sys

def add_registration_system(app_name):
    try:
        add_registration = input("Do you want to add a registration system to your project? (yes/no): ").lower()
        if add_registration == 'yes':
            add_registration_url(app_name)
            create_login_view(app_name)
            create_template_files(app_name)
            append_models_code(app_name)
    except Exception as e:
        print(f"Error occurred during registration setup: {e}")
        sys.exit(1)

def add_registration_url(app_name):
    urls_file_path = f'{app_name}/urls.py'
    with open(urls_file_path, 'r') as urls_file:
        urls_content = urls_file.read()
    
    if 'from django.contrib.auth import views as auth_views' not in urls_content:
        with open(urls_file_path, 'a') as urls_file:
            urls_content_to_add = get_file_content('.View_Url_Models_Setup/registration_url.txt')
            urls_file.write(urls_content_to_add)

def create_login_view(app_name):
    views_file_path = f'{app_name}/views.py'
    with open(views_file_path, 'r') as views_file:
        views_content = views_file.read()
    
    if 'from django.shortcuts import render\nfrom django.contrib.auth.decorators import login_required' not in views_content:
        with open(views_file_path, 'a') as views_file:
            views_content_to_add = get_file_content('.View_Url_Models_Setup/login_view.txt')
            views_file.write(views_content_to_add)

def create_template_files(app_name):
    templates_dir = f'{app_name}/templates'
    os.makedirs(templates_dir, exist_ok=True)

    login_html_path = os.path.join(templates_dir, 'login.html')
    if not os.path.exists(login_html_path):
        login_html_content = get_file_content('.Html_Setup_Folder/login_template.html')
        with open(login_html_path, 'w') as login_html_file:
            login_html_file.write(login_html_content)

    signup_html_path = os.path.join(templates_dir, 'signup.html')
    if not os.path.exists(signup_html_path):
        signup_html_content = get_file_content('.Html_Setup_Folder/signup_template.html')
        with open(signup_html_path, 'w') as signup_html_file:
            signup_html_file.write(signup_html_content)

def append_models_code(app_name):
    models_file_path = f'{app_name}/models.py'
    if not os.path.exists(models_file_path):
        return
    
    models_content = get_file_content('.View_Url_Models_Setup/models.txt')
    with open(models_file_path, 'a') as models_file:
        models_file.write(models_content)

def get_file_content(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as file:
        content = file.read()
    return content
