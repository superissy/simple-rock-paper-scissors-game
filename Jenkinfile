
pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('d4506f04-b98c-47db-95ce-018ceac27ba6')
        SCANNER_HOME = tool 'sonar-scanner'
        IMAGE_NAME = 'idrisniyi94/devopsfullstack-site'
        IMAGE_TAG = "v.0.0.${BUILD_NUMBER}"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/superissy/simple-rock-paper-scissors-game.git'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=devopsfullstack-site -Dsonar.projectName=devopsfullstack-site"
                }
            }
        }
        stage('Quality Gate') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    waitForQualityGate abortPipeline: false, credentialsId: 'sonar-token'
                }
            }
        }
        // stage('Owasp Dependency Check') {
        //     steps {
        //         dependencyCheck additionalArguments: '--scan ./ --disableYarnAudit --disableNodeAudit --nvdApiKey 4bdf4acc-8eae-45c1-bfc4-844d549be812', odcInstallation: 'DP-Check'
        //         dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
        //     }
        // }
        stage('Trivy FS Scan') {
            steps {
                script {
                    sh "trivy fs . --exit-code 0"
                }
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
                    echo "Docker Build Completed"
                }
            }
        }
        stage('Trivy Docker Scan') {
            steps {
                script {
                    sh "trivy image $IMAGE_NAME:$IMAGE_TAG --exit-code 0"
                }
            }
        }
        stage('Docker Push') {
            steps {
                script {
                    sh "docker push $IMAGE_NAME:$IMAGE_TAG"
                    echo "Docker Push Completed"
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    def containerName = "devopsfullstack-site"
                    def isRunning = sh(script: "docker ps -a | grep ${containerName}", returnStatus: true)
                    if (isRunning == 0) {
                        sh "docker stop ${containerName}"
                        sh "docker rm ${containerName}"
                        echo "Stopped and Removed existing container"
                        echo "Deploying new container"
                        dir("terraform") {
                            sh "terraform init"
                            sh "terraform apply -auto-approve -var 'image_name=${IMAGE_NAME}' -var 'image_tag=${IMAGE_TAG}' -var 'container_name=${containerName}' -var external_port=8769"
                        }
                    }
                    else {
                        dir("terraform") {
                            sh "terraform init"
                            sh "terraform apply -auto-approve -var 'image_name=${IMAGE_NAME}' -var 'image_tag=${IMAGE_TAG}' -var 'container_name=${containerName}' -var external_port=8769"
                        }
                    }
                }
            }
        }
    }
}
