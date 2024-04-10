from dataclasses import dataclass, field
from typing import Optional
import pandas as pd

@dataclass
class Author:
    """Stores author information."""
    first_name: Optional[str]
    surname: str

    def __post_init__(self) -> None:
        self.first_name = self.first_name.title()
        self.surname = self.surname.title()

    def __str__(self) -> str:
        if self.first_name and self.surname:
            return f"{self.first_name} {self.surname}"
        return ""

    def __repr__(self) -> str:
        if self.first_name and self.surname:
            return f"{self.first_name} {self.surname}"
        return ""

@dataclass
class Article:
    """Stores the metadata for the article content."""
    title: str              = ""
    abstract: str           = ""
    authors: list[Author]   = field(default_factory=list)
    doi_url: str            = ""

    def __post_init__(self) -> None:
        if self.title is None:
            return
        # add a newline for every `chars_per_line` characters
        chars_per_line = 6
        title = ""
        tokens = self.title.split(" ")
        if len(tokens) > chars_per_line:
            for i, t in enumerate(tokens):
                title += f" {t}"
                if (i != 0) and (i % chars_per_line == 0):
                    title += "\n\t"
            self.title = title

    def to_json(self) -> dict[str, str]:
        """Returns a JSON object containing class attributes."""
        return {
            "title": self.title,
            "authors": [str(author) for author in self.authors],
            "url": self.doi_url,
        }

    def to_series(self) -> pd.Series:
        """Returns a pandas Series containing class attributes."""
        first_author = self.authors[0].surname
        d = [self.title, f"{first_author} et al.", self.doi_url]
        index = ["title", "authors", "url"]
        return pd.Series(d, index)

@dataclass
class ArticleTable:
    """Formats article list into a DataFrame."""
    data: list[Article]

    def to_df(self) -> pd.DataFrame:
        """
        Converts each Article object to a pandas Series and concatenates
        each series to return a DataFrame.
        """
        d = [article.to_series() for article in self.data]
        return pd.DataFrame(d)
