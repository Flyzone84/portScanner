import socket
from datetime import datetime

# Function to scan a single port
def scan_port(target, port):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Set timeout to 1 second
    
    # Try to connect to the given port on the target
    result = sock.connect_ex((target, port))  # connect_ex() returns an error code
    
    # Check if the port is open
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    
    # Close the socket connection
    sock.close()

# Function to scan a range of ports
def scan_ports(target, start_port, end_port):
    print(f"Scanning ports {start_port}-{end_port} on {target}")
    print("-" * 50)
    
    # Loop through the range of ports
    for port in range(start_port, end_port + 1):
        scan_port(target, port)
    
    print("-" * 50)

# Main program to accept input from user
def main():
    print("Welcome to the Simple Port Scanner!")
    
    # Get the target IP address or domain name
    target = input("Enter the target IP address or domain name: ")
    
    # Validate IP or domain format
    try:
        socket.gethostbyname(target)  # Check if the domain is valid
    except socket.gaierror:
        print("Invalid IP address or domain name")
        return
    
    # Get the port range from the user
    try:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
    except ValueError:
        print("Please enter valid numbers for ports.")
        return
    
    # Ensure the port range is valid
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Port numbers should be between 1 and 65535.")
        return
    
    # Start scanning
    start_time = datetime.now()
    print(f"Scanning started at {start_time}")
    
    scan_ports(target, start_port, end_port)
    
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Scanning completed in {total_time}")

if __name__ == "__main__":
    main()

