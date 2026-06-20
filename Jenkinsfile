pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirement.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=results.xml
                '''
                junit 'results.xml'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    . venv/bin/activate
                    echo 3 | python3 app.py
                '''
            }
        }
    }
}
