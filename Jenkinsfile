pipeline {
    agent any

    environment {
        // Путь к виртуальному окружению
        VENV = '.venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python virtual environment') {
            steps {
                sh '''
                    python -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run pytest') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    pytest --junitxml=results/pytest.xml --cov=src --cov-report=xml:results/coverage.xml
                '''
            }
        }

        stage('Publish results') {
            steps {
                junit 'results/pytest.xml'
                // Для покрытия можно использовать плагин Cobertura
                cobertura coberturaReportFile: 'results/coverage.xml'
            }
        }
    }

    post {
        always {
            // Очистка workspace или виртуального окружения при необходимости
            cleanWs()
        }
        failure {
            echo 'Тесты завершились с ошибкой!'
        }
    }
}