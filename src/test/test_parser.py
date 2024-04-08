from pytest import raises
from parser import MainParser
from api import BiorxivApi
from trees import TREE

class TestParser:
    """Unit tests for the MainParser class."""

    def test_init_without_params(self) -> None:
        """Expect instantiation without paramaters to raise a TypeError."""
        with raises(TypeError) as err:
            MainParser()
        assert err.type is TypeError

    def test_init_with_params(self) -> None:
        """Expect instantiation with paramters to raise no errors."""
        api = BiorxivApi("genetics")
        api.fetch()
        parser = MainParser(api.response, TREE)
        for attr in ["resp", "soup"]:
            assert hasattr(parser, attr)

    def test_extract_articles(self) -> None:
        """Expect to return a list of Article objects with `n` elements."""
        api = BiorxivApi("genetics")
        n = 2
        api.fetch(2)
        parser = MainParser(api.response, TREE)
        articles = parser.data
        assert len(articles) == (n * 10)
