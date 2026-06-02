pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
        TEST_REPORT_DIR = 'test-reports'
    }

    stages {
        stage('Setup Environment') {
            steps {
                // Очистка рабочей директории
                cleanWs()
                // Создание виртуального окружения Python
                bat """
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    if exist requirements.txt (
                        pip install -r requirements.txt
                    ) else (
                        echo requirements.txt not found, skipping...
                    )
                """
            }
        }

        stage('Linting') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pip install flake8
                    flake8 . --exit-zero
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    if not exist %TEST_REPORT_DIR% mkdir %TEST_REPORT_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pytest -v --junitxml=%TEST_REPORT_DIR%\\pytest-results.xml
                """
            }
            post {
                always {
                    junit testResults: "${TEST_REPORT_DIR}\\pytest-results.xml"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished on Windows agent.'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}