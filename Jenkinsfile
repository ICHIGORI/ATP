pipeline {
    // Агент может быть любой – Jenkins будет использовать главный сервер
    agent any

    stages {
        stage('Set Build Name') {
            steps {
                wrap([$class: 'BuildUser']) {
                    script {
                        // Изменяем имя сборки на "Имя пользователя - #Номер сборки"
                        currentBuild.displayName = "${env.BUILD_USER} - #${env.BUILD_NUMBER}"
                    }
                }
            }
        }
        stage('Build Docker image') {
            steps {
                // Используем bat, потому что это Windows
                bat 'docker build -t my-pytest-tests .'
            }
        }
        stage('Run smoke tests') {
            steps {
                bat 'docker run --rm my-pytest-tests pytest -v -m smoke'
            }
        }
        stage('Run regression tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {
                    bat 'docker run --rm my-pytest-tests pytest -v -m regression'
                }
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