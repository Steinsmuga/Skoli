#!/bin/bash
kerfiur=0
while [ $kerfiur != 5 ]
do
	echo "Úr hvaða kerfi vilt þú breyta?:"
	echo "1 - Tvíunda"
	echo "2 - Áttunda"
	echo "3 - Tuga"
	echo "4 - Sextánda"
	echo "5 - Hætta í Forritinu"
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
		5)
			break
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

	if [ $kerfiur == 1 ]
	then
		for i in $kerfii
		do
			if [ $i == 1 ]
			then
				echo "obase=2; ibase=2; $tviunda" | bc
			elif [ $i == 2 ]
			then
				echo "obase=8; ibase=2; $tviunda" | bc
			elif [ $i == 3 ]
			then
				echo "obase=10; ibase=2; $tviunda" | bc
			elif [ $i == 4 ]
                	then
                        	echo "obase=16; ibase=2; $tviunda" | bc

			fi
		done
	elif [ $kerfiur == 2 ]
	then
        	for i in $kerfii
        	do
                	if [ $i == 1 ]
                	then
                        	echo "obase=2; ibase=8; $attunda" | bc
                	elif [ $i == 2 ]
                	then
                        	echo "obase=8; ibase=8; $attunda" | bc
                	elif [ $i == 3 ]
                	then
                        	echo "obase=10; ibase=8; $attunda" | bc
                	elif [ $i == 4 ]
                	then
                        	echo "obase=16; ibase=8; $attunda" | bc

                	fi
        	done

	elif [ $kerfiur == 3 ]
	then
        	for i in $kerfii
        	do
                	if [ $i == 1 ]
                	then
                        	echo "obase=2; ibase=10; $tuga" | bc
               		 elif [ $i == 2 ]
                	then
                        	echo "obase=8; ibase=10; $tuga" | bc
                	elif [ $i == 3 ]
                	then
                        	echo "obase=10; ibase=10; $tuga" | bc
                	elif [ $i == 4 ]
                	then
                        	echo "obase=16; ibase=10; $tuga" | bc

                	fi
        	done

	elif [ $kerfiur == 4 ]
	then
        	for i in $kerfii
        	do
                	if [ $i == 1 ]
                	then
                        	echo "obase=2; ibase=16; $sextanda" | bc
                	elif [ $i == 2 ]
                	then
                        	echo "obase=8; ibase=16; $sextanda" | bc
                	elif [ $i == 3 ]
                	then
                        	echo "obase=10; ibase=16; $sextanda" | bc
                	elif [ $i == 4 ]
                	then
                        	echo "obase=16; ibase=16; $sextanda" | bc

                	fi
        	done

	fi
done
