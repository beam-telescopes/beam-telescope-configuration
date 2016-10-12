
#!/bin/bash

echo "Script to generate the EUDAQ configuration files for long LED runs"
echo "usage: source create_from1file.sh -l(--labviewConffolder) LabviewPCConfigurationFolder -r(--readoutcycles) CYCLES -e(--eudaqfolder) EUDAQdatafolder -c(--createDatafolder) y/n"
echo "requires the existence of:"
echo "                    a)       the xxLED.conf file, see the end of the script to see how it should look"
echo "                    b)       the longLED_wind/LED_00.ini file, see the end of the script to see how it should look"



LABVFolder="dailyLED_July2016"
CYCLES="3000"
EUDAQ_FOLDER="20160729"
MAKE_DIR="n"

echo "  "
echo " default values "
echo "  "
echo "--labviewConffolder=${LABVFolder}, it assumes: F:\\LEDEUDAQ\\+labviewConffolder+\\LED_yy.ini"
echo "--v0=${NV}"
echo "--nvoltages=${V0}      --> (file 0= pedestal, file 1= voltage 1...)"
echo "--step=${dmV}      --> (increase of mV)"
echo "--readoutcycles=${CYCLES}      --> (increase of mV)"
echo "--eudaqfolder=${EUDAQ_FOLDER=}, it assumes LED/+eudaqfolder+/Run_"
echo "--createDatafolder=${MAKE_DIR}, only for eudaq pc"

for i in "$@"
do
case $i in
    -l=*|--labviewConffolder=*)
    LABVFolder="${i#*=}"
    ;;
    CYCLES-r=*|--readoutcycles=*)
    dmV="${i#*=}"
    ;;
    -e=*|--eudaqfolder=*)
    EUDAQ_FOLDER="${i#*=}"
    ;;
   -c=*|--createfolder=*)
    MAKE_DIR="${i#*=}"
    ;;
    *)
    ;;
esac
done

echo " "
echo LABVFolder = ${LABVFolder} 
echo V0 = ${V0}
echo NV = ${NV}
echo dmV = ${dmV}
echo EUDAQ_FOLDER = ${EUDAQ_FOLDER}
echo MAKE_DIR = ${MAKE_DIR}


if [ "${MAKE_DIR}" == "y" ]
then
    mkdir /home/calice/Desktop/EUDAQ1.6/data/LED/${EUDAQ_FOLDER}
    echo "Creating folder: /home/calice/Desktop/EUDAQ1.6/data/LED/${EUDAQ_FOLDER}"
else
    if [ "${MAKE_DIR}" != "n" ] 
    then
	echo "wrong option, choose --createDatafolder=y or --createDatafolder=n"
	break
    fi
fi

#create file LED_00.conf, pedestal run
echo "Creating Pedestal file, LED_00.conf"

/bin/cp -f $PWD/xxLED.conf $PWD/LED_00.conf
sed -i "s/readoutcycles/${CYCLES}/g" $PWD/LED_00.conf
sed -i "s/labfold/${LABVFolder}/g" $PWD/LED_00.conf
sed -i "s/eudaqfold/${EUDAQ_FOLDER}/g" $PWD/LED_00.conf


#create the others, from minimum VLEDbegin to VLEDend 
#files LED_yy.conf

COUNTERI=0
COUNTERJ=1

while [ $COUNTERI -lt 5 ]; 
do  
    CNT2DI=`seq -f "%02.0f" ${COUNTERI} ${COUNTERI}`
    # echo "2digin counter I: ${CNT2DI}"
    CNT2DJ=`seq -f "%02.0f" ${COUNTERJ} ${COUNTERJ}`
    echo "Creating File-J: ${CNT2DJ}"
    /bin/cp -f $PWD/LED_$CNT2DI.conf $PWD/test.conf
    sed -i "s/LED_$CNT2DI/LED_$CNT2DJ/g" $PWD/test.conf
    /bin/cp -f $PWD/test.conf $PWD/LED_$CNT2DJ.conf
    let COUNTERI=COUNTERI+1
    let COUNTERJ=COUNTERJ+1
done

sed -i "s/NextConfigFileOnFileLimit/\#NextConfigFileOnFileLimit/g" $PWD/LED_$CNT2DJ.conf

rm $PWD/test.conf
