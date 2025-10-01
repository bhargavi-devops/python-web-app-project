# DevOps Sample Project

## Overview
This is a Python Flask app deployed using Docker, Jenkins, and Kubernetes.

### Steps:
1. Build Docker image:
   docker build -t devops-sample-app .

2. Run locally:
   docker run -p 5000:5000 devops-sample-app

3. Jenkins pipeline:
   - Build & push image
   - Deploy to Kubernetes

4. Kubernetes deployment:
   kubectl apply -f k8s-deployment.yaml
   kubectl apply -f k8s-service.yaml

App will be available at http://<minikube-ip>:80
