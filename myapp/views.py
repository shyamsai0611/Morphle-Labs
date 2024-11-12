from django.http import HttpResponse
from django.utils.timezone import datetime
import os
import pytz
import psutil

def htop_view(request):
    # Define the data
    name = "K. Shyam Sai Manohar"  # Replace with your full name
    username = os.getlogin()  # Get system username
    ist = pytz.timezone('Asia/Kolkata')  # Define IST timezone
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")  # Get server time in IST

    # Get the system stats using psutil
    top_output = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        top_output.append(f"{proc.info['pid']:>6} {proc.info['name']:<20} {proc.info['cpu_percent']:>5} % {proc.info['memory_percent']:>5.2f} %")

    # Format the output similar to `top`
    top_output = "\n".join(top_output)

    # Generate HTML response
    html_content = f"""
    <html>
        <body>
            <h2>System Information</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h3>Top Command Output:</h3>
            <pre>PID     Name                 CPU %    Memory %\n{top_output}</pre>
        </body>
    </html>
    """
    return HttpResponse(html_content)
