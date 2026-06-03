#!/bin/bash
set -e

PREVIOUS_TAG=$1

if [ -z "$PREVIOUS_TAG" ]; then
  echo "ERROR: Previous image tag required"
  exit 1
fi

echo "Rolling back to: $PREVIOUS_TAG"
sed -i "s|IMAGE_TAG|${PREVIOUS_TAG}|g" k8s/base/deployment.yaml

git config user.email "ci@github.com"
git config user.name "CI Bot"
git add k8s/base/deployment.yaml
git commit -m "rollback: revert to ${PREVIOUS_TAG}"
git push
echo "Rollback complete!"
