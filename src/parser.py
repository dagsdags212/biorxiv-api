from httpx import Response
from bs4 import BeautifulSoup
from classes import Author, Article
from trees import COLLECTION_TREE, CONTENT_TREE

class HTMLParser:
    def __init__(self, responses: list[Response]) -> None:
        """
        Base class for HTML parsers. Subclasses are expected to implement the
        `extract_data` method which instructs the class how to parse an HTML
        string from a response object.

        The `tree` object contains a mapping of the field to extract and its
        selector for parsing.

        Parameters
        ==========
        >>> responses (list) : a list of httpx reponse objects containing HTMl data
        >>> ptype (str)      : type of parser to be used
        >>> tree  (dict)     : a JSON object contaning selector paths for parsing
        """
        self.responses = responses
        self.ptype = "html.parser"
        self.soups = []
        # convert reponse text to soup objects
        self._soupify()

    def _soupify(self) -> None:
        """Generates a BeautifulSoup object from an HTML response."""
        for resp in self.responses:
            soup = BeautifulSoup(resp.text, self.ptype)
            self.soups.append(soup)

    def extract_data(self) -> None:
        raise NotImplementedError


class CollectionParser(HTMLParser):
    """
    Parser for reponse objects retrieved from a collection URL.
    A collection URL is specified by the `field` with the following format:

    https://biorxiv.org/collection/{field}

    From each response, the doi URL is extracted from each article. This is 
    the endpoint for collection pertinent article information and metadata.
    """

    def __init__(self, responses: Response) -> None:
        super().__init__(responses)
        self.tree = COLLECTION_TREE

    def extract_data(self) -> None:
        doi_urls = []
        for soup in self.soups:
            url = self._parse_collection(soup)
            doi_urls.extend(url)
        return doi_urls

    def _parse_collection(self, soup) -> None:
        url_list = []
        article_root = soup.select(self.tree["article_list"]["root"])[0]
        for article in article_root.find_all("li"):
            node = article.select(self.tree["article_list"]["doi_url"])
            doi_url = node[0].text.strip()[5:]
            doi = doi_url[16:]
            url = f"https://www.biorxiv.org/content/{doi}v1"
            url_list.append(url)
        return url_list

class ContentParser(HTMLParser):
    def __init__(self, responses: list[Response]) -> None:
        super().__init__(responses)
        self.tree = CONTENT_TREE

    def extract_data(self) -> None:
        articles = []
        for soup in self.soups:
            a = self._parse_article_content(soup)
            articles.append(a)
        return articles

    def _parse_article_content(self, soup):
        root = soup.select(self.tree["root"])[0]
        title = root.select(self.tree["title"])[0].text
        doi_url = root.select(self.tree["doi_url"])[0].text[5:]
        abstract = root.select(self.tree["abstract"])[0].text
        author_list = root.select(self.tree["author_list"]["root"])[0]
        authors = []
        for author_node in author_list.find_all("span", class_="highwire-citation-author"):
            first_name = author_node.select(self.tree["author_list"]["first_name"])[0].string
            surname = author_node.select(self.tree["author_list"]["surname"])[0].string
            authors.append(Author(first_name, surname))
        return Article(title, abstract, authors, doi_url)
