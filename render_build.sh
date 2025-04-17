#!/bin/bash

echo "🧭 Setting Flask environment variables..."
export FLASK_APP=wsgi.py
export FLASK_ENV=production

echo "📂 Ensuring correct working directory..."

ls

echo "🔥 Running database migrations..."
flask db upgrade -d migrations


echo "👤 Seeding admin account..."
python3 -m marine_training_app.scripts.seed_admin

echo "✅ Render build script complete."
