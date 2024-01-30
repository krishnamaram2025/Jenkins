// import statements
import jenkins.model.*
import com.cloudbees.plugins.credentials.CredentialsStore
import com.cloudbees.plugins.credentials.SystemCredentialsProvider
import com.cloudbees.plugins.credentials.SystemCredentialsProvider.StoreImpl
import com.cloudbees.plugins.credentials.*
import com.cloudbees.plugins.credentials.common.*
import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.plugins.credentials.impl.*
import com.cloudbees.plugins.plaincredentials.*
import com.cloudbees.plugins.plaincredentials.impl.*
import hudson.util.Secret

// Declare variables
deployRepo = "https://github.com/fullstack2025/keys-rotation.git"
deployReponame = "keys-rotation"

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
        string(name: "BRANCH_NAME", description: "branch name", defaultValue: "dev")
    }
    // Stages in execution
    stages{
        // Set up environment
        stage ("Set up environment"){
            steps {
                script {
                    gitClone()
                    // sh """
                    // export access_key=${AWS_ACCESS_KEY_ID}
                    // export secret_key=${AWS_SECRET_ACCESS_KEY}
                    // /pip3 install -r requirements.txt
                    // python3 aws_automation/accesskeys_rotation.py
                    // """
                }
            }
        }
        // keys rotation
        stage("Keys rotation"){
            steps{
            script {
                try{
                    println "-------Started access keys rotation ------"
                    def secret_data = sh(script: 'export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID};export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY};python3 aws_automation/accesskeys_rotation.py createaccesskey', returnStdout: true)
                    if(secret_data !=""){
                        accesskey = secret_data.split(':')[0]
                        secretkey = secret_data.split(':')[1]
                        update_access_key(accesskey)
                        update_secret_key(secretkey)
                        println "--------------Started deleting old access keys--------------"
                        // def delete_secret_data = sh(script: 'export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID};export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY};python3 aws_automation/accesskeys_rotation.py deleteaccesskey', returnStdout: true)
                        println "--------------Successfully deleted old access keys--------------"
                    }
                
                    else{
                        println "--------------Skipped rotating access keys--------------"
                    }
                }
                catch(Exception e){
                    println("Exception while creating acess key: ${e}")
                    }
                }
                
            }
            }
        }
    }



// Groovy script

// Clone Git repo
def gitClone(){
    dir(deployReponame) {
        git branch: params.BRANCH_NAME, credentialsId: 'gitcred', url: deployRepo
    }
}

// Update Access key in Jenkins server
@NonCPS
def update_access_key(key){
    try{
        domain = Domain.global()
        def store = Jenkins.instance.getExtentionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()
        // oldaccesskey = new StringCredentialsImpl(
        //     CredentialsScope.GLOBAL, 
        //     "accesskey", 
        //     "accesskeydesc", 
        //     null)
        // newaccesskey = new StringCredentialsImpl(
        //     CredentialsScope.GLOBAL, 
        //     "accesskey", 
        //     "accesskeydesc", 
        //     Secret.fromString(key))
        // store.updateCredentials(domain, oldaccesskey, newaccesskey)

    }
    catch(Exception e){
        println("Exception while updating acess key: ${e}")
    }
}

// Update Secret key in Jenkins server
@NonCPS
def update_secret_key(key){
    try{
        domain = Domain.global()
        def store = Jenkins.instance.getExtentionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()
        // oldsecretkey = new StringCredentialsImpl(CredentialsScope.GLOBAL, "secretkey", "secretkeydesc", null)
        // newsecretkey = new StringCredentialsImpl(CredentialsScope.GLOBAL, "secretkey", "secretkeydesc", Secret.fromString(key))
        // store.updateCredentials(domain, oldsecretkey, newsecretkey)
    }
    catch(Exception e){
        println("Exception while updating acess key: ${e}")
    }
}
