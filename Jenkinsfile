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
                bat '''
                    python -m venv .venv
                    call .venv/Scripts/activate.bat
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run pytest') {
            steps {
                bat '''
                    call .venv/Scripts/activate.bat
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