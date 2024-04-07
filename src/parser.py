from requests import Response
from bs4 import BeautifulSoup
from classes import Author, Article

class HTMLParser:
    def __init__(self, tree: dict=None) -> None:
        """
        Parameters
        ==========
        >>> ptype (str) : type of parser to be used
        >>> tree  (dict): a JSON object contaning selector paths for parsing
        """
        self.ptype = "html.parser" 
        self.tree = tree

class MainParser(HTMLParser):
    def __init__(self, resp: Response, tree) -> None:
        super().__init__(tree)
        self.resp = resp
        self.soup = None
        self._generate_soup()

    def _generate_soup(self) -> None:
        """Generates a BS4 object from the response body."""
        html = self.resp.text
        soup = BeautifulSoup(html, self.ptype)
        self.soup = soup

    def extract_articles(self, n: int=10):
        """
        Extracts `n` articles from the stored soup object.
        Returns a list of Articles.
        """
        TREE = self.tree
        soup = self.soup
        data = []
        # extract the nodes containing pertinent article information
        article_list = soup.select(TREE["article_list"]["root"])
        articles = article_list[0].find_all("li")[:n]
        # extract fields for each article
        for article in articles:
            # extract title and doi
            title = article.select(TREE["article_list"]["title"])[0].text
            url = article.select(TREE["article_list"]["doi"])[0].text.strip()[5:]
            # extract list of authors
            author_list = article.select(TREE["article_list"]["author_list"]["root"])[0]
            authors = []
            for author_node in author_list.find_all("span", class_="highwire-citation-author"):
                first_name = author_node.select(TREE["article_list"]["author_list"]["first_name"])[0].string
                surname = author_node.select(TREE["article_list"]["author_list"]["surname"])[0].string
                author = Author(first_name, surname)
                authors.append(author)
            # store data in an Article object
            article = Article(title, authors, url)
            data.append(article)

        return data

   
