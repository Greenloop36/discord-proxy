"""

    Discord API Proxy
    28/07/2025

"""


## Imports
from rich import print
from rich.console import Console

from flask import Flask, request
from markupsafe import escape
import requests

## API
app = Flask(__name__)
console = Console()

@app.route('/api/webhooks/<string:webhook_id>/<string:webhook_token>', methods=['POST'])
def webhook_proxy(id: str, token: str):
    url: str = f"https://discord.com/api/webhooks/{id}/{token}"
    body: dict = request.get_json()

    try:
        response = requests.post(url, body)
        response.raise_for_status()
    except requests.HTTPError:
        return response.text, response.status_code
    except Exception as e:
        console.print_exception(show_locals=True)
        return "Internal Error", 500
    else:
        return "OK", 200


if __name__ == "__main__":
    app.run()
