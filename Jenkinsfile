pipeline{
    agent any
    stages{
        stage('Clone'){
            steps{
            git branch: 'main', url: 'https://github.com/jithya2003/python_app', credentialsId: '313c6e6e-6646-4ab2-a380-7374ff1959f6'
            }

        }
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t jithyasasmitha/python_app .'
            }
        }
        stage('Scan with Trivy'){
            steps{
                sh 'trivy image --exit-code 1 --severity CRITICAL jithyasasmitha/python_app'
            }
        }
        stage('Push Image'){
            steps{
                sh 'docker push jithyasasmitha/python_app'
            }
        }
        stage('Deploy to Kubernetes'){
            steps{
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }

    }
}
