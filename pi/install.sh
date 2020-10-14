#!/bin/bash

sudo apt update

sudo apt install -y software-properties-common
sudo apt -y install ansible

./playbook.yaml