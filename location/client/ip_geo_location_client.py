from typing import Optional
from typing import Dict, Any
import requests
import os
import json
from ip.client.get_ip_client_interface import IPClientInterface
from ip.client.ipify_ip_client import IpifyIpClient
from location.client.location_client_interface import LocationClientInterface
from location.dtos.location_dto import LocationDTO

class IPGeoLocationClient(LocationClientInterface):
    def __init__(self, api_key: str | None = None, ip_client: IPClientInterface = None):
        self.api_key = api_key or os.getenv("IP_GEOLOCATION_API_KEY")
        self.ip_client = ip_client or IpifyIpClient()
        self.base_url = f"https://api.ipgeolocation.io/v2/ipgeo?apiKey={self.api_key}"
        self._ip: Optional[str] = None

    def get_location(self) -> LocationDTO:
        if not self.ready():
            raise RuntimeError("IPGeoLocationClient is not ready — missing API key")
        response = requests.get(self._build_url())
        response.raise_for_status()
        print(json.dumps(response.json(), indent=2))
        location_dto = self._parse_response(response.json())
        return location_dto

    def _parse_response(self, response: Dict[str, Any]) -> LocationDTO:
        location = response.get("location", {})
        return LocationDTO(
            city=location.get("city"),
            country=location.get("country_name"),
            latitude=float(location.get("latitude")),
            longitude=float(location.get("longitude")),
            continent=location.get("continent_name"),
            zipcode=location.get("zipcode"),
            district=location.get("district")
        )

    def _build_url(self) -> str:
        return f"{self.base_url}&ip={self._ip}"

    def ready(self) -> bool:
        if self.api_key is None:
            return False
        if self._ip is None:
            try:
                self._ip = self.ip_client.get_public_ip()
                return self._ip is not None
            except requests.RequestException:
                return False
        return True
