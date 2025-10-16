from flask import Flask, jsonify
import requests
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CAT_API_URL = "https://catfact.ninja/fact"

@app.route('/me', methods=['GET'])
def get_profile():
    try:
        response = requests.get(CAT_API_URL, timeout=5)
        response.raise_for_status()
        fact_data = response.json()
        cat_fact = fact_data.get("fact", "Cats are awesome!")
    except Exception as e:
        cat_fact = "Could not fetch a cat fact right now."

    data = {
        "status": "success",
        "user": {
            "email": os.getenv("USER_EMAIL"),
            "name": os.getenv("USER_NAME"),
            "stack": os.getenv("USER_STACK")
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True)
