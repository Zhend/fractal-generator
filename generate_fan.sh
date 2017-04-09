#process command line arguments
if [ $# -ne 9 ]; then
	echo "Syntax: bash generate_fan.sh x0 y0 x1 y1 dtheta0 ql qtheta num_lines planes rotations"
	echo "Suggested: use 'bash generate_fan.sh 0 250 0 200 0.524 0.95 0.95 y 6'"
	exit
fi

x0=$1
y0=$2
x1=$3
y1=$4
dtheta0=$5
ql=$6
qtheta=$7
planes=$8
rotations=$9

#Read in the available colours
readarray -t colours < css_colours.txt;

#Get generator intermediate picture
	#Evoke generator
	python generate_arc.py $x0 $y0 $x1 $y1 $dtheta0 $ql $qtheta 25 Black > arc.txt

	#Parse arc.txt into an array	
	readarray ARC < arc.txt;

	#Get the line count of arc.txt
	#FIXME: replace with the equivalent argument?
	line_count="${#ARC[@]}";

	#Write over the colours in source txt
		#Write over the first one
		printf "%s" "${ARC[0]}" | sed 's/Black/'"${colours[0]}"'/' > arc.txt;
		#Write over the rest
		for ((i=1;i<line_count;i++));
			do printf "%s" "${ARC[i]}" | sed 's/Black/'"${colours[i]}"'/' >> arc.txt;
		done;

	#Convert the txt to make the intermediate svg
	python lines_to_svg_colour.py arc.txt > arc.svg

#Get final transformed version
	#Transform intermediate txt
	python mirror_duplicate.py arc.txt $planes $rotations > fan.txt
	readarray FAN < fan.txt;
	printf "%s" "${FAN[0]}" | sed 's/Black/'"${colours[0]}"'/' > fan.txt;

	line_count="${#FAN[@]}";

	#write over the colours in fan.txt
	for ((i=1;i<line_count;i++));
		do printf "%s" "${FAN[i]}" | sed 's/Black/'"${colours[i]}"'/' >> fan.txt;
	done;

	python lines_to_svg_colour.py fan.txt > fan.svg
