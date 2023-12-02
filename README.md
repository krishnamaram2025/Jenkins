# Jenkins
This project is intended to get hands on CICD tool Jenkins.

# Pre-Requisites
sudo vi /etc/sudoers. Add line : jenkins ALL=NOPASSWD:/path of script/
Permissions in visudo jenkins ALL=(ALL) NOPASSWD: ALL

# Build AMI using Packer
```
https://github.com/krishnamaram2025/Packer
```
# Create Instance using Terraform
```
https://github.com/krishnamaram2025/Terraform
```
# Install and set up Jenkins server using Ansible
* Step 1: Install Jenkins
```
https://github.com/krishnamaram2025/Ansible
```
* Step 2: Login to server and get temp passwd
```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
* Step 3: Access from Browser
```
http://<<PUBLIC_IP>>:8080/
click on Install suggested plugins
```
* Step 4: Pass aws access keys as a Jenkins environment variables
```
Manage Jenkins => Configure System => Global properties => Environemnt variables => add two variables with the below names

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY
```
* Step 5: To create Jenkins job
```
 to create Jenkins Job New item=> create free style project=> general=> Source Code Management : select Git and enter url=> build steps=>

EXECUTABLE STEPS

1.echo pwd

2.export AWS_ACCESS_KEY_ID=”VALUE”

3.export AWS_SECRET_ACCESS_KEY=”VALUE”
```

* Step 6: Permissions in visudo
```
jenkins ALL=(ALL) NOPASSWD: ALL
```
# Manual: Install and configure software packages for Jenkins
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
sudo yum install jenkins -y
sudo systemctl start jenkins 
sudo systemctl enable jenkins
```

# Manage Jenkins using Python Automation
