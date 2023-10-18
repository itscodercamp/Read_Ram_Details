# add_blog_to_project.py

import os
from setup_django_project import create_django_app, link_app_to_installed_apps, get_file_content

def add_blog_app_to_project(project_name):
    app_name = 'blog'  # You can change 'blog' to any name you prefer for the blog app
    create_django_app(app_name, project_name)
    link_app_to_installed_apps(app_name)
    copy_files_for_blog_app(app_name)

def copy_files_for_blog_app(app_name):
    # Copy the models.py file content
    models_file_content = get_file_content('.Blog_data_files/models_blog.txt')
    with open(f'{app_name}/models.py', 'w') as models_file:
        models_file.write(models_file_content)

    # Copy the urls.py file content
    urls_file_content = get_file_content('.Blog_data_files/urls_blog.txt')
    with open(f'{app_name}/urls.py', 'w') as urls_file:
        urls_file.write(urls_file_content)

    # Copy the views.py file content
    views_file_content = get_file_content('.Blog_data_files/views_blog.txt')
    with open(f'{app_name}/views.py', 'w') as views_file:
        views_file.write(views_file_content)

    # Copy the templates
    blog_templates_dir = os.path.join(app_name, 'templates', 'blog')
    os.makedirs(blog_templates_dir, exist_ok=True)

    index_html_content = get_file_content('.Blog_Html_files/index_blog.html')
    with open(os.path.join(blog_templates_dir, 'index.html'), 'w') as index_html_file:
        index_html_file.write(index_html_content)

    post_detail_html_content = get_file_content('post_detail.html')
    with open(os.path.join(blog_templates_dir, 'post_detail.html'), 'w') as post_detail_html_file:
        post_detail_html_file.write(post_detail_html_content)
