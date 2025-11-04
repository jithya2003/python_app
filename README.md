# python_app
**Hello from Python App - CI/CD is success and successfully deployed!**

---

## Project Overview

This project demonstrates:

- Building a Python Flask app
- Dockerizing the application
- CI/CD with Jenkins pipeline
- Scanning Docker images using Trivy
- Deploying to Kubernetes (K3s cluster)

---

## Features

- Flask app running on port 5000
- CI/CD pipeline triggered on GitHub push
- Automated Docker build and push to Docker Hub
- Kubernetes deployment with NodePort service
- Prometheus and Grafana monitoring support
---

## Pipeline Stages

1. **Clone**: Pull source code from GitHub
2. **Build Docker Image**: Build `python_app:dev`
3. **Scan with Trivy**: Security scan for CRITICAL vulnerabilities
4. **Push Image**: Push image to Docker Hub using personal access token
5. **Deploy to Kubernetes**: Apply `deployment.yaml` and `service.yaml`

---

## Deployment

**Kubernetes Service:**

```bash
kubectl get all
