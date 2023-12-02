# Jenkins
This project is intended to get hands on CICD tool Jenkins.

# Pre-Requisites
sudo vi /etc/sudoers. Add line : jenkins ALL=NOPASSWD:/path of script/
Permissions in visudo jenkins ALL=(ALL) NOPASSWD: ALL

# Build AMI using Packer

# Create Instance using Terraform

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


# Install and set up Jenkins server using Ansible
```
git clone https://github.com/krishnamaram2025/Jenkins.git && cd Jenkins && ansible-playbook ansible jenkins.yml
```
# Manage Jenkins using Python Automation
