pipeline {
    // Агент может быть любой – Jenkins будет использовать главный сервер
    agent any

    stages {
        stage('Build Docker image') {
            steps {
                // Используем bat, потому что это Windows
                bat 'docker build -t my-pytest-tests .'
            }
        }
        stage('Run tests') {
            steps {
                bat 'docker run --rm my-pytest-tests'
            }
        }
        stage('Cleanup') {
            steps {
                // Удаляем образ после тестов, чтобы не занимать место
                bat 'docker rmi my-pytest-tests'
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