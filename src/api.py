from enums import Collection

class BiorxivApi:
    """A wrapper for sending request to the bioRxiv server."""
    BASE_URL = "https://www.biorxiv.org"

    def __init__(self, field: Collection) -> None:
        self.field = field.lower()
        self.url = None
        self.response = None
        if self.field in Collection:
            self._compose_url()
        else:
            raise ValueError("invalid `field` parameter")

    def _compose_url(self) -> None:
        """Builds a url from the given field."""
        url = f"{self.BASE_URL}/collection/{self.field}"
        self.url = url

    def fetch(self) -> str:
        """
        Builds a query url based on the given field and sends a request
        to the bioRxiv server.
        
        Returns a status code upon receiving a valid Response object.
        """
        import requests
        resp = requests.get(self.url)
        resp.raise_for_status()
        self.response = resp
        return resp.status_code

