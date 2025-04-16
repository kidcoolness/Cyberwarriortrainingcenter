#!/bin/bash

# Navigate to app directory if needed
cd marine_training_app

# Run migrations
flask db upgrade

# Start the app
gunicorn run:app
