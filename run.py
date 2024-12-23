import os
from app import create_app

LOG_FILE = "ip_logs.txt"
PDF_FILE = "ip_log.pdf"

# Create the log file if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("IP Address Logs\n")
        f.write("=" * 20 + "\n")

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
