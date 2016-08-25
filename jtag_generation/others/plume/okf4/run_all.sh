rm chip1/*.txt
rm chip3/*.txt
rm chip4/*.txt
rm chip5/*.txt
rm chip6/*.txt
rm jtag_okf4/*.txt

cd chip6
python jtag_generator.py
source adjust_plane_position.sh 0
cp pos*.txt ../jtag_okf4
cd ..

cd chip5
python jtag_generator.py
source adjust_plane_position.sh 1
cp pos*.txt ../jtag_okf4
cd ..

cd chip4
python jtag_generator.py
source adjust_plane_position.sh 2
cp pos*.txt ../jtag_okf4
cd ..

cd chip3
python jtag_generator.py
source adjust_plane_position.sh 3
cp pos*.txt ../jtag_okf4
cd ..

cd chip1
python jtag_generator.py
source adjust_plane_position.sh 4
cp pos*.txt ../jtag_okf4
cd ..

