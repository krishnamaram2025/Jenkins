# Jenkins
This project is intended to get hands on CICD tool Jenkins.

# Pre-Requisites
* Step 1: Permissions in visudo
```
jenkins ALL=(ALL) NOPASSWD: ALL
```
* Step 2: Export Env variables
```
export JENKINS_SERVER=http://IP:8080
export JENKINS_USR=
export JENKINS_PWD=
```

# Execution Flow
* Step 1: install wget utility to download packages
```
sudo yum install wget -y
```
* Step 2: install openjdk and set up environment variables 
```
sudo yum install java-11-openjdk-devel -y
```
* Step 3: install Jenkins server 
```
curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo 
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key 
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo 
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
if any issues occured => https://stackoverflow.com/questions/62018771/how-do-i-solve-the-error-public-key-for-jenkins-2-238-1-1-noarch-rpm-is-not-inst
sudo yum install jenkins -y
sudo systemctl start jenkins 
sudo systemctl enable jenkins
```
* Step 4: Login to server and get temp passwd
```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
* Step 5: Access from Browser
```
http://<<PUBLIC_IP>>:8080/
click on Install suggested plugins
```
* Step 6: Pass aws access keys as a Jenkins environment variables
```
Manage Jenkins => Configure System => Global properties => Environemnt variables => add two variables with the below names

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY
```
* Step 7: To create Jenkins job
```
 to create Jenkins Job New item=> create free style project=> general=> Source Code Management : select Git and enter url=> build steps=>

EXECUTABLE STEPS

1.echo pwd

2.export AWS_ACCESS_KEY_ID=”VALUE”

3.export AWS_SECRET_ACCESS_KEY=”VALUE”
```
