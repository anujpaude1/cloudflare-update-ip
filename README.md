# Cloudflare Update IP

This project is a Python script that updates a Cloudflare DNS record with the current public IPv6 address of your machine.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/cloudflare-update-ip.git
    cd cloudflare-update-ip
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Cloudflare API token, zone ID, record ID, and DNS name:
    ```env
    API_TOKEN=your_api_token
    ZONE_ID=your_zone_id
    RECORD_ID=your_record_id
    DNS_NAME=your_dns_name
    ```

## Usage

Run the script:
```sh
python main.py
```

The script will fetch the current public IPv6 address and update the specified Cloudflare DNS record.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.