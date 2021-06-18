#!/usr/bin/env bash

sudo apt-get -y install vsftpd
sudo mv /etc/vsftpd.conf /etc/vsftpd.conf_orig
cat > /etc/vsftpd.conf <<EOF
listen=YES
listen_ipv6=NO
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES
chroot_local_user=YES
secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
ssl_enable=NO
pasv_enable=Yes
pasv_min_port=10000
pasv_max_port=10100
allow_writeable_chroot=YES
EOF

sudo ufw allow from any to any port 20,21,10000:10100 proto tcp
sudo systemctl  start vsftpd
sudo systemctl status vsftpd
sudo useradd -m ftpuser
# sudo passwd ftpuser
sudo bash -c "echo FTP TESTING > /home/ftpuser/FTP-TEST"

