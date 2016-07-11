TELESCOPE='aconite'
#rm chip57/*.txt
rm jtag_$TELESCOPE/*.txt

cd chip57
#python jtag_generator.sh
source adjust_plane_position.sh 0
cp pos*.txt ../jtag_$TELESCOPE
cd ..

cd chip68
#python jtag_generator.sh
source adjust_plane_position.sh 1
cp pos*.txt ../jtag_$TELESCOPE
cd ..

cd chip81
#python jtag_generator.sh
source adjust_plane_position.sh 2
cp pos*.txt ../jtag_$TELESCOPE
cd ..

