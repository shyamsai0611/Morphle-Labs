from django.http import HttpResponse
from django.utils.timezone import datetime
import pytz
import subprocess

def htop_view(request):
    
    name = "K. Shyam Sai Manohar"  
    username = "Shyam Sai"
    ist = pytz.timezone('Asia/Kolkata')  
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")  

    
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except subprocess.CalledProcessError as e:
        top_output = "Could not retrieve `top` output."

    
    html_content = f"""
    <html>
        <body>
            <h2>System Information</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h3>Top Command Output:</h3>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return HttpResponse(html_content)
