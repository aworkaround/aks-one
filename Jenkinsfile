pipeline {
  agent any
  environment {
    ENV='DEV'
  }
  stages {
    stage ('Build') {
      agent any
      steps {
        echo "Builing release for ${ENV} environment."
        script {
          docker login --username docker.com/kamalk8s --password "\$(echo \$DOCKER_ACCESS_TOKEN)"
          docker build --tag "kamalk8s/demo-api:1.0.1" "./app/microservices/api"
          docker push "kamalk8s/demo-api:1.0.1"
        }
      }
    }
    stage ('Success') {
      agent any
      steps {
        echo "Success Printed."
      }
    }
  }
}