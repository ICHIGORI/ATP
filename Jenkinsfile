pipeline {
    // test new branch for Jenkins user access +1 test
    // Агент может быть любой – Jenkins будет использовать главный сервер
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '30')) // Хранить последние 30 сборок
    }

    stages {
        stage('Get User') {
            steps {
                // Вот так правильно — withBuildUser как шаг
                withBuildUser {
                    script {
                        echo "Build initiated by: ${env.BUILD_USER_ID}"
                    }
                }
            }
        }

        stage('Build Docker image') {
            steps {
                
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