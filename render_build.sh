#!/bin/bash
echo "Installing Dependencies"
pip install -r requirements.txt

echo "🧭 Setting Flask environment variables..."
export FLASK_APP=wsgi.py
export FLASK_ENV=production

echo "📂 Ensuring correct working directory..."

echo "🔥 Running database migrations..."
flask db upgrade -d migrations


echo "👤 Seeding admin account..."
python3 -m marine_training_app.scripts.seed_admin

echo "✅ Render build script complete."
