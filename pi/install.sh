#!/bin/bash

sudo apt update

# TODO: replace below shell logic with playbook
# sudo apt install -y software-properties-common
# sudo apt -y install ansible

# ./playbook.yaml
sudo su

gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB

curl -L https://get.rvm.io | bash -s stable --ruby
source /home/pi/.rvm/scripts/rvm

rvm current

gem install bundler

# ubertooth deps
sudo apt-get -y install cmake libusb-1.0-0-dev make gcc g++ libbluetooth-dev \
pkg-config libpcap-dev python-numpy python-pyside python-qt4


# more uberooth tools
wget https://github.com/greatscottgadgets/libbtbb/archive/2018-12-R1.tar.gz -O libbtbb-2018-12-R1.tar.gz
tar -xf libbtbb-2018-12-R1.tar.gz
cd libbtbb-2018-12-R1
mkdir build
cd build
cmake ..
make
make install

# even moar tools
wget https://github.com/greatscottgadgets/ubertooth/releases/download/2018-12-R1/ubertooth-2018-12-R1.tar.xz
tar xf ubertooth-2018-12-R1.tar.xz
cd ubertooth-2018-12-R1/host
mkdir build
cd build
cmake ..
make
make install


# stuff for blueooth & generic
sudo apt-get install -y \
  python-bluez \
  python-dbus \
  sqlite3 \
  bluez-tools \
  ruby-dev \
  bluez \
  bluez-test-scripts \
  python-bluez \
  python-dbus \
  libsqlite3-dev \
  ubertooth \
  git