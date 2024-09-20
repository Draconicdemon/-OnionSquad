import webbrowser
import socket

def open_ocint_page():
    url = "https://www.cyberbackgroundchecks.com"  # Replace with the actual OCINT page URL
    webbrowser.open(url)
    print(f"Opening {url}...\n")

def show_discord_link():
    discord_link = "https://discord.gg/onionsquad"
    print(f"Join the Discord here: {discord_link}\n")

def check_ports(ip, ports):
    print(f"Checking open ports on {ip}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        sock.close()
    print()

def scan_ips(ip_range):
    # This is a placeholder. You can use advanced tools like 'nmap' or 'scapy' for real IP scanning.
    print(f"Scanning IP range {ip_range} (Placeholder function)...")
    print()

def main():
    while True:
        print("======= OnionSquad Tool =======")
        print("1. Open OCINT Page")
        print("2. Show Discord Link")
        print("3. Check Ports")
        print("4. Scan IPs")
        print("0. Exit")
        print("===============================")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            open_ocint_page()
        elif user_input == "2":
            show_discord_link()
        elif user_input == "3":
            ip = input("Enter the IP address to check ports: ")
            ports = input("Enter the ports to check (comma-separated, e.g., 22,80,443): ")
            port_list = [int(port.strip()) for port in ports.split(',')]
            check_ports(ip, port_list)
        elif user_input == "4":
            ip_range = input("Enter the IP range to scan (e.g., 192.168.1.1-192.168.1.255): ")
            scan_ips(ip_range)
        elif user_input == "0":
            print("Exiting OnionSquad tool.")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
