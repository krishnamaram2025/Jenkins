# Project Title

Jenkins is used for Continuous Integration/Continuous Delivery/Continuous Deployment purpose

Jenkins installation and Set up
=====================================

https://linuxize.com/post/how-to-install-jenkins-on-centos-7/


Step 1: install openjdk and set up environment variables
$sudo yum install java-1.8.0-openjdk-devel

Step 2: install Jenkins server
$curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo

$sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key

$sudo yum install jenkins

$sudo systemctl start jenkins

$sudo systemctl enable jenkins

Step 3: configure jenkins job to build and deploy war file




Automation Installation 
==============================

$yum update -y && yum upgrade -y

$yum install git -y && yum install wget -y && yum install unzip -y && yum install curl -y

$yum install ansible -y

Set up
==============

Step 1: switch to root user

sudo su -l

passwd root

step 2: enable password authentication

vi /etc/ssh/sshd_config

PasswordAuthentication yes

permitroorlogin yes

systemctl restart sshd

step 3: generate ssh keys for key based authentication

ssh-keygen

ssh-copy-id root@localhost


Execution Flow
=======================
step 1: clone repo

$git clone https://github.com/krishnamaram2/Configuration_Manager.git

Step 2:

$cd Configuration_Manager/src

$ansible-playbook -i hosts jenkins.yml







Plugins
1.Role Strategy Plugin
2.Folder plugin
3.Github pull request builder plugin

Trigger builds automatically on GitHub pull request
1.Using GitHub webhooks      + GitHub pull request builder plugin


Configuring  Jenkins job


New Item => Folder = project name=>configure- Folder = team name=>configure-user-username=>configure-job templete = job name
1.General
     Discard old builds =>
            strategy =Log rotation
            max# of builds to keep = 20
2.Job Notifications
     This project is parameterized =>=>
              String parameter
                                       name = aws_region
                                        value = us-east-1
     Restrict where this project can be run
            Label expression = Jenkins slave node
3.Source code management
  Git =>
     respositories => url
4.Build triggers
5.Build environment
     delete workspace before build starts
6.Bindings
    secret text => 
                 variable = git api token,aws acces key, aws secret key,artifactory credentials, docker api keys
                credentials=
 7.Build
    Docker build and publish =>
         Docker registry uri =     
         repository name = 
    Execute shell =>
                  command = docker run
8.Postbuild actions





Jenkinsfile

node("LINUX'){
        stages(){
         stage('SCM'){
       //git clone
         git "https://github.com/krishnamaram4/test.git
                            }
           stage("Build the package'){
        // packaging
        sh 'mvn package'
            }
            stage('Archival'){
         //Archiving artifacts
        archive 'target/*.war'
               }
              }
              }
1.How to give permissions in Jenkins?
Roles=>
Browse,administer,builder,develop,manage
Group=>
     iot_software_platform
Membership=>
2.What is build executor 
Build executor is a number of jobs that can be executed parallelly

3.what is  Build periodically vs Poll SCM
Build periodically builds the project periodically even though no changes are made
Poll SCM => periodically polls the SCM to check whether new commits pushed since the last build
