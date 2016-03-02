git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
gpio -v

sudo git clone git://github.com/timleland/rfoutlet.git /var/www/rfoutlet
sudo chown root.root /var/www/rfoutlet/codesend
sudo chmod 4755 /var/www/rfoutlet/codesend