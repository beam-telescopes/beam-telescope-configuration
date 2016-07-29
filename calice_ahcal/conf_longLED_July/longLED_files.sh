#!/bin/bash

echo "Script to generate the EUDAQ configuration files for long LED runs"
echo "usage: source create_from1file.sh -l(--labviewConffolder) LabviewPCConfigurationFolder -v(--v0) V0 -n(--nvoltages) NVoltages -s(--step) dmv_step -r(--readoutcycles) CYCLES -e(--eudaqfolder) EUDAQdatafolder -c(--createDatafolder) y/n"
echo "requires the existence of:"
echo "                    a)       the xxLED.conf file, see the end of the script to see how it should look"
echo "                    b)       the longLED_wind/LED_00.ini file, see the end of the script to see how it should look"



LABVFolder="longLED_July2016"
NV="91"
V0="3500"
dmV="50"
CYCLES="3000"
EUDAQ_FOLDER="20160729_long"
MAKE_DIR="y"

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
    -v=*|--v0=*)
    V0="${i#*=}"
    ;;
    -n=*|--nvoltages=*)
    NV="${i#*=}"
    ;;
    CYCLES-r=*|--readoutcycles=*)
    dmV="${i#*=}"
    ;;
    -s=*|--step=*)
    ="${i#*=}"
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

while [ $COUNTERI -lt ${NV} ]; 
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

## Create Windows, configuration files
echo "Create Windows, configuration files"

cd longLED_wind

COUNTERI=1
COUNTERJ=2
LEDV=${V0}
LEDV2=${V0}

while [ $COUNTERI -lt ${NV} ]; 
do  
    
    let LEDV2=LEDV+${dmV}
    CNT2DI=`seq -f "%02.0f" ${COUNTERI} ${COUNTERI}`
    echo "2digin counter I: ${CNT2DI}"
    CNT2DJ=`seq -f "%02.0f" ${COUNTERJ} ${COUNTERJ}`
    echo "2digin counter J: ${CNT2DJ}"
    /bin/cp -f $PWD/LED_$CNT2DI.ini $PWD/test.ini
    sed -i "s/\=$LEDV/\=$LEDV2/g" $PWD/test.ini
    /bin/cp -f $PWD/test.ini $PWD/LED_$CNT2DJ.ini
    let COUNTERI=COUNTERI+1
    let COUNTERJ=COUNTERJ+1
    let LEDV=LEDV+${dmV}
done

rm $PWD/test.ini

scp *.ini calice@131.169.184.84:F:\\LEDEUDAQ\\${LABVFolder}\\.


# xxLED.conf
# This is an example config file, you can adapt it to your needs.
# All text following a # character is treated as comments

#[RunControl]
#RunEventLimit = readoutcycles
#NextConfigFileOnFileLimit = 1
#
#[LogCollector]
#SaveLevel = EXTRA
#PrintLevel = INFO
#
#
#[Producer.CaliceSc]
#FileLEDsettings ="F:\\LEDEUDAQ\\labfold\\LED_00.ini"
#FileMode = 0
#WaitMillisecForFile = 1000
## Sleeping time (in seconds) after clicking stop: needed to read
## all the events stored in the Labview data queue
#waitsecondsForQueuedEvents = 6
#
#Port = 5622
#IPAddress = "192.168.1.11"
#Reader = "Scintillator"
#
#WriteRawOutput = 1
#RawFileName = "LED/eudaqfold/DetectorRawData_Run_%05d"
#WriteRawFileNameTimestamp = 0
#
#
#[DataCollector.CaliceDataCollector]
#FileType = "lcio"                                                       
#FilePattern = "LED/eudaqfold/Run_$5R$X"


# longLED_wind/LED_00.ini
#;==================================================
#; This is test configuration file for auotmatic LED scan.
#; The format of this file is based on Windows configuration
#; settings file and is divided into sections by brackets.
#; Brackets enclose section name which in our case is the
#; Module ID. Each section has a key named "voltage" which
#; takes a 4 digits integer as LED voltage of that layer in mV. 
#;==================================================
#
#[1]
#voltage=0 ; One can write comments for each line
#
#[2]
#voltage=0
#
#[3]
#voltage=0
#
#[4]
#voltage=0
#
#[5]
#voltage=0
#
#etc
