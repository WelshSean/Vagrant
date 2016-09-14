#/usr/bin/bash

# Very basic stuff from raw RHEL7 minimal build to get vagrant up and running
# run as root or via sudo

echo "*** DOnt forget to register with redhat ***"
# Do this manually
# subscription-manager register --username ID --password PW --auto-attach
# sudo subscription-manager attach

yum install git -y
yum install vim -y
sudo subscription-manager repos --enable rhel-7-server-optional-rpms
sudo yum install -y gcc ruby-devel wget
wget https://releases.hashicorp.com/vagrant/1.8.5/vagrant_1.8.5_x86_64.rpm
sudo yum install -y vagrant_1.8.5_x86_64.rpm
yum install gcc make patch  dkms qt libgomp -y
yum install kernel-headers kernel-devel fontforge binutils glibc-headers glibc-devel -y
rpm -Uvh http://download.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-7.noarch.rpm
wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
yun install VirtualBox-5.1 -y
# Almost certainly needs to be updated
export KERN_DIR=/usr/src/kernels/$(rpm -q kernel-devel | sed 's/^kernel-devel-//')
service vboxdrv setup

