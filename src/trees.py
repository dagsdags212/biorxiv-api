"""
Trees represent the hierarchical structure of an HTML file. Each key is a node
and the corresponding value is a selector for extracting field information.

TREE        : for parsing article metadata from a collection
CONTENT_TREE: for parsing the content of an article
URL_TREE    : represents bioRxiv endpoints
"""

COLLECTION_TREE = {
    "article_list": {
        "root": "div.highwire-article-citation-list div.highwire-list ul",
        "doi_url": "div.highwire-cite-metadata span.highwire-cite-metadata-doi",
    }
}

CONTENT_TREE = {
    "root": "div#block-system-main div.content div.main-content-wrapper div.inside",
    "title": "h1#page-title",
    "doi_url": "div.highwire-cite-metadata span.highwire-cite-metadata-doi",
    "abstract": "div.abstract p",
    "author_list": {
        "root": "div.highwire-cite-authors",
        "first_name": "span.nlm-given-names",
        "surname": "span.nlm-surname"
    }
}


URL_TREE = {
    "root": "https://www.biorxiv.org",
    "collection": "https://www.biorxiv.org/collection",
    "content": "https://www.biorxiv.org/content"
}
