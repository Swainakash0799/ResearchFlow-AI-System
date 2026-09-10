from unittest.mock import patch, Mock

from tools import web_search, scrape_url


def test_web_search():
    fake_result = {
        "results": [
            {
                "title": "Test Title",
                "url": "https://example.com",
                "content": "This is test content"
            }
        ]
    }

    with patch("tools.tavily.search", return_value=fake_result):
        result = web_search.invoke("test query")

    assert "Test Title" in result
    assert "https://example.com" in result
    assert "This is test content" in result


def test_scrape_url():
    fake_response = Mock()
    fake_response.text = """
        <html>
            <body>
                <h1>Hello World</h1>
                <p>This is test content.</p>
            </body>
        </html>
    """

    with patch("tools.requests.get", return_value=fake_response):
        result = scrape_url.invoke("https://example.com")

    assert "Hello World" in result
    assert "This is test content." in result


def test_scrape_url_error():
    with patch(
        "tools.requests.get",
        side_effect=Exception("Connection failed")
    ):
        result = scrape_url.invoke("https://example.com")

    assert "Could not scrape URL" in result