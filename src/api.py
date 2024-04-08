from time import sleep
from enums import Collection

class BiorxivApi:
    """A wrapper for sending request to the bioRxiv server."""
    BASE_URL = "https://www.biorxiv.org"

    def __init__(self, field: Collection) -> None:
        self.field = field.lower()
        self.url = None
        self.response = []
        if self.field in Collection:
            self._compose_url()
        else:
            raise ValueError("invalid `field` parameter")

    def _compose_url(self) -> None:
        """Builds a url from the given field."""
        url = f"{self.BASE_URL}/collection/{self.field}"
        self.url = url

    def fetch(self, n_pages=1) -> str:
        """
        Builds a query url based on the given field and sends a request
        to the bioRxiv server.
        
        Returns a status code upon receiving a valid Response object.
        """
        import requests
        print("Sending a GET request to server...")
        for page in range(n_pages):
            payload = {"page": page}
            print(f"Retrieving page {page+1} of {n_pages}...")
            resp = requests.get(self.url, payload)
            resp.raise_for_status()
            self.response.append(resp)
            sleep(0.25)
        print("All responses have been collected!")
        return resp.status_code

