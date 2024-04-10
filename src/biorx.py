from sys import exit
from tabulate import tabulate
# custom modules
from api import BiorxivApi
from classes import ArticleTable
from ArgumentParser import arg_parser


def main() -> None:
    # parse args into a dictionary
    args = arg_parser.parse_args()
    field = args.field.lower()
    n_pages = args.pages if args.pages else 1
    # create api instance
    api = BiorxivApi(field, n_pages)
    # extract list of articles and store into a dataframe
    article_data = api.data
    # exit program if api retuns an empty list
    if len(article_data) == 0:
        exit(1)
    df = ArticleTable(article_data).to_df()
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
    table = tabulate(df, tablefmt="pipe", headers="keys", numalign="center")
    print(table)

if __name__ == "__main__":
    main()
