pipeline {
  agent any
  environment {
    ENV = DEV
  }
  stages {
    stage('Build Docker Image') {
      steps {
        script {
          docker.withRegistry('https://registry.hub.docker.com', 'docker_creds') {
            docker.Build('kamalk8s/demo-api:1.0.2')
        }
      }
      }
    }
  }
}