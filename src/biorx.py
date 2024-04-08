import argparse
from tabulate import tabulate
import pandas as pd
# custom modules
from api import BiorxivApi
from classes import ArticleTable
from parser import MainParser
from trees import TREE
from ArgumentParser import arg_parser


def main() -> None:
    args = arg_parser.parse_args()
    field = args.field.lower()
    n_pages = args.pages if args.pages else 1
    api = BiorxivApi(field)
    if api.fetch(n_pages) <= 200:
        resp = api.response
        parser = MainParser(resp, TREE)
        data = parser.data
        df = ArticleTable(data).to_df()
        # truncate table if -t flag is passed
        if args.truncate:
            if ":" in args.truncate:
                start, end = args.truncate.split(":")
                start, end = int(start), int(end)
            else:
                start = 1
                end = int(args.truncate)
            df = df.truncate(start, end)
        # sort table by column if -s flag is passed
        if args.sort:
            # sort by multiple columns
            if "," in args.sort:
                columns = [col.lower() for col in args.sort.split(",")]
                df = df.sort_values(columns)
            # sort by a single column
            else:
                df = df.sort_values(args.sort)
        # format and dispaly dataframe
        table = tabulate(df, tablefmt="pipe", headers="keys", numalign="center")
        print(table)
    else:
        print("Reponse failed, exiting...")
        exit(1)

if __name__ == "__main__":
    main()
