#!/system/xbin/bash
clear
toilet -f slant --gay "LiteSpam"
echo "\033[36;1m Spam Yang Tersedia :"
echo "1. Tokopedia"
echo "2. Telkomsel"
echo "3. Matahari Mall"
echo "4. PHD"
echo "5. Jd.Id"
echo "6. Email Bomber"
echo "7. toko cash call"
echo "0. Keluar"
echo "\033[33;1m Pilih Angka:"
read mrrm
if [ $mrrm = 1 ] || [ $mrrm = 1 ]
then
clear
echo "\033[34;1m"
php 1.php
fi

if
[ $mrrm = 2 ] || [ $mrrm = 2 ]
then
clear
echo "\033[31;1m"
toilet "T-Sel"
php 2.php
fi

if [ $mrrm = 3 ] || [ $mrrm = 3 ]
then
clear
echo "\033[31;1m"
figlet "Mthr Mall"
php 3.php
fi


if [ $mrrm = 4 ] || [ $mrrm = 4 ]
then
clear
toilet -f mono12 -F gay "PHD"
echo "\033[30;1m"
php 4.php
fi

if
[ $mrrm = 5 ] || [ $mrrm = 5 ]
then
clear
toilet -f mono12 -F gay "Jd.Id"
echo "\033[33;1m"
php 5.php
fi

if
[ $mrrm = 6 ] || [ $mrrm = 6 ]
then
clear
toilet -f standard -F gay "Email Bomber"
echo "\033[36;1m"
python2 6.py
fi

if [ $mrrm = 7 ] || [ $mrrm = 7 ]
then
clear
echo "\033[34;1m"
figlet "cash call"
python2 call.py
fi
