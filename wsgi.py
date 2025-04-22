import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from marine_training_app.app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug = True, host="0.0.0.0", port=port)