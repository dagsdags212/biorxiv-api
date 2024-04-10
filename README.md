# biorxiv-api

A command-line interface for retrieving preprint information from bioRxiv.

© Jan Samson (reach out at jegsamson.dev@gmail.com)

## Usage

The `field` argument is the only required parameter. This pertains to the research 
area of interest. Optional flags are listed below.

| Argument      | Alias  | Description                                   |
| ------------- | ------ | --------------------------------------------- |
| --out         | -o     | filepath to save output                       |
| --pages       | -p     | number of HTML pages to retrieve from server  |
| --truncate    | -t     | subsets a table with a start and end indices  |
| --filter      | -f     | filter the table by column headers            |

Listed below are optional boolean flags:

| Argument      | Description                                           |
| ------------- | ----------------------------------------------------- |
| --no-header   | excludes the column names when writing stdout to file |
| --csv         | writes output to file as csv                          |
| --tsv         | writes ouput to file as tsv                           |
| --json        | writes output to file as json                         |
| --verbose     | print out program messages                            |


Retrieve the most recent pre-prints in the field of bioinformatics.
```
# returns 10 articles by default
biorx.py bioinformatics
```

Retrieve article information from the first 3 pages of bioRxiv.
```
biorx.py bioinformatics --pages 3
```

Display the first five articles.
```
biorx.py bioinformatics --truncate 5
```

Extract all articles between the 8th and 15th articles.
```
biorx.py bioinformatics --pages 2 --truncate 8:15
```

Return the first 8 articles and sort by title.
```
biorx.py bioinformatics --truncate 8 --sort title
```

Display article information as json.
```
biorx.py bioinformatics --json
```

## Todo

- [x] create tree object for navigating the HTML/XML document
- [x] generate dataclasses for storing article information
    - [x] Author
    - [x] Article
- [x] command line parser for providing program arguments
- [x] design command line interface with custom flags
- [x] convert API to client that supports HTTP connection pooling
- [ ] support for stdin, stdout for piping operations 
- [ ] display output as json
- [ ] download full article text to a specified file

## User Stories

> I should be able retrieve the most recent biorxiv pre-prints for a given field.

> For each article, I should be able to view its TITLE, AUTHORS, DATE OF PUBLICATION,
> DOI, and ABSTRACT

