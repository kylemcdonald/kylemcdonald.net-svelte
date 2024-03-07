#!/usr/bin/env bash
npm run build
rsync -avz build/ kylemcdonald@kylemcdonald.net:/home/kylemcdonald/kylemcdonald.net