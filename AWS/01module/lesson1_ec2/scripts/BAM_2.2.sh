#!/bin/bash
set -x
export HOME=/root
dnf install -y git
cd /home/ec2-user
git clone https://github.com/BalericaAI/SEIR-Foundations.git
bash SEIR-Foundations/module1/lesson1_ec2/API/install/install.sh
chown -R ec2-user:ec2-user /home/ec2-user/SEIR-Foundations /opt/balerica-bank
echo "BALERICA USER DATA FINISHED"