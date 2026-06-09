pipeline {
    //test tuna Блюхера 7
    // Агент может быть любой – Jenkins будет использовать главный сервер
    agent any

    stages {
        stage('Set Build Name') {
            steps {
                wrap([$class: 'BuildUser']) {
                    script {
                        // Выполняем Git-команду, чтобы получить имя автора последнего коммита
                        // Команда: git log -1 --pretty=format:'%an'
                        def authorName = sh(script: "git log -1 --pretty=format:'%an'", returnStdout: true).trim()

                        // Формируем новое имя сборки (например, "Автор - #123")
                        currentBuild.displayName = "${authorName} - #${env.BUILD_NUMBER}"

                        // (Опционально) Можно также установить описание сборки, добавив, например, хеш коммита
                        def commitHash = sh(script: "git log -1 --pretty=format:'%h'", returnStdout: true).trim()
                        currentBuild.description = "Commit: ${commitHash}"
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