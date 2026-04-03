#!/usr/bin/env bash
set -euo pipefail

DESTINATION="${DEPLOY_DESTINATION:-kylemcdonald@kylemcdonald.net:/home/kylemcdonald/kylemcdonald.net/}"

npm run build
rsync -avz --delete-delay --exclude-from=deploy/rsync-excludes.txt build/ "$DESTINATION"
