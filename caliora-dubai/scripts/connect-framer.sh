#!/usr/bin/env bash
set -euo pipefail

# Connect this cloud/agent environment to a Framer project.
# Usage:
#   FRAMER_PROJECT_ID=xxxx FRAMER_API_KEY=yyyy ./connect-framer.sh
#   ./connect-framer.sh https://framer.com/projects/xxxx

PROJECT_REF="${1:-${FRAMER_PROJECT_ID:-}}"
API_KEY="${FRAMER_API_KEY:-}"

if [[ -z "${PROJECT_REF}" ]]; then
  echo "Missing project. Pass a Framer project URL/ID or set FRAMER_PROJECT_ID."
  exit 1
fi

npx @framer/agent@latest setup >/dev/null

if [[ -n "${API_KEY}" ]]; then
  npx @framer/agent@latest project auth "${PROJECT_REF}" "${API_KEY}"
else
  echo "No FRAMER_API_KEY set — launching browser auth (needs local callback)..."
  npx @framer/agent@latest project auth "${PROJECT_REF}"
fi

echo "Creating session..."
npx @framer/agent@latest session new "${PROJECT_REF}"
