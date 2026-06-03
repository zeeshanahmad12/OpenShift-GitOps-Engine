#!/bin/bash
set -e

APP_URL=$1
MAX_RETRIES=10
COUNT=0

echo "Running smoke test on: $APP_URL"

until curl -sf "$APP_URL/health" > /dev/null; do
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_RETRIES ]; then
    echo "FAILED: Health check failed after $MAX_RETRIES retries"
    exit 1
  fi
  echo "Waiting... attempt $COUNT/$MAX_RETRIES"
  sleep 5
done

echo "SUCCESS: App is healthy!"
