from requests.utils import unquote

encoded_url = "https://example.com/path%3Fquery%3Dvalue%26id%3D123"
decoded_url = unquote(encoded_url)
print(decoded_url)  # Output: https://example.com/path?query=value&id=123
