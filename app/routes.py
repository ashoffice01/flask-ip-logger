# from flask import Blueprint, request, send_file, jsonify
# from datetime import datetime
# import os

# bp = Blueprint('main', __name__)

# LOG_FILE = "ip_logs.txt"  # Define the log file path
# TXT_FILE = "/Christmas_cards.txt"
# PDF_FILE = "/Christmas_cards.pdf"  # Define the file you want to serve

# def log_to_file(ip_address):
#     """Log the IP address to a text file with a timestamp."""
#     with open(LOG_FILE, "a") as f:
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         f.write(f"{timestamp} - {ip_address}\n")

# @bp.route('/')
# def home():
#     visitor_ip = request.remote_addr
#     return f"Your IP address is: {visitor_ip}"

# @bp.route('/Christmas_cards.txt', methods=['GET'])
# def log_ip_txt():
#     """Serve the log file as a .txt download and log the IP."""
#     visitor_ip = request.remote_addr
#     log_to_file(visitor_ip)  # Log the IP to the file
#     return send_file(TXT_FILE, as_attachment=True)

# @bp.route('/Christmas_cards.pdf', methods=['GET'])
# def log_ip_pdf():
#     """Serve a .pdf (simulated) log file and log the IP."""
#     visitor_ip = request.remote_addr
#     log_to_file(visitor_ip)  # Log the IP to the file

#     # Simulating a PDF file (you can generate a real one if desired)
#     with open(PDF_FILE, 'wb') as f:
#         f.write(b'%PDF-1.4\n%PDF generated for logging\n')
#         f.write(f"IP Address: {visitor_ip}\n".encode())
#         f.write(b"%%EOF\n")

#     return send_file(PDF_FILE, as_attachment=True)


from flask import Blueprint, request, send_file, jsonify
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

bp = Blueprint('main', __name__)

LOG_FILE = "ip_logs.txt"  # Define the log file path
TXT_FILE = "Christmas_cards.txt"
PDF_FILE = "/Christmas_cards.pdf"  # Define the file you want to serve

def log_to_file(ip_address):
    """Log the IP address to a text file with a timestamp."""
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {ip_address}\n")

@bp.route('/')
def home():
    visitor_ip = request.remote_addr
    return f"Your IP address is: {visitor_ip}"

@bp.route('/christmas_greetings.txt', methods=['GET'])
def log_ip_txt():
    """Serve the log file as a .txt download and log the IP."""
    visitor_ip = request.remote_addr
    log_to_file(visitor_ip)  # Log the IP to the file
    print('christmas_greetings')
    return send_file(LOG_FILE, as_attachment=True)

@bp.route('/log_ip.pdf', methods=['GET'])
def log_ip_pdf():
    """Generate and serve a PDF file with an embedded URL that triggers logging."""
    visitor_ip = request.remote_addr
    log_to_file(visitor_ip)  # Log the IP to the file

    # Create a PDF with an embedded link to trigger the /log_ip route
    c = canvas.Canvas(PDF_FILE, pagesize=letter)
    c.drawString(100, 750, "Click the link below to trigger the log:")
    c.setFont("Helvetica", 12)
    # Create a clickable link in the PDF
    c.linkURL("http://127.0.0.1:5000/log_ip.txt", (100, 730, 300, 750), relative=1)
    c.drawString(100, 710, "Click here to log the IP address")
    c.save()

    return send_file(PDF_FILE, as_attachment=True)

