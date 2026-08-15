pipeline {
    agent any

    environment {
        IMAGE_NAME = "shivamdocker28/python-flask-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
    steps {
        bat '''
        "C:\\Users\\91902\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv
        call venv\\Scripts\\activate
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        '''
    }
}

        stage('Run Tests') {
    steps {
        bat '''
        call venv\\Scripts\\activate
        python -m pytest
        '''
    }
}

        stage('Build Docker Image') {
            steps {
                bat '''
                docker build -t %IMAGE_NAME%:%IMAGE_TAG% .
                '''
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

                    bat '''
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    docker push %IMAGE_NAME%:%IMAGE_TAG%
                    docker logout
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}