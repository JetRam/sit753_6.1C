pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building with Maven'
            }
        }
        stage('Unit and Integration Tests') {
            steps {
                echo 'Testing with JUnit for unit tests and Selenium for integration tests'
            }
        }
        stage('Code Analysis') {
            steps {
                echo 'Analyzing code with SonarQube'
            }
        }
        stage('Security Scan') {
            steps {
                echo 'Performing security scan with OWASP ZAP'
            }
        }
        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to AWS EC2 staging instance'
            }
        }
        stage('Integration Tests on Staging') {
            steps {
                echo 'Running integration tests on staging environment with Selenium'
            }
        }
        stage('Deploy to Production') {
            steps {
                echo 'Deploying to AWS EC2 production instance'
            }
        }
    }
    post {
        success {
            mail to: 'djethroramos@gmail.com',
                subject: "Success: Pipeline ${currentBuild.fullDisplayName}",
                body: "Pipeline completed successfully."
        }
        failure {
            mail to: 'djethroramos@gmail.com',
                subject: "Failed: Pipeline ${currentBuild.fullDisplayName}",
                body: "Pipeline failed. Please check the Jenkins logs."
        }
    }
}