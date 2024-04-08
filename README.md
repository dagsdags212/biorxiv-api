# biorxiv-api

A command-line interface for retrieving preprint information from bioRxiv.

© Jan Samson (reach out at jegsamson.dev@gmail.com)

## Usage

The `field` argument is the only required parameter. This pertains to the research 
area of interest. Optional flags are listed below.

| Flag | Alias | Description |
| --------------- | --------------- | --------------- |
| --count  | -c | limits the number of journals displayed |
| --filter | -f | filter the table by column headers |


Retrieve the most recent pre-prints in the field of bioinformatics.
```
biorx.py bioinformatics
```

Return only the first five articles.
```
biorx.py bioinformatics --count 5
```


## Todo

- [ ] generate dataclasses for storing article information
    - [x] Author
    - [x] Article
- [ ] command line interface
- [x] create tree object for navigating the HTML/XML document
- [ ] write Enum classes
    - [ ] `Collections` to restrict valid request URLs
- [ ] command line parser for providing program arguments
- [ ] write unit tests :(
