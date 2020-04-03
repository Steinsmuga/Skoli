#!/bin/bash
echo "Úr hvaða kerfi vilt þú breyta?:"
echo "1 - Tvíunda"
echo "2 - Áttunda"
echo "3 - Tuga"
echo "4 - Sextánda"
read -p "Veldu aðgerð:" kerfiur
case $kerfiur in
	1)
        	read -p "Sláðu inn tölu í tvíundarkerfinu:" tviunda
		;;
	2)
		read -p "Sláðu inn tölu í áttundakerfinu:" attunda
		;;
	3)
		read -p "Sláðu inn tölu í tugakerfinu:" tuga
		;;
	4)
		read -p "Sláðu inn tölu í sextándakerfinu:" sextanda
		;;
	*)
		read -p "Rangt val"
esac
echo "Í hvaða kerfi vilt þú breyta í?:"
echo "1 - Tvíunda"
echo "2 - Áttunda"
echo "3 - Tuga"
echo "4 - Sextánda"
read -p "Veldu aðgerð:" kerfii

if [ $kerfiur == 1 ] && [ $kerfii == 1 ]
then 
	echo "obase=2; ibase=2; $tviunda" | bc

elif [ $kerfiur == 1 ] && [ $kerfii == 2 ]
then 
        echo "obase=8; ibase=2; $tviunda" | bc

elif [ $kerfiur == 1 ] && [ $kerfii == 3 ]
then 
        echo "obase=10; ibase=2; $tviunda" | bc

elif [ $kerfiur == 1 ] && [ $kerfii == 4 ]
then
        echo "obase=16; ibase=2; $tviunda" | bc
#___________________________________________________
elif [ $kerfiur == 2 ] && [ $kerfii == 1 ]
then 
        echo "obase=2; ibase=8; $attunda" | bc

elif [ $kerfiur == 2 ] && [ $kerfii == 2 ]
then 
        echo "obase=8; ibase=8; $attunda" | bc

elif [ $kerfiur == 2 ] && [ $kerfii == 3 ]
then 
        echo "obase=10; ibase=8; $attunda" | bc

elif [ $kerfiur == 2 ] && [ $kerfii == 4 ]
then
        echo "obase=16; ibase=8; $attunda" | bc
#___________________________________________________
elif [ $kerfiur == 3 ] && [ $kerfii == 1 ]
then 
        echo "obase=2; ibase=10; $tuga" | bc

elif [ $kerfiur == 3 ] && [ $kerfii == 2 ]
then 
        echo "obase=8; ibase=10; $tuga" | bc

elif [ $kerfiur == 3 ] && [ $kerfii == 3 ]
then 
        echo "obase=10; ibase=10; $tuga" | bc

elif [ $kerfiur == 3 ] && [ $kerfii == 4 ]
then 
        echo "obase=16; ibase=10; $tuga" | bc

#___________________________________________________
elif [ $kerfiur == 4 ] && [ $kerfii == 1 ]
then
	echo "obase=2; ibase=16; $sextanda" | bc
elif [ $kerfiur == 4 ] && [ $kerfii == 2 ]
then
        echo "obase=8; ibase=16; $sextanda" | bc
elif [ $kerfiur == 4 ] && [ $kerfii == 3 ]
then
        echo "obase=10; ibase=16; $sextanda" | bc
elif [ $kerfiur == 4 ] && [ $kerfii == 4 ]
then
        echo "obase=16; ibase=16; $sextanda" | bc
fi
