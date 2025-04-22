import sys
import os
from marine_training_app.app.utils import natural_key
from marine_training_app.app import create_app

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = create_app()

app.jinja_env.globals['natural_key'] = natural_key

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)