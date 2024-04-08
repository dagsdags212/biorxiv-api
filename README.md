# biorxiv-api

A command-line interface for retrieving preprint information from bioRxiv.

© Jan Samson (reach out at jegsamson.dev@gmail.com)

## Usage

The `field` argument is the only required parameter. This pertains to the research 
area of interest. Optional flags are listed below.

| Flag     | Alias  | Description                                   |
| -------- | ------ | --------------------------------------------- |
| --pages  | -p     | number of HTML pages to retrieve from server  |
| --count  | -c     | number of articles to display                 |
| --filter | -f     | filter the table by column headers            |


Retrieve the most recent pre-prints in the field of bioinformatics.
```
biorx.py bioinformatics
```

Retrieve article information from the first 5 pages of bioRxiv.
```
biorx.py bioinformatics --pages 5
```

## Todo

- [ ] generate dataclasses for storing article information
    - [x] Author
    - [x] Article
- [ ] command line interface
- [x] create tree object for navigating the HTML/XML document
- [ ] write Enum classes
    - [x] `Collections` to restrict valid request URLs
- [ ] command line parser for providing program arguments
- [ ] write unit tests :(

## User Stories

> I should be able retrieve the most recent biorxiv pre-prints for a given field.

> For each article, I should be able to view its TITLE, AUTHORS, DATE OF PUBLICATION,
> DOI, and ABSTRACT


## Testing Coverage

- BiorxivApi Class
    + initantiation 
    + response attribute
- MainParser class
    + instantiation
    + extracting articles

