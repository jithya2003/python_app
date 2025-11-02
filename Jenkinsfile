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
                sh 'docker build -t jithyasasmitha/python_app:dev .'
            }
        }
        stage('Scan with Trivy'){
            steps{
                sh 'trivy image --exit-code 1 --severity CRITICAL jithyasasmitha/python_app:dev'
            }
        }
        stage('Push Image'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'b07850fd-3aa1-4686-833d-e595b1a7297b', 
                                                usernameVariable: 'DOCKER_USER', 
                                                passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push jithyasasmitha/python_app:dev
                        '''
                }
            }
        }
        stage('Deploy to Kubernetes'){
            steps{
                sh 'kubectl apply -f kubernetes/deployment.yaml'
                sh 'kubectl apply -f kubernetes/service.yaml'
            }
        }

    }
}
