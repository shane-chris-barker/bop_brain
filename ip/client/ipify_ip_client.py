import logging
from typing import Optional
logger = logging.getLogger(__name__)
import requests
from ip.client.get_ip_client_interface import IPClientInterface

class IpifyIpClient(IPClientInterface):
    def __init__(self):
        self.base_url = "https://api.ipify.org?format=json"
        self.log_prefix = "[🛜 IPIFY IP CLIENT]"

    def get_public_ip(self) -> Optional[str]:
        logger.info(f"{self.log_prefix} is trying to get public IP")
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.json().get("ip")
        except requests.RequestException as e:
            logger.error(f"{self.log_prefix} Could not get IP - {e}")
            return None
