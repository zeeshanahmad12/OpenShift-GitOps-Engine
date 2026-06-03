#!/bin/bash
set -e

IMAGE_TAG=$1
MANIFEST_FILE="k8s/overlays/staging/kustomization.yaml"

if [ -z "$IMAGE_TAG" ]; then
  echo "ERROR: Image tag required"
  exit 1
fi

echo "Updating image tag to: $IMAGE_TAG"
sed -i "s|IMAGE_TAG|${IMAGE_TAG}|g" k8s/base/deployment.yaml

git config user.email "ci@github.com"
git config user.name "CI Bot"
git add k8s/base/deployment.yaml
git commit -m "ci: update image tag to ${IMAGE_TAG}"
git push
