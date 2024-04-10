import sys
import json
from tabulate import tabulate
# custom modules
from biorxiv.api import BiorxivApi
from biorxiv.ArgumentParser import arg_parser, process_args
from biorxiv.classes import ArticleTable

def main() -> None:
    """
    Entry point for the CLI tool. Processes given arguments, instantiates an API
    object, and prints out a filtered table containing article information.
    """
    # parse args into a dictionary
    args = process_args(arg_parser)
    # create api instance
    if args.verbose:
        print("Fetching list of articles...")
    api = BiorxivApi(args.field, args.pages)
    # extract list of articles and store into a dataframe
    if args.verbose:
        print("Extracting article information...")
    article_data = api.data
    # exit program if api retuns an empty list
    if len(article_data) == 0:
        sys.exit(1)
    if args.verbose:
        print("Processing data...")
    df = ArticleTable(article_data).to_df()
    if args.truncate:
        df = df.truncate(args.truncate_start, args.truncate_end)
    # sort table by column if -s flag is passed
    if args.sort:
        df = df.sort_values(args.sort_cols)
    # format DataFrame into a markdown table
    table = tabulate(df, tablefmt="pipe", headers="keys", numalign="center")
    # check display format
    if args.json:
        json_articles = [a.to_json() for a in article_data]
        data = [json.dumps(a) for a in json_articles]
        print(data)
    else:
        print(table)

if __name__ == "__main__":
    main()
