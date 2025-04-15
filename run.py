import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from marine_training_app.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
