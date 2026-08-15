pipeline {
    agent any

    environment {
        IMAGE_NAME = "shivamdocker28/python-flask-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
        PYTHON = "C:\\Users\\91902\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
    }

    stages {

        stage('Create Virtual Environment') {
            steps {
                bat """
                "%PYTHON%" -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                call venv\\Scripts\\activate
                python -m pytest
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                docker build -t %IMAGE_NAME%:%IMAGE_TAG% .
                docker tag %IMAGE_NAME%:%IMAGE_TAG% %IMAGE_NAME%:latest
                """
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat """
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    docker push %IMAGE_NAME%:%IMAGE_TAG%
                    docker push %IMAGE_NAME%:latest
                    docker logout
                    """
                }
            }
        }
    }

    post {
        success {
            echo '======================================'
            echo 'Pipeline completed successfully!'
            echo "Docker Image: ${IMAGE_NAME}:${IMAGE_TAG}"
            echo "Docker Image: ${IMAGE_NAME}:latest"
            echo '======================================'
        }

        failure {
            echo 'Pipeline failed. Check the console output for details.'
        }

        always {
            cleanWs()
        }
    }
}