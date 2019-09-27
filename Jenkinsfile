def project = 'testproject'
def  appName = 'k8s-sample-application'
def  imageTag = "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"

//https://issues.jenkins-ci.org/browse/JENKINS-51353
pipeline{
  agent {
    kubernetes {
      label 'sampleapp'

      activeDeadlineSeconds 2000
      defaultContainer 'docker'
      yaml """
 
apiVersion: v1
kind: Pod
metadata:
labels:
  component: ci
spec:
  # Use service account that can deploy to all namespaces
  serviceAccountName: jenkins
  volumes:
  - name: docker-sock-volume
    hostPath:
      # location on host
      path: /var/run/docker.sock
      # this field is optional
      type: File
  containers:
  - name: docker
    image: docker
    command:
    - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-sock-volume    
  - name: gcloud
    image: gcr.io/cloud-builders/gcloud
    command:
    - cat
    tty: true
  - name: kubectl
    image: gcr.io/cloud-builders/kubectl
    command:
    - cat
    tty: true
  - name: node
    image: node
    command:
    - cat
    tty: true    
"""
}
}

	environment {
		TESTENV = 'true'
		registry = "gogotechhk/${appName}:${imageTag}"
		registryCredential = "Dockerhub-GGVDEVOPS"
	}

	stages{	  
		stage("build and do the test"){
		
			steps{
				container("node"){
					echo "run node "
					sh "node -v"
					
				}
			}
		}

		stage("Build the image"){
			steps{
				container("docker"){
					script{
						def customImage = docker.build("${env.registry}")
						docker.withRegistry('',registryCredential){
							customImage.push()
						}
					}
				}
			}			
		}

	



	}

	post {

	  success {
	  	echo "This will run if it is successful"
	  }
	  

	



	}
}
