from flask import redirect, request, jsonify, Blueprint
import random
from functions import generate_short_code
from db import conn, cursor

shortenerRoute = Blueprint("shortener", __name__)


@shortenerRoute.route("/shorten-url", methods=["POST"])
def url_shortener():
    data = request.get_json()
    original_url = data.get("url")
    if not original_url:
        return jsonify({"error": "url is required"}), 400

    short_url_length = random.randint(5, 10)
    short_url = generate_short_code(short_url_length)

    cursor.execute(
        "INSERT INTO urls (short_url, original_url) VALUES (%s, %s)",
        (short_url, original_url),
    )
    conn.commit()

    short_url = f"http://localhost:5000/{short_url}"
    return jsonify({"short_url": short_url}), 201


@shortenerRoute.route("/<short_url>")
def redirect_to_original(short_url):
    cursor.execute(
        "SELECT original_url FROM urls WHERE short_url = %s", (short_url,))
    result = cursor.fetchone()
    if result:
        original_url = result[0]
        return redirect(original_url)
    else:
        return jsonify({"error": "Invalid short URL"}), 404


if __name__ == "__main__":
    shortenerRoute.run(debug=True, port=5000)
