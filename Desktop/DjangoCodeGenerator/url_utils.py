import os

def include_app_urls(project_name, app_name):
    try:
        # Get the project's urls.py file path
        # project_directory = os.path.join(os.getcwd(), project_name)
        project_urls_file = os.path.join( project_name, 'urls.py')

        if not os.path.exists(project_urls_file):
            print(f"Error: '{project_urls_file}' not found. Please make sure the project name is correct.")
            return

        # Read the project's urls.py file
        with open(project_urls_file, 'r') as f:
            content = f.read()

        # Check if the app's URLs are already included
        if f'include("{app_name}.urls")' not in content:
            # Append the app's URLs to the project's urls.py
            new_content = content.replace(
                "from django.urls import path\n",
                f"from django.urls import path, include\n\n"
            )

            new_content = new_content.replace(
                "urlpatterns = [\n",
                f"urlpatterns = [\n    path('', include('{app_name}.urls')),\n"
                
            )

            # Write the updated content back to project's urls.py
            with open(project_urls_file, 'w') as f:
                f.write(new_content)

            print(f"Included '{app_name}' URLs in '{project_urls_file}' successfully.")
        else:
            print(f"'{app_name}' URLs are already included in '{project_urls_file}'.")

        # Check if the app's urls.py file exists, if not, create it
        app_directory = os.path.join(app_name)
        app_urls_file = os.path.join(app_directory, 'urls.py')

        if not os.path.exists(app_urls_file):
            with open(app_urls_file, 'w') as f:
                f.write(f"from django.urls import path\n\nfrom . import views\n\nurlpatterns = [\n    path('',views.index,name='home'),\n# Add values here this section\n]\n")
                f.write("\n\n\n\nfrom django.conf import settings \nfrom django.conf.urls.static import static \nurlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ")

            print(f"Created '{app_name}/urls.py' file successfully.")

    except Exception as e:
        print(f"Error including app URLs: {e}")
