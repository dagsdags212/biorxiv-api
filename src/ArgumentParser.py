import argparse

arg_parser = argparse.ArgumentParser(
    prog="biorx",
    description="A CLI tool for querying prepints hosted in BioRxiv",
)

arg_parser.add_argument("field", type=str)
arg_parser.add_argument("-p", "--pages", type=int)
arg_parser.add_argument("-t", "--truncate", type=str)
arg_parser.add_argument("-s", "--sort", type=str)


