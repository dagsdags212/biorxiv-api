from pytest import raises
from api import BiorxivApi

class TestBiorxivApi:
    """Unit tests for the BiorxivApi class."""

    def test_init_without_field(self):
        """
        Expect to raise an error when class is initialized with empty
        `field` parameter.
        """
        with raises(TypeError) as err:
            BiorxivApi()
        assert err.type is TypeError

    def test_init_with_field(self):
        """
        Expect to generate a class instance with the attributes `BASE_URL`,
        `field`, `url`, and `response`.
        """
        field = "bioinformatics"
        api = BiorxivApi(field)
        for attr in ["BASE_URL", "field", "url", "response"]:
            assert hasattr(api, attr)

    def test_response(self) -> None:
        """Expect the class instance to contain a Response object."""
        from requests import Response
        field = "bioinformatics"
        api = BiorxivApi(field)
        api.fetch()
        resp = api.response
        assert isinstance(resp, Response)
        assert hasattr(resp, "text")

