# simple-docker-ci-app
Simple Flask app with Docker and GitHub Actions CI/CD
# Simple Docker CI App

This repository contains a simple Flask web application that runs inside a Docker container.

## Features

- Dockerfile for local development
- CI/CD using GitHub Actions
- Automatic Docker image build
- Image publishing to Docker Hub
- Automatic deployment to Railway or Fly.io (free-tier)

## How to run locally

```bash
docker build -t myapp .
docker run -p 5000:5000 myapp
