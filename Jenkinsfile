pipeline{
    agent any

    triggers {
        cron('H/5 * * * * ')
    }

    stages {
        stage('build') {
            steps {
                sh 'docker build -t maintenance-bot:v1 .'
            }
        }

        stage('run') {
            steps {
                sh 'docker run -v ${WORKSPACE}/logs:/app/logs -e LOG_FILE_PATH=logs/app.log maintenance-bot:v1'
            }
        }
    }
}