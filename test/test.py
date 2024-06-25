import unittest
import sys
import os

# Add the root directory of your project to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from functions import generate_short_code
from db import conn, cursor


class TestUrlShortener(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.base_url = "http://localhost:5000"

    def test_shorten_url(self):
        original_url = "https://www.youtube.com"
        response = self.app.post(
            "/shorten-url",
            json={"url": original_url},  # Use json instead of data
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 201)
        short_url = response.get_json()["short_url"]
        self.assertIsNotNone(short_url)

        # Extract the short code from the full short URL
        short_code = short_url.split("/")[-1]
        self.assertTrue(len(short_code) >= 5 and len(short_code) <= 10)

    def test_generate_short_code(self):
        length = 7
        short_code = generate_short_code(length)
        self.assertIsNotNone(short_code)
        self.assertEqual(len(short_code), length)

    def test_redirect_to_original(self):
        original_url = "https://www.youtube.com"
        short_code = generate_short_code(6)

        # Insert the short URL into the database
        cursor.execute(
            "INSERT INTO urls (short_url, original_url) VALUES (%s, %s)",
            (short_code, original_url),
        )
        conn.commit()

        response = self.app.get(f"/{short_code}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], original_url)


if __name__ == "__main__":
    unittest.main()
