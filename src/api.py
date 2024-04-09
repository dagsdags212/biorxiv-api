import asyncio
import httpx
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

    async def _get(self, client: httpx.AsyncClient, params: dict) -> httpx.Response:
        """Sends an asynchronous request to the server."""
        resp = await client.get(self.url, params=params)
        resp.raise_for_status()
        return resp

    async def fetch(self, n_pages=1) -> str:
        """
        Builds a query url based on the given field and sends a request
        to the bioRxiv server.
        
        Returns a status code upon receiving a valid Response object.
        """
        print("Fetching data from server...")
        async with httpx.AsyncClient() as client:
            response = await asyncio.gather(
                *[self._get(client, {"page": i}) for i in range(n_pages)]
            )
            self.response = response
        print("All responses have been collected!")
            
        return response

