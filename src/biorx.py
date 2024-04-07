import argparse
from bs4 import BeautifulSoup
from tabulate import tabulate
# custom modules
from api import BiorxivApi
from classes import Author, Article, ArticleTable
from parser import HTMLParser, MainParser
from trees import TREE

parser = argparse.ArgumentParser(
    prog="biorx",
    description="A CLI tool for querying prepints hosted in BioRxiv",
)

parser.add_argument("field", type=str)
parser.add_argument("-c", "--count", type=int)
args = parser.parse_args()

def main() -> None:
    field = args.field.lower()
    count = args.count if args.count else 10
    api = BiorxivApi(field)
    if api.fetch() <= 200:
        resp = api.response
        parser = MainParser(resp, TREE)
        data = parser.extract_articles(count)
        df = ArticleTable(data).to_df()
        table = tabulate(df, tablefmt="pipe", headers="keys", numalign="center")
        print(table)
    else:
        print("Reponse failed, exiting...")
        exit(1)

if __name__ == "__main__":
    main()
