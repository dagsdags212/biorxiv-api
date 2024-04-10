import asyncio
import httpx
from enums import Collection
from parser import CollectionParser, ContentParser
from trees import URL_TREE

class BiorxivApi:
    """A wrapper for sending request to the bioRxiv server."""

    def __init__(self, field: Collection, n_pages: int=1) -> None:
        self.field = field.lower()
        self.n_pages = n_pages if n_pages >= 1 else 1
        self.root_url = None
        self.collection_response = []
        self.content_response = []
        self.article_urls = []
        self.data = []

        self._compose_url()
        asyncio.run(self._fetch_collection())
        self._extract_article_urls()
        asyncio.run(self._fetch_content())
        self._extract_article_content()

    def _compose_url(self) -> None:
        """Builds a url from the given field."""
        field = self.field.lower()
        if field in Collection:
            url = f"{URL_TREE["collection"]}/{field}"
            self.root_url = url
        else:
            raise ValueError("invalid `field` parameter")

    async def _get(self, client: httpx.AsyncClient, url: str, params: dict={}) -> httpx.Response:
        """Sends an asynchronous request to the server."""
        resp = await client.get(url, params=params, timeout=10.0)
        resp.raise_for_status()
        return resp

    async def _fetch_collection(self) -> None:
        """
        Builds a query url based on the given field and send a series of request
        to the bioRxiv server.
        
        Returns a list of httpx Response objects.
        """
        print("Fetching article list from server...")
        async with httpx.AsyncClient() as client:
            response = await asyncio.gather(
                *[self._get(client, self.root_url, {"page": i}) for i in range(self.n_pages)]
            )
            self.collection_response = response
        print("Done!")

    def _extract_article_urls(self) -> None:
        """Parses a list of response objects to extract the article url."""
        parser = CollectionParser(self.collection_response)
        self.article_urls = parser.extract_data()

    async def _fetch_content(self) -> None:
        """
        Sends a request to fetch data containing the article content. The url
        for each article is stored in the `article_urls` attribute. Response
        objects are stored in `content_response` attribute.
        """
        print("Fetching content for each article...")  
        async with httpx.AsyncClient() as client:
            response = await asyncio.gather(
                *[self._get(client, url) for url in self.article_urls]
            )
            self.content_response = response
        print("Done!")

    def _extract_article_content(self) -> None:
        parser = ContentParser(self.content_response)
        self.data = parser.extract_data()
