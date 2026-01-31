pipeline{
    agent any

    triggers {
        cron('H/5 * * * * ')
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t maintenance-bot:v1 .'
            }
        }

        stage('Generate test data') {
            steps {
                echo 'creating dummy log files for the test...'
                sh 'mkdir -p logs'
                sh 'for i in {1..2000}; do echo "System Critical Error $i" >> logs/app.log; done'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -v ${WORKSPACE}/logs:/app/logs -e LOG_FILE_PATH=logs/app.log maintenance-bot:v1'
            }
        }
    }
}