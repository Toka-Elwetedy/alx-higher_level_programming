#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

# Open the URL and read the response
with urllib.request.urlopen(url) as response:
    # Read the contents of the response as bytes
    data = response.read()
    # Decode the bytes to a string using the utf-8 encoding
    data = data.decode('utf-8')
    # Print the data
    print(data)
