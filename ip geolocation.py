import re
import requests
import folium
import ipaddress

# Sample `tracert` output
tracert_output = """
Tracing route to linkedin.com [198.18.255.254]
over a maximum of 30 hops:

  1     2 ms     1 ms     2 ms  10.110.131.129
  2    21 ms    13 ms    15 ms  109.144.192.25
  3    15 ms    15 ms    16 ms  192.168.204.252
  4    16 ms    33 ms    23 ms  198.18.255.254

Trace complete.
"""

# Extract only IPv4 addresses from the tracert output
ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', tracert_output)

# Initialize map centered on a default location
m = folium.Map(location=[51.5074, -0.1278], zoom_start=3)  # Centered on London

# Define the API URL for ip-api.com
API_URL = 'http://ip-api.com/json/'

for ip in ips:
    # Skip private IPs using the ipaddress library
    if ipaddress.ip_address(ip).is_private:
        print(f"Skipping private IP: {ip}")
        continue

    try:
        # Get geolocation data from ip-api.com
        response = requests.get(f'{API_URL}{ip}')
        data = response.json()

        # Print the response for debugging
        print(f"Response for IP {ip}: {data}")

        # Check if the response is successful and has latitude and longitude
        if data['status'] == 'success':
            lat = data['lat']
            lon = data['lon']
            print(f"IP: {ip}, Location: ({lat}, {lon})")  # Confirm coordinates

            # Add a marker to the map
            folium.Marker(
                location=[lat, lon],
                popup=f"IP: {ip}\nCity: {data.get('city', 'N/A')}\nCountry: {data.get('country', 'N/A')}",
                tooltip=ip
            ).add_to(m)
        else:
            print(f"No location data for IP {ip}")

    except Exception as e:
        print(f"Could not retrieve data for IP {ip}: {e}")

# Add a test marker to ensure the map and markers work
folium.Marker(
    location=[51.5074, -0.1278],  # Coordinates for London
    popup="Test Marker - London",
    tooltip="London"
).add_to(m)

# Save map to an HTML file
m.save("tracert_geolocation_map.html")
print("Map saved as tracert_geolocation_map.html")
