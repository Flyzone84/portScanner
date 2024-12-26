Simple Port Scanner
A simple Python-based port scanner to check the status of ports (open or closed) on a target system. This tool is designed for educational purposes and should only be used for ethical hacking, i.e., scanning systems you have permission to test.

Table of Contents
Project Description
Features
Installation
Usage
Requirements
Contributing
License
Project Description
This project is a Port Scanner written in Python that allows you to check whether specific ports are open or closed on a given target IP address or domain name. The script scans a specified range of ports and returns the status of each port, which helps in identifying vulnerabilities or ensuring the availability of necessary services.

This script is for educational purposes only. Please ensure you have explicit permission to scan any network or system, as unauthorized scanning can be considered illegal.

Features
Scans a user-defined range of ports.
Reports whether each port is open or closed.
Allows scanning by IP address or domain name.
Displays the time taken for the scan to complete.
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/simple-port-scanner.git
Navigate to the project folder:

bash
Copy code
cd simple-port-scanner
Ensure you have Python 3.x installed on your system. You can check the Python version by running:

bash
Copy code
python --version
The script uses Python's built-in libraries (socket, datetime), so no additional packages are required.

Usage
Run the script by executing the following command in your terminal:

bash
Copy code
python port_scanner.py
The script will prompt you for the following inputs:

Target IP address or domain name: The system you want to scan.
Starting port: The first port in the range to scan.
Ending port: The last port in the range to scan.
The script will begin scanning the specified range of ports and display whether each port is open or closed.

Example:
bash
Copy code
Welcome to the Simple Port Scanner!
Enter the target IP address or domain name: 192.168.1.1
Enter the starting port: 20
Enter the ending port: 25
Scanning ports 20-25 on 192.168.1.1
--------------------------------------------------
Port 20 is CLOSED
Port 21 is OPEN
Port 22 is OPEN
Port 23 is OPEN
Port 24 is CLOSED
Port 25 is OPEN
--------------------------------------------------
Scanning completed in 0:00:03.234567
Requirements
Python 3.x
No additional libraries are required (uses Python's built-in socket and datetime libraries).
Contributing
If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Here are a few suggestions for improvement:

Add multi-threading to speed up port scanning.
Implement advanced scanning techniques (e.g., service detection).
Add error handling for unreachable hosts or other exceptions.
Please ensure any contributions align with the purpose of the project and adhere to ethical hacking practices.

License
This project is licensed under the MIT License - see the LICENSE file for details.
