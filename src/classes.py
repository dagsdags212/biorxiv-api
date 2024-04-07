from dataclasses import dataclass
import pandas as pd

@dataclass
class Author:
    first_name: str
    surname: str

    def __post_init__(self) -> None:
        self.first_name = self.first_name.title()
        self.surname = self.surname.title()

    def __str__(self) -> str:
        return f"{self.first_name} {self.surname}"

    def __repr__(self) -> str:
        return f"{self.first_name} {self.surname}"

@dataclass
class Article:
    title: str
    authors: list[Author]
    url: str

    def __post_init__(self) -> None:
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
            "url": self.url,
        }

    def to_series(self) -> pd.Series:
        """Returns a pandas Series containing class attributes."""
        first_author = str(self.authors[0])
        d = [self.title, f"{first_author} et al.", self.url]
        index = ["title", "authors", "url"]
        return pd.Series(d, index)

@dataclass
class ArticleTable:
    data: list[Article]

    def to_df(self) -> pd.DataFrame:
        """
        Converts each Article object to a pandas Series and concatenates
        each series to return a DataFrame.
        """
        d = [article.to_series() for article in self.data]
        return pd.DataFrame(d)


