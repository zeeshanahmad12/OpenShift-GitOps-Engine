#!/bin/bash
set -e

IMAGE_TAG=$1

if [ -z "$IMAGE_TAG" ]; then
  echo "ERROR: Image tag required"
  exit 1
fi

echo "Updating image tag to: $IMAGE_TAG"
sed -i "s|python-webapp:.*|python-webapp:${IMAGE_TAG}|g" k8s/base/deployment.yaml

git config user.email "ci@github.com"
git config user.name "CI Bot"
git remote set-url origin "https://x-access-token:${GITHUB_TOKEN}@github.com/zeeshanahmad12/OpenShift-GitOps-Engine.git"
git add k8s/base/deployment.yaml

if git diff --cached --quiet; then
  echo "No changes to commit — same image tag"
  exit 0
fi

git commit -m "ci: update image tag to ${IMAGE_TAG}"
git push
