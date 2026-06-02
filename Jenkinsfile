pipeline {
    // 1. Указываем, где выполнять сборку. 'any' - на любом доступном агенте Jenkins.
    agent any

    // 2. Определяем этапы (stages) нашего конвейера
    stages {
        stage('Checkout & Info') {
            steps {
                // Jenkins сам клонирует репозиторий, но мы добавим информативный вывод.
                script {
                    // Выводим имя ветки, которую сейчас собираем
                    def branchName = env.BRANCH_NAME
                    echo "Сборка для ветки: ${branchName}"
                }
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Установка Python и зависимостей...'
                // Эти команды выполняются для каждой ветки в отдельном workspace
                bat '''
                    REM Проверка версии Python (должна быть в PATH на Jenkins-агенте)
                    python --version

                    REM Создание виртуального окружения (опционально, но рекомендуется)
                    python -m venv venv

                    REM Активация окружения и установка зависимостей
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                echo 'Запуск тестов...'
                bat '''
                    call venv\\Scripts\\activate
                    REM Команда для запуска pytest.
                    REM --maxfail=1 остановит прогон после первого упавшего теста
                    REM --tb=short сделает вывод ошибок более кратким
                    REM --junitxml=report.xml создаст отчёт в формате JUnit для Jenkins
                    pytest --maxfail=1 --tb=short --junitxml=report.xml
                '''
            }
        }

        stage('Publish Reports') {
            steps {
                echo 'Публикация отчёта о тестировании...'
                // Публикуем XML-отчёт, созданный pytest
                junit 'report.xml'
            }
        }
    }

    // 3. Блок, который выполняется в конце всегда, вне зависимости от результата
    post {
        success {
            echo 'Поздравляю! Все тесты для этой ветки прошли успешно.'
        }
        failure {
            echo 'В этой ветке есть падающие тесты. Пожалуйста, проверьте консоль.'
        }
        always {
            echo 'Работа пайплайна завершена.'
            cleanWs() // Опционально: удаляет временные файлы сборки, чтобы сэкономить место
        }
    }
}