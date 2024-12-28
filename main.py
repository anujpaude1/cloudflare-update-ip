import requests
from dotenv import load_dotenv
import os
import subprocess
import re

load_dotenv()

#api token - my profile - api tokens - create token - edit zone - zone - dns - edit
API_TOKEN = os.getenv('API_TOKEN')

#zone id - specific domain - overview - api - zone id
ZONE_ID = os.getenv('ZONE_ID')

#record id - edit dns record - audit log - record id
RECORD_ID = os.getenv('RECORD_ID')

#dns name
DNS_NAME = os.getenv('DNS_NAME')



# Get the current public IP
def get_public_ip():
    try:
        # Run the `ip` command to fetch IPv6 addresses
        result = subprocess.run(['ip', '-6', 'addr', 'show', 'scope', 'global'], 
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            raise Exception(result.stderr.strip())
        
        # Use regex to extract IPv6 addresses
        ipv6_addresses = re.findall(r'inet6 ([\da-f:]+)', result.stdout)
        
        if not ipv6_addresses:
            return "No global IPv6 address found."
        
        # Return the first global IPv6 address
        return f"Current IPv6 address: {ipv6_addresses[0]}"
    
    except FileNotFoundError:
        return "The 'ip' command is not available. Please install 'iproute2'."
    except Exception as e:
        return f"An error occurred: {e}"

# Update Cloudflare DNS record
def update_dns_record(ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{RECORD_ID}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "type": "AAAA",
        "name": DNS_NAME,
        "content": ip,
        "ttl": 1,  # Automatic TTL
        "proxied": True  # Enable Cloudflare proxy
    }
    response = requests.put(url, json=data, headers=headers)
    return response.json()

# Main
if __name__ == "__main__":
    public_ip = get_public_ip()
    print(f"Current public IP: {public_ip}")
    result = update_dns_record(public_ip)
    print(result)
