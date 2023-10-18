# setup_django_project.py

import os
import sys
import subprocess
from colorama import Fore, Style

# All external App Imports
from registration_setup import *
from Settings_Setup import *
import add_blog_app

import time

def create_virtualenv(venv_name):
    if venv_name:
        subprocess.run(['python', '-m', 'venv', venv_name])

def install_packages(venv_name):
    if venv_name:
        subprocess.run([os.path.join(venv_name, "Scripts","activate.bat" if os.name == "nt" else "bin", "python"), '-m', 'pip', 'install', 'Pillow', 'django-jazzmin', 'Django'])

def create_django_project(project_name):
    subprocess.run(['django-admin', 'startproject', project_name])

def create_django_app(app_name, project_name):
    os.chdir(project_name)
    subprocess.run(['django-admin', 'startapp', app_name])

def create_app_urls(app_name):
    urls_file_content = f"""
from django.urls import path
from . import views

urlpatterns = [
    # Add your app URL patterns here
    # Example: path('app_url/', views.app_view, name='app_view'),
]
"""
    with open(f'{app_name}/urls.py', 'w') as urls_file:
        urls_file.write(urls_file_content)

def link_app_urls_to_project(app_name, project_name):
    # Add include statement for app urls in project urls
    with open(f"{project_name}/urls.py", "r") as f:
        content = f.read()
    content = content.replace(
        """from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
""", 
        f"from django.urls import path, include\n\nurlpatterns = [\n    path('admin/', admin.site.urls),\n    path('', include('{app_name}.urls')),\n]"
    )
    with open(f"{project_name}/urls.py", "w") as f:
        f.write(content)
    with open(f"{app_name}/urls.py", "a") as f:
        f.write("\nfrom django.conf import settings\n")
        f.write("from django.conf.urls.static import static\n\n")
        f.write("urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n")



def create_static_and_template_folders(app_name):
    templates_dir = os.path.join(app_name, 'templates')
    os.makedirs(templates_dir, exist_ok=True)

    static_dir = os.path.join(app_name, 'static')
    os.makedirs(static_dir, exist_ok=True)

def add_html_file_to_templates(app_name):
    templates_dir = os.path.join(app_name, 'templates')
    base_template_path = os.path.join(templates_dir, 'base.html')
    index_template_path = os.path.join(templates_dir, 'index.html')

    if not os.path.exists(base_template_path):
        base_template_content = get_file_content('.Html_Setup_Folder/base_template.html')
        with open(base_template_path, 'w') as base_template_file:
            base_template_file.write(base_template_content)

    if not os.path.exists(index_template_path):
        index_template_content = get_file_content('.Html_Setup_Folder/index_template.html')
        with open(index_template_path, 'w') as index_template_file:
            index_template_file.write(index_template_content)
            
def create_project():
        
        # mujori sambhalega bole toh arguments
    if len(sys.argv) < 3:
        print(Fore.GREEN + "\nUsage: python setup_django_project.py project_name app_name [venv_name]\n"+ Style.RESET_ALL)
        sys.exit(1)
    project_name = sys.argv[1]
    app_name = sys.argv[2]
    venv_name = sys.argv[3] if len(sys.argv) >= 4 else None

        # name check karega
    if os.path.exists(project_name):
        print(Fore.RED + f"\n\nDekh ye '{project_name}' name ka banda Pehlese idher hai Tu naya bana nhi toh ghar ja ...\n\n"+ Style.RESET_ALL)
        sys.exit(1)

    try:
        # ek hi name ka project banayega 
        os.makedirs(project_name, exist_ok=True)

        # Ye New wale project directory tk leke jayega
        os.chdir(project_name)

        create_virtualenv(venv_name)
        install_packages(venv_name)
        create_django_project(project_name)
        create_django_app(app_name, project_name)
        create_app_urls(app_name)
        link_app_urls_to_project(app_name, project_name)
        configure_project_settings(project_name, app_name)
        create_static_and_template_folders(app_name)
        add_html_file_to_templates(app_name)
        add_registration_system(app_name)
        add_blog_app.main(project_name)
        #  ye toh bss Run migrations wala kam hai
        print(Fore.GREEN + "\n2 second me kam 25\n "+ Style.RESET_ALL)
        time.sleep(2)
        python_executable = os.path.join(venv_name, "Scripts" if os.name == "nt" else "bin", "python") if venv_name else "python"
        subprocess.run([python_executable, 'manage.py', 'makemigrations'])
        subprocess.run([python_executable, 'manage.py', 'migrate'])
        
        # Ye error dekhega

    except OSError as e:
        print(Fore.RED + f"Himmat nhi harte bhai :\n\n Koyi nhi chalta hai bhai \n\n {e}"+ Style.RESET_ALL)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Command execution failed:\n\n Aare bhai bhai bhai bhai..... yo kya kr diyo \n\n {e}"+ Style.RESET_ALL)
        sys.exit(1)
    except KeyboardInterrupt:
        print(Fore.RED + "\nProcess interrupted by the user (Matlab. Teri Galti hai meri nhi)"+ Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    create_project()