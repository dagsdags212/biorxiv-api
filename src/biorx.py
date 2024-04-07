import argparse
from bs4 import BeautifulSoup
from tabulate import tabulate
from classes import Author, Article, ArticleTable
import client
from trees import TREE

parser = argparse.ArgumentParser(
    prog="biorx",
    description="A CLI tool for querying prepints hosted in BioRxiv",
)

parser.add_argument("field")
args = parser.parse_args()

def parse_html(url: str, parser: str="html.parser") -> list[Article]:
    """
    Parses an HTML file into a list of articles.

    Parameters
    ==========
    >>> url: str
    >>> parser: Enum<optional> (default: `html.parser`)
    """
    html = client.fetch_html(url)
    soup = BeautifulSoup(html, parser)
    
    data = []
    # extract the nodes containing pertinent article information
    article_list = soup.select(TREE["article_list"]["root"])
    articles = article_list[0].find_all("li")

    # extract fields for each article
    for article in articles:
        # extract title and doi
        title = article.select(TREE["article_list"]["title"])[0].string
        url = article.select(TREE["article_list"]["doi"])[0].text.rstrip()[5:]
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

def main() -> None:
    url = client.BASE_URL + f"/collection/{args.field.lower()}" 
    data = parse_html(url)
    df = ArticleTable(data).to_df()
    table = tabulate(df, tablefmt="pipe", headers="keys", numalign="center")
    print(table)
    

if __name__ == "__main__":
    main()
