import urllib.parse


# URL and Query Helpers

def make_url(base_url, endpoint):
    """Combines a base URL and endpoint into a clean URL"""
    if not base_url: return endpoint or ""
    if not endpoint: return base_url or ""
    return base_url.rstrip("/") + "/" + endpoint.lstrip("/")

def make_query(params):
    """Converts a dictionary of parameters into a URL query string"""
    if not params: return ""
    return urllib.parse.urlencode(params)

def full_url(base_url, endpoint="", params=None):
    """Builds a complete URL with path and query parameters"""
    url = make_url(base_url, endpoint)
    query = make_query(params)
    if query: return url + "?" + query
    return url


# Response Status Code Helpers

def is_success(code):
    """Checks if an HTTP status code indicates success (200 to 299)"""
    return 200 <= code <= 299

def is_client_err(code):
    """Checks if an HTTP status code is a client error (400 to 499)"""
    return 400 <= code <= 499

def is_server_err(code):
    """Checks if an HTTP status code is a server error (500 to 599)"""
    return 500 <= code <= 599

def status_msg(code):
    """Returns a short description string for common HTTP status codes"""
    if code == 200: return "OK"
    if code == 201: return "Created"
    if code == 204: return "No Content"
    if code == 400: return "Bad Request"
    if code == 401: return "Unauthorized"
    if code == 403: return "Forbidden"
    if code == 404: return "Not Found"
    if code == 429: return "Too Many Requests"
    if code == 500: return "Internal Server Error"
    if code == 502: return "Bad Gateway"
    if code == 503: return "Service Unavailable"
    return "Unknown Status"