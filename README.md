# SmartScan-Pro-Advanced-Port-Scanner

## Project Overview
SmartScan Pro is a GUI-based TCP Port Scanner developed using Python and Nmap.
It allows users to scan open ports on a target system using multiple advanced scanning techniques.

This tool is designed for network analysis, cybersecurity learning, and port monitoring.

## Features
- User-friendly GUI using Tkinter
- Basic TCP Port Scan
- SYN Scan (Stealth Scan)
- Service Version Detection
- OS Detection
- Aggressive Scan
- Start / Stop Scan functionality
- Real-time output display
- Save scan results to file
- Clear output option
- Dark / Light mode toggle

## Technologies Used
- Python
- Tkinter (GUI)
- Nmap (Network Scanner)

## Installation (Kali Linux)
sudo apt update
sudo apt install nmap python3-tk -y

## How to Run
nano smartscan_pro.py
sudo python3 smartscan_pro.py

## Example Usage
Enter target:
scanme.nmap.org

Then select any scan type:
- Basic Scan
- SYN Scan
- Service Scan
- OS Detection
- Aggressive Scan

## Sample Output
22/tcp open ssh
80/tcp open http
443/tcp open https

## Important Note
If no ports are displayed, it means:
- All ports are closed OR
- Ports are filtered by firewall

OS Detection may fail if:
- No open and closed ports are available
- Target is protected or behind firewall

## Use Cases
- Network Security Testing
- Port Analysis
- Learning Ethical Hacking
- System Monitoring

## Screenshots
(Add your screenshots here)

## Author
VADDHIPARTHI RAGHU
