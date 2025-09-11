#!/usr/bin/env bash
#
# regen-sdk.sh  – keep project layout clean
set -euo pipefail

# Define arrays of OpenAPI spec URLs and corresponding package names.
# Each PKG name can be either the full form (e.g. "asteroid_odyssey.openapi_client")
# or just the module part (e.g. "openapi_client"). In the latter case it will be
# prefixed with "asteroid_odyssey." automatically.
API_SPEC_URLS=(
  "https://odyssey.asteroid.ai/api/v1/openapi.yaml"
  "https://odyssey.asteroid.ai/agents/v2/openapi.yaml"
)
PKG_NAMES=(
  "asteroid_odyssey.agents_v1_gen"
  "asteroid_odyssey.agents_v2_gen"
)

GENERATOR_VERSION="v2.23.1"
GENERATOR_CLI="@openapitools/openapi-generator-cli@${GENERATOR_VERSION}"
TMP_DIR=".openapi-build"

echo "📦 Ensuring OpenAPI Generator CLI (${GENERATOR_VERSION}) ..."
npx --yes "${GENERATOR_CLI}" version >/dev/null

# Validate arrays are aligned
if [ ${#API_SPEC_URLS[@]} -ne ${#PKG_NAMES[@]} ]; then
  echo "❌ API_SPEC_URLS and PKG_NAMES must have the same length" >&2
  exit 1
fi

echo "🧹 Cleaning previous temp directory ..."
rm -rf "${TMP_DIR}"
mkdir -p "${TMP_DIR}"

# purge stale docs/test inside src
echo "🧹 Removing stale docs/test inside src/ ..."
rm -rf src/docs src/test

# Prepare top-level targets
mkdir -p src/asteroid_odyssey
rm -rf test
mkdir -p test

# Generate for each pair
for i in "${!API_SPEC_URLS[@]}"; do
  API_SPEC_URL="${API_SPEC_URLS[$i]}"
  PKG_NAME_RAW="${PKG_NAMES[$i]}"

  # Normalize package name to full form asteroid_odyssey.X
  if [[ "${PKG_NAME_RAW}" == asteroid_odyssey.* ]]; then
    PKG_NAME="${PKG_NAME_RAW}"
  else
    PKG_NAME="asteroid_odyssey.${PKG_NAME_RAW}"
  fi

  PKG_MODULE="${PKG_NAME#asteroid_odyssey.}"
  GEN_DIR="${TMP_DIR}/gen_${i}"

  echo "⚙️  Generating ${PKG_NAME} from ${API_SPEC_URL} into ${GEN_DIR} ..."
  npx --yes "${GENERATOR_CLI}" generate \
    -i "${API_SPEC_URL}" \
    -g python \
    -o "${GEN_DIR}" \
    --additional-properties "packageName=${PKG_NAME},projectName=asteroid-odyssey" \
    --skip-validate-spec

  echo "🚚 Updating src/asteroid_odyssey/${PKG_MODULE} ..."
  rm -rf "src/asteroid_odyssey/${PKG_MODULE}"
  mkdir -p src/asteroid_odyssey
  mv "${GEN_DIR}/asteroid_odyssey/${PKG_MODULE}" src/asteroid_odyssey/

  echo "🧪 Organizing tests for ${PKG_MODULE} ..."
  rm -rf "test/${PKG_MODULE}"
  if [ -d "${GEN_DIR}/test" ]; then
    mkdir -p test
    mv "${GEN_DIR}/test" "test/${PKG_MODULE}"
  fi
done

# rm -f openapitools.json || true  # Keep openapitools.json to pin generator version

echo "🧹 Removing temporary build directory ..."
rm -rf "${TMP_DIR}"

echo "✅ SDK(s) regenerated and project structure preserved."
