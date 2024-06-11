# Jetify Deploy Integrations

This repo contains examples of how to connect your Jetify Cloud services to external databases, caches, and object storage.

There are 3 examples in this repo:

1. Supabase (PostgreSQL)
2. Upstash (Redis/Cache)
3. Amazon S3 (Object Storage)

## Organization

This repo contains two folders at the root level:

1. `devbox-json` shows how to deploy projects using only a devbox.json file
2. `docker` shows how to deploy projects with a custom Dockerfile

## How to Use this Repo

1. Fork this repo to your own Github account
2. Create a new Jetify Cloud account at `cloud.jetify.com`. You will need at least a Solo account to deploy these examples
3. On the Dashboard, select New Project.
4. Connect your Github account to Jetify Cloud
5. On the Import Git Repository screen, select your fork of this repository. You may need to configure your Github access to make the repo accessible if you forked it to a private repository
6. Select the repo, and then enter the path to the project folder that you want to deploy
