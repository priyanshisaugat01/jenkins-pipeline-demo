pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
        stage('Deploy') {
            steps {
                // Run the game with a sample input
                sh 'echo 3 | python app.py'
            }
        }
    }
}
