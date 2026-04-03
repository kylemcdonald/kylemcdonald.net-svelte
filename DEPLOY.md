# Deployment

This repo is the source of truth for the public homepage and the legacy assets
kept under `static/`.

- GitHub Actions builds the site on pushes to `main`.
- The server only receives flat files from `build/`.
- Root redirects and access rules live in `static/.htaccess`.
- Server-only legacy paths that should survive deploys live in `deploy/rsync-excludes.txt`.

Required GitHub secret:

- `DEPLOY_SSH_KEY`: private SSH key that can write to `kylemcdonald@ssh.kylemcdonald.net`
