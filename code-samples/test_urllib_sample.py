from urllib.parse import unquote

def test_urllib_sample():
    encoded_url = "https%3A%2F%2Fexample.com%2Fpath%3Fquery%3Dvalue"
    decoded_url = unquote(encoded_url)
    print(decoded_url)  # Output: https://example.com/path?query=value
