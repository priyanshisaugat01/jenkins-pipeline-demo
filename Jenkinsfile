pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install --break-system-packages -r requirement.txt'
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
