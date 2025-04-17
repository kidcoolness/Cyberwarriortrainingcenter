#!/bin/bash

if [ ! -d "marine_training_app/migrations" ]; then
  echo "⚠️ No migrations folder, initializing..."
  flask db init
  flask db migrate -m "Init"
fi

flask db upgrade
