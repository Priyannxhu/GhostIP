import requests
import pyfiglet

def geolocate_ip(ip):
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        country = data.get('country_name', 'Unknown')
        city = data.get('city', 'Unknown')
        region = data.get('region', 'Unknown')
        postal = data.get('postal', 'Unknown')
        latitude = data.get('latitude', 'Unknown')
        longitude = data.get('longitude', 'Unknown')

        figlet = pyfiglet.Figlet()
        print(figlet.renderText("IP Geolocation"))

        print("Geolocating IP...\n")
        print(f"IP: {ip}")
        print(f"Country: {country}")
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Postal Code: {postal}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Unable to geolocate IP.")

# Example usage
figlet = pyfiglet.Figlet()
print(figlet.renderText("IP Geolocation"))

ip_address = input("Enter IP address to geolocate: ")
print()

geolocate_ip(ip_address)
