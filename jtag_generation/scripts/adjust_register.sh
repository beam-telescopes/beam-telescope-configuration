# Adjust register 
# adjust header/trailer entries, change postion index, generates new files including postion in name
# by Jan Dreyling-Eschweiler, telescope-coor@desy.de
# version: 11. April 2018
# -----------------------
# Info:
# -----
# adjust extern start
# 0 ; :RO_MODE0[X][1] --> 1 ; :RO_MODE0[X][1]
# adjust ctrl_pix
# 63 ; :CTRL_PIX[X][3] --> 0 ; :CTRL_PIX[X][3]

for POS in '0' '1' '2' '3' '4' '5'
do
    for FILE in pos$POS*.txt
    do
        echo $FILE
        # adjust extern start
        sed -i "s/0 ; :RO_MODE0\[.\]\[1\]/1 ; :RO_MODE0\[$POS\]\[1\]/" $FILE
        sed -i "s/63 ; :CTRL_PIX\[.\]\[3\]/0 ; :CTRL_PIX\[$POS\]\[3\]/" $FILE
        #sed -i 's/.*HEADERTRAILER\[.\]\[1\]/43600 ; :HEADERTRAILER\[0\]\[1\]/' $FILE
        # change position index for all entries and save as new file
        #sed "s/\[./\[$NEW/" $FILE 
        #echo "Write file: pos${NEW}_${FILE}"
    done
done
