# Adjust plane position and generates JTAG file with prefix 
# argument: plane position (number)
# adjust header/trailer entries, change postion index, generates new files including postion in name
# by Jan Dreyling-Eschweiler, telescope-coor@desy.de
# First version: 4. September 2015
# -----------------------
# Info:
# -----
# general JTAG-structure:
# value ; :NAME[plane number][index number]
# Check constant header/trailer:
# line 64: 43600 ; :HEADERTRAILER[X][1]
# line 66: 21845 ; :HEADERTRAILER[X][3]
# e.g. from plane 0 to 1
# Adjust changing header/trailer (e.g. from plane 0 to 1):
# line 63: 43601 ; :HEADERTRAILER[0][0] --> 43602 ; :HEADERTRAILER[1][0]
# line 65: 21841 ; :HEADERTRAILER[0][2] --> 21842 ; :HEADERTRAILER[1][2]

NEW=$1
HEADER0=$((43601+$NEW))
HEADER2=$((21841+$NEW))

for FILE in *thresh*.txt
do 
  # adjust postion header/trailer
  sed -i "s/.*HEADERTRAILER\[.\]\[0\]/$HEADER0 ; :HEADERTRAILER\[0\]\[0\]/" $FILE
  sed -i "s/.*HEADERTRAILER\[.\]\[2\]/$HEADER2 ; :HEADERTRAILER\[0\]\[2\]/" $FILE
  # check/adjust constant header/trailer
  sed -i 's/.*HEADERTRAILER\[.\]\[1\]/43600 ; :HEADERTRAILER\[0\]\[1\]/' $FILE
  sed -i 's/.*HEADERTRAILER\[.\]\[3\]/21845 ; :HEADERTRAILER\[0\]\[3\]/' $FILE
  # change position index for all entries and save as new file
  sed "s/\[./\[$NEW/" $FILE > "pos${NEW}_${FILE}"
  echo "Write file: pos${NEW}_${FILE}"
done
