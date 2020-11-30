# DevOpsProject
# Final project DevOps course
# Itamar Aharon

# GUI program for Docker
# The program allows download\delete images and run\stop\delete containers and view all images and containers in a visual interface

### Before running the program must be installed ###

# install python3
sudo apt install python3 python3-pip python3-tk
# install docker
# Download Dependencies
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
# Add Docker’s GPG Key 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Install the Docker Repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# Install Latest Version of Docker  
sudo apt-get install docker-ce
# install SDK docker
pip3 install docker
# Granting permissions   
# Create the docker group. 
sudo groupadd docker 
# Add your user to the docker group.  
sudo usermod -aG docker ${USER}
sudo gpasswd -a $USER docker
newgrp docker
