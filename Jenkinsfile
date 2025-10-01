pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t devops-sample-app .'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests... (none added yet)"'
            }
        }
        stage('Push Image') {
            steps {
                sh 'echo "Pushing image to DockerHub (dummy step)"'
            }
        }
        stage('Deploy to K8s') {
            steps {
                sh 'kubectl apply -f k8s-deployment.yaml'
                sh 'kubectl apply -f k8s-service.yaml'
            }
        }
    }
}
