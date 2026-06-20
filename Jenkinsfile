pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirement.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest --junitxml=results.xml'
                junit 'results.xml'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo 3 | python3 app.py'
            }
        }
    }
}
