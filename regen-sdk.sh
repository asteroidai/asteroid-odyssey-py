#!/usr/bin/env bash
#
# regen-sdk.sh  – keep project layout clean
set -euo pipefail

API_SPEC_URL="https://odyssey.asteroid.ai/api/v1/openapi.yaml"
PKG_NAME="asteroid_odyssey.openapi_client"
GENERATOR_VERSION="latest"
GENERATOR_CLI="@openapitools/openapi-generator-cli@${GENERATOR_VERSION}"
TMP_DIR=".openapi-build"

echo "📦 Ensuring OpenAPI Generator CLI (${GENERATOR_VERSION}) ..."
npx --yes "${GENERATOR_CLI}" version >/dev/null

echo "🧹 Cleaning previous temp directory ..."
rm -rf "${TMP_DIR}"
mkdir -p "${TMP_DIR}"

# 2‑bis. purge stale docs/test inside src
echo "🧹 Removing stale docs/test inside src/ ..."
rm -rf src/docs src/test

echo "⚙️  Generating client into ${TMP_DIR} ..."
npx --yes "${GENERATOR_CLI}" generate \
  -i "${API_SPEC_URL}" \
  -g python \
  -o "${TMP_DIR}" \
  --additional-properties "packageName=${PKG_NAME},projectName=asteroid-odyssey"

echo "🚚 Updating src/asteroid_odyssey/openapi_client ..."
rm -rf src/asteroid_odyssey/openapi_client
mkdir -p src/asteroid_odyssey
mv "${TMP_DIR}/asteroid_odyssey/openapi_client" src/asteroid_odyssey/

echo "🚚 Refreshing top‑level test/ ..."
rm -rf test
mv "${TMP_DIR}/test" ./test

rm openapitools.json

echo "🧹 Removing temporary build directory ..."
rm -rf "${TMP_DIR}"

echo "✅ SDK regenerated and project structure preserved."
