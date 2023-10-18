# import psutil

# # Get a list of all running processes
# running_processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name', 'username', 'memory_info', 'cpu_percent', 'status'])]

# # Display the list of running processes with detailed information
# print("Running Processes:")
# for process in running_processes:
#     print(f"PID: {process['pid']}")
#     print(f"Name: {process['name']}")
#     print(f"Username: {process['username']}")
#     print(f"Memory Usage: {process['memory_info']}")  # This includes resident memory (RSS) and virtual memory (VMS)
#     print(f"CPU Usage: {process['cpu_percent']}%")
#     print(f"Status: {process['status']}")
#     print()

#     try:
#         p = psutil.Process(process['pid'])
#         try:
#             cmdline = p.cmdline()
#             print(f"Command Line: {cmdline}")
#         except psutil.AccessDenied:
#             print("Access to command line denied")
        
#         try:
#             open_files = p.open_files()
#             print(f"Open Files: {open_files}")
#         except psutil.AccessDenied:
#             print("Access to open files denied")

#         # You can add more process attributes as needed
#     except psutil.NoSuchProcess:
#         print("Process not found")

#     print()


import psutil
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Get a list of all running processes
running_processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name', 'username', 'memory_info', 'cpu_percent', 'status'])]

# Create a list to store the process information
process_info = []

# Populate the process_info list
for process in running_processes:
    info = f"PID: {process['pid']}\n"
    info += f"Name: {process['name']}\n"
    info += f"Username: {process['username']}\n"
    info += f"Memory Usage: {process['memory_info']}\n"
    info += f"CPU Usage: {process['cpu_percent']}%\n"
    info += f"Status: {process['status']}\n"

    try:
        p = psutil.Process(process['pid'])
        try:
            cmdline = p.cmdline()
            info += f"Command Line: {cmdline}\n"
        except psutil.AccessDenied:
            info += "Access to command line denied\n"

        try:
            open_files = p.open_files()
            info += f"Open Files: {open_files}\n"
        except psutil.AccessDenied:
            info += "Access to open files denied\n"
    except psutil.NoSuchProcess:
        info += "Process not found\n"

    process_info.append(info)

# Create a PDF document
doc = SimpleDocTemplate("process_info.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Add process information to the PDF
for info in process_info:
    p = Paragraph(info, styles["Normal"])
    story.append(p)
    story.append(Spacer(1, 12))

doc.build(story)

print("Process information saved to process_info.pdf")
