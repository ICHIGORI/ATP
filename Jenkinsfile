pipeline {
    agent any

    environment {
        VENV = '.venv'
        TEST_REPORT_DIR = 'results'   // <-- добавлено
    }

    stages {
        stage('Checkout') {
            steps {
            echo 'Проверка кода в Git ркпозитории...'
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
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat '''
                        if not exist %TEST_REPORT_DIR% mkdir %TEST_REPORT_DIR%
                        call .venv/Scripts/activate.bat
                        pytest --junitxml=%TEST_REPORT_DIR%/pytest.xml --cov=src --cov-report=xml:%TEST_REPORT_DIR%\\coverage.xml
                    '''
                }
            }
        }

        stage('Publish results') {
            steps {
                junit testResults: "${TEST_REPORT_DIR}\\pytest.xml"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            echo 'Тесты завершились с ошибкой!'
        }
        success {
            echo 'Все тесты пройдены успешно!'
        }
    }
}