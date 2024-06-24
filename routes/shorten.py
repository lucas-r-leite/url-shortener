from flask import redirect, request, jsonify, Blueprint

# import uuid
import random
from functions import generate_short_code

shortenerRoute = Blueprint("shortener", __name__)

urls = {}


@shortenerRoute.route("/shorten-url", methods=["POST"])
def url_shortener():
    data = request.get_json()
    original_url = data.get("url")
    if not original_url:
        return jsonify({"error": "url is required"}), 400

    short_code_length = random.randint(5, 10)
    short_code = generate_short_code(short_code_length)

    # short_id = str(uuid.uuid4())[:8]
    urls[short_code] = original_url
    short_url = f"http://localhost:5000/{short_code}"
    return jsonify({"short_url": short_url}), 201


@shortenerRoute.route("/<short_code>")
def redirect_to_original(short_code):
    original_url = urls.get(short_code)
    if not original_url:
        return jsonify({"error": "Invalid short URL"}), 404
    return redirect(original_url)


if __name__ == "__main__":
    shortenerRoute.run(debug=True, port=5000)
