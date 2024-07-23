import socket
import ipinfo

# Function to read the access token from a file
def get_access_token():
    try:
        with open('AccessToken.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("AccessToken.txt file not found.")
        return None

# Function to print details of the IP address using the ipinfo API
def print_details(ip_add):
    access_token = get_access_token()
    if not access_token:
        print("Access token is missing.")
        return

    handler = ipinfo.getHandler(access_token)
    
    try:
        # Fetch details of the given IP address
        details = handler.getDetails(ip_add)
        print(f"IP Address: {ip_add}")
        print(f"Location: {details.city}, {details.region}, {details.country}")
        print(f"Coordinates: (Lat: {details.latitude}, Lng: {details.longitude})")
        print(f"Time Zone: {details.timezone}")
        print(f"ISP: {details.org}")
    except Exception as e:
        # Handle any errors that occur during API call
        print(f"Error retrieving details: {e}")

# Function to get the IP address from a URL
def get_ip_from_url(url):
    try:
        # Resolve the URL to an IP address
        return socket.gethostbyname(url)
    except socket.gaierror:
        # Handle errors if the URL is invalid or cannot be resolved
        print("Invalid URL or the URL could not be resolved.")
        return None

def main():
    # Prompt user to choose between tracking by URL or IP address
    choice = input("Track by URL, Enter: 1\nTrack by Ip, Enter: 2\nEnter your Key: ")

    if choice == '1':
        url = input("Enter URL: ")
        ip_add = get_ip_from_url(url)
        if ip_add:
            # Print details of the resolved IP address
            print_details(ip_add)
    elif choice == '2':
        ip_add = input("Enter IP address: ")
        # Print details of the provided IP address
        print_details(ip_add)
    else:
        # Handle invalid choice
        print("Invalid choice. Please enter 1 or 2.")

# Entry point of the script
if __name__ == "__main__":
    main()
