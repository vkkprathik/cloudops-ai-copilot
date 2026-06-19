pipeline {
agent any


stages {

    stage('Checkout') {
        steps {
            git branch: 'main',
                url: 'https://github.com/vkkprathik/cloudops-ai-copilot.git'
        }
    }

    stage('Build Docker Images') {
        steps {
            sh 'docker compose build'
        }
    }

    stage('Deploy Application') {
        steps {
            sh 'docker compose down'
            sh 'docker compose up -d'
        }
    }

    stage('Verify Deployment') {
        steps {
            sh 'docker ps'
            sh 'curl -f http://localhost:8000/docs'
        }
    }
}

post {
    success {
        echo 'Deployment Successful!'
    }

    failure {
        echo 'Deployment Failed!'
    }
}


}


