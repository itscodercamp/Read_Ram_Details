import os

def configure_views(app_name):
    try:
        # Open the existing views.py file inside the app folder
        views_file_path = os.path.join(app_name, 'views.py')
        
        # Check if views.py already exists
        if os.path.exists(views_file_path):
            with open(views_file_path, 'a') as f:
                # Append the view code for 'index' that renders 'index.html'
                f.write(f"from .models import *\n")
                f.write(f"from django.shortcuts import HttpResponse\n\n")
                f.write("def index(request):\n")
                f.write("    # Your view logic here\n")
                f.write(f"    return render(request, 'index.html')\n")

            print(f"Added 'index' view code to 'views.py' in '{app_name}' successfully.")
        else:
            print(f"'views.py' does not exist in '{app_name}'. Please create it manually.")

    except Exception as e:
        print(f"Error configuring views: {e}")

