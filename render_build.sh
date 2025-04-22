#!/bin/bash
echo "Installing Dependencies"
pip install -r requirements.txt

echo "🧭 Setting Flask environment variables..."
export PYTHONPATH=$(pwd)
export FLASK_APP=wsgi.py
export FLASK_ENV=production

echo "🔥 Running database migrations..."
flask db upgrade

echo "👤 Seeding admin account..."
#python3 -m marine_training_app.scripts.seed_admin

echo "✅ Render build script complete."
