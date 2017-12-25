import socket
from app import app

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

targeturl = s.getsockname()[0]
app.run(host=targeturl, debug=True)