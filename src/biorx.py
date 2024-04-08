import argparse
from tabulate import tabulate
# custom modules
from api import BiorxivApi
from classes import ArticleTable
from parser import MainParser
from trees import TREE

parser = argparse.ArgumentParser(
    prog="biorx",
    description="A CLI tool for querying prepints hosted in BioRxiv",
)

parser.add_argument("field", type=str)
parser.add_argument("-p", "--pages", type=int)
args = parser.parse_args()

def main() -> None:
    field = args.field.lower()
    n_pages = args.pages if args.pages else 1
    api = BiorxivApi(field)
    if api.fetch(n_pages) <= 200:
        resp = api.response
        parser = MainParser(resp, TREE)
        data = parser.data
        df = ArticleTable(data).to_df()
        table = tabulate(df, tablefmt="pipe", headers="keys", numalign="center")
        print(table)
    else:
        print("Reponse failed, exiting...")
        exit(1)

if __name__ == "__main__":
    main()
