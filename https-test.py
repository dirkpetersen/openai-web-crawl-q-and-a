#! /usr/bin/env python3

import os, sys, requests

# Attempting to access the webpage
url = os.getenv('DOC_URL')
print(f'Trying to connect to {url}')

try:
    response = requests.get(url)
    success = True
    status_code = response.status_code
    content = response.text[:500]  # Displaying only the first 500 characters for brevity
except Exception as e:
    success = False
    error_message = str(e)

# Preparing the result
result = {
    "success": success,
    "status_code": status_code if success else None,
    "content": content if success else None,
    "error_message": error_message if not success else None
}

print(result)

