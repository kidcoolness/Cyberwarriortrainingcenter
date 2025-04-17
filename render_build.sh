#!/usr/bin/env bash

# 🧱 Step 1: Install dependencies
pip install -r requirements.txt

# 🧱 Step 2: Set Flask App context
export FLASK_APP=wsgi.py

# 🧱 Step 3: Run database migrations
flask db upgrade

# 🧱 Step 4 (optional): Seed admin account
python marine_training_app/scripts/seed_admin.py
