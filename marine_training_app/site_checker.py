import os
import sys
from flask import Flask
from app import create_app  # Adjust based on your app structure
import requests
from urllib.parse import urljoin
import logging

# === SETUP LOGGER ===
log_file = "site_check_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === BOOTSTRAP FLASK APP ===
os.environ["FLASK_ENV"] = "development"
app = create_app()
client = app.test_client()

# === TEST ROUTES ===
def test_routes():
    with app.app_context():
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and "<" not in rule.rule:  # Skip dynamic routes
                try:
                    response = client.get(rule.rule)
                    if response.status_code != 200:
                        logging.error(f"[{response.status_code}] {rule.rule}")
                    else:
                        logging.info(f"[200 OK] {rule.rule}")
                except Exception as e:
                    logging.exception(f"[EXCEPTION] {rule.rule}: {str(e)}")

    print(f"✅ Route check complete. See `{log_file}` for details.")

if __name__ == "__main__":
    test_routes()
