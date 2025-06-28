import socket

def find_free_port():
    """
    Find a free port that is not currently in use.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))  # Bind to localhost and let the OS choose a free port
    port = sock.getsockname()[1]  # Get the port number
    sock.close()  # Close the socket
    return port

# Find a free port
port = find_free_port()
print(f"Free port found: {port}")
