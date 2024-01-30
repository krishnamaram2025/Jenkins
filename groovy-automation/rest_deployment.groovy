// import statements
import groovy.json.JsonSlurperClassic

// Declare variables
deployRepo = "https://github.com/devopsmadeeasyorg/Django.git"
deployReponame = "Django"
deployDir = "${deployReponame}/deployments"

// Declarative Pipeline
pipeline {
    // To run job on any available agent
    agent any
    // Environment variables
    environment {
        AWS_ACCESS_KEY_ID = credentials('accesskey')
        AWS_SECRET_ACCESS_KEY = credentials('secretkey')
    }
    // Passing parameters 
    parameters {
        string(name: "BRANCH_NAME", description: "Branch Name", defaultValue: "master")
        string(name: "TARGET_SERVER", description: "SERVER IP", defaultValue: "127.0.0.1")
        string(name: "USERNAME", description: "USER", defaultValue: "")
        string(name: "PASSWORD", description: "PASSWD", defaultValue: "")
    }
    // Stages in execution
    stages{
        // Set up environment
        stage ("Set up environment"){
            steps {
                script {
                    gitClone()
                }
            }
        }
        // REST API deployments
        stage("Execute tasks"){
            steps{
            script {
                sh """
                  export BRANCH_NAME=${BRANCH_NAME}
                  export TARGET_SERVER=${TARGET_SERVER}
                  export USERNAME=${USERNAME}
                  export PASSWORD=${PASSWORD}
                  export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
                  export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
                  cd ${deployDir} && python3 rest_deployment.py
                """
                }
            }
            }
        }
    }

// Clone Git repo
def gitClone(){
    dir(deployReponame) {
        git branch: params.BRANCH_NAME, credentialsId: 'gitcred', url: deployRepo
    }
}