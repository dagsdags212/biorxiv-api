import argparse

arg_parser = argparse.ArgumentParser(
    prog="biorx",
    description="A CLI tool for querying pre-prints hosted in BioRxiv",
)

# parameterized flags
arg_parser.add_argument("field", type=str)
arg_parser.add_argument("-p", "--pages", type=int)
arg_parser.add_argument("-t", "--truncate", type=str)
arg_parser.add_argument("-s", "--sort", type=str)
# boolean flags
arg_parser.add_argument("--json", action="store_true", help="display output as json object")
arg_parser.add_argument("--verbose", action="store_true", help="increases program verbosity")

def process_args(arg_parser: argparse.ArgumentParser) -> dict[str, str]:
    """Runs some checks to validate command line arguments."""
    args = arg_parser.parse_args()
    # convert field to lowercase, no check since it is required
    args.field = args.field.lower()
    # check if --pages flag given, if not default to 1
    args.pages = args.pages if args.pages else 1
    # check if --truncate flag is given
    if args.truncate:
        # start and end indices are give, separated by a colon (:)
        if ":" in args.truncate:
            # split string and map to integers
            start, end = map(int, args.truncate.split(":"))
        # single number provided, set as end index
        else:
            start = 1
            end = int(args.truncate)
        args.truncate_start = start
        args.truncate_end = end

    # check if --sort flag is given to arrange by column value
    if args.sort:
        # multiple columns can be passed which is separated by a comma (,)
        if "," in args.sort:
            # split column names and lowercase
            args.sort_cols =[col.lower() for col in args.sort.split(",")]
        else:
            args.sort_cols = args.sort.lower()
    return args
