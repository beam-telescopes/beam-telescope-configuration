# JTAG files generator
# calculates DAC values for different S/N cuts (3 to 12) and generates JTAG (txt) files, update creation date
# by Jan Dreyling-Eschweiler, telescope-coor@desy.de
# First version: 4. September 2015
# -----------------------

# modules
import re
import math
import numpy as np
import time
import inspect, os

class Jtag:
    def __init__(self, sensor_name, IVDREF2, IVDREF1A, IVDREF1B, IVDREF1C, IVDREF1D, THN_matA, THN_matB, THN_matC, THN_matD, FPN_matA, FPN_matB, FPN_matC, FPN_matD, OFF_matA, OFF_matB, OFF_matC, OFF_matD, DIS_col):
        self.sensor_name = sensor_name
        self.IVDREF2  = IVDREF2 
        self.IVDREF1A = IVDREF1A
        self.IVDREF1B = IVDREF1B
        self.IVDREF1C = IVDREF1C
        self.IVDREF1D = IVDREF1D
        self.THN_matA = THN_matA 
        self.THN_matB = THN_matB
        self.THN_matC = THN_matC
        self.THN_matD = THN_matD
        self.FPN_matA = FPN_matA
        self.FPN_matB = FPN_matB
        self.FPN_matC = FPN_matC
        self.FPN_matD = FPN_matD
        self.OFF_matA = OFF_matA
        self.OFF_matB = OFF_matB
        self.OFF_matC = OFF_matC
        self.OFF_matD = OFF_matD
        self.DIS_col = np.array(DIS_col)
        self.input_file = "default_jtag.txt" 
        self.DAC_slope = 0.25

    def values(self):
        print "Sensor", self.sensor_name
        # Middlepoints in DAC
        print "IVDREF2:", self.IVDREF2
        print "Middlepoint A:", self.IVDREF1A
        print "Middlepoint B:", self.IVDREF1B
        print "Middlepoint C:", self.IVDREF1C
        print "Middlepoint D:", self.IVDREF1D
        # Temporal noise: TN
        print "Temporal noise (mean) A:", self.THN_matA
        print "Temporal noise (mean) B:", self.THN_matB
        print "Temporal noise (mean) C:", self.THN_matC
        print "Temporal noise (mean) D:", self.THN_matD
        # Fixed pattern noise: FPN
        print "Fixed Pattern noise (sigma) A:", self.FPN_matA
        print "Fixed Pattern noise (sigma) B:", self.FPN_matB
        print "Fixed Pattern noise (sigma) C:", self.FPN_matC
        print "Fixed Pattern noise (sigma) D:", self.FPN_matD
        # Offset
        print "Offset (FPN mean) A:", self.OFF_matA
        print "Offset (FPN mean) B:", self.OFF_matB
        print "Offset (FPN mean) C:", self.OFF_matC
        print "Offset (FPN mean) D:", self.OFF_matD
        # Disabled columns
        print "Columns to diable:", self.DIS_col

    def generate(self, thr_min, thr_max):
        # Offset in DAC units
        IVDREF1A_offset = -(self.IVDREF1A * self.DAC_slope) 
        IVDREF1B_offset = -(self.IVDREF1B * self.DAC_slope) 
        IVDREF1C_offset = -(self.IVDREF1C * self.DAC_slope) 
        IVDREF1D_offset = -(self.IVDREF1D * self.DAC_slope) 
        # total noise
        TON_matA = math.sqrt(self.THN_matA**2 + self.FPN_matA**2) 
        TON_matB = math.sqrt(self.THN_matB**2 + self.FPN_matB**2) 
        TON_matC = math.sqrt(self.THN_matC**2 + self.FPN_matC**2) 
        TON_matD = math.sqrt(self.THN_matD**2 + self.FPN_matD**2) 
        TON_avg = (TON_matA + TON_matB + TON_matC + TON_matD) / 4
        #print TON_matA, TON_matB, TON_matC, TON_matD
        print "\nTotal noise average of sensor", str(self.sensor_name), "-->", TON_avg 
        # Sigma to noise cut
        SN = np.arange(thr_min, thr_max+1)
        #print SN
        # mV value 
        VmV_matA = (TON_matA * SN) + self.OFF_matA
        VmV_matB = (TON_matB * SN) + self.OFF_matB
        VmV_matC = (TON_matC * SN) + self.OFF_matC
        VmV_matD = (TON_matD * SN) + self.OFF_matD
        #print VmV_matA, VmV_matB, VmV_matC, VmV_matD
        # DAC value
        DAC_matA = (VmV_matA - IVDREF1A_offset) / self.DAC_slope 
        DAC_matB = (VmV_matB - IVDREF1B_offset) / self.DAC_slope
        DAC_matC = (VmV_matC - IVDREF1C_offset) / self.DAC_slope
        DAC_matD = (VmV_matD - IVDREF1D_offset) / self.DAC_slope
        #print DAC_matA, DAC_matB, DAC_matC, DAC_matD
        DAC_matA = np.round(DAC_matA).astype(int) 
        DAC_matB = np.round(DAC_matB).astype(int) 
        DAC_matC = np.round(DAC_matC).astype(int) 
        DAC_matD = np.round(DAC_matD).astype(int) 
        #print DAC_matA, DAC_matB, DAC_matC, DAC_matD
        # set 255 as highest value
        # print np.where(DAC_matD > 255)
        DAC_matA[np.where(DAC_matA > 255)] = 255.
        DAC_matB[np.where(DAC_matB > 255)] = 255.
        DAC_matC[np.where(DAC_matC > 255)] = 255.
        DAC_matD[np.where(DAC_matD > 255)] = 255.
        #print DAC_matA, DAC_matB, DAC_matC, DAC_matD

        # Adjust DAC values in txt-files
        # -----------------
        # e.g. DAC-vlaues (XXX) of plane 0
        # line 26: XXX ; :BIAS_DAC[0][10] --> IVDREF1D
        # line 27: XXX ; :BIAS_DAC[0][11] --> IVDREF1C
        # line 28: XXX ; :BIAS_DAC[0][12] --> IVDREF1B
        # line 29: XXX ; :BIAS_DAC[0][13] --> IVDREF1A
        # line 30: XXX ; :BIAS_DAC[0][14] --> IVDREF2

        for i, n in enumerate(SN):
          #print i, n

          output_file = "chip" + str(self.sensor_name) + "_thresh" + str(SN[i]) + ".txt" 
          print "\nWrite file:",  output_file
          file_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
          # IVDREF2
          with open(file_path + "/" + self.input_file, "r") as sources:
              lines = sources.readlines()
          with open(output_file, "w") as sources:
              for line in lines:
                  sources.write(re.sub(r'^(.*?)BIAS_DAC\[.\]\[14\]', str(self.IVDREF2) + ' ; :BIAS_DAC[0][14]', line))
          #print "IVDREF2", IVDREF2

          # IVDREF1A
          with open(output_file, "r") as sources:
              lines = sources.readlines()
          with open(output_file, "w") as sources:
              for line in lines:
                  sources.write(re.sub(r'^(.*?)BIAS_DAC\[.\]\[13\]', str(DAC_matA[i]) + ' ; :BIAS_DAC[0][13]', line))
          print "DAC_matA["+str(n)+"]", DAC_matA[i], ", Delta Middlepoints:", DAC_matA[i]-self.IVDREF1A

          # IVDREF1B
          with open(output_file, "r") as sources:
              lines = sources.readlines()
          with open(output_file, "w") as sources:
              for line in lines:
                  sources.write(re.sub(r'^(.*?)BIAS_DAC\[.\]\[12\]', str(DAC_matB[i]) + ' ; :BIAS_DAC[0][12]', line))
          print "DAC_matB["+str(n)+"]", DAC_matB[i], ", Delta Middlepoints:", DAC_matB[i]-self.IVDREF1B

          # IVDREF1C
          with open(output_file, "r") as sources:
              lines = sources.readlines()
          with open(output_file, "w") as sources:
              for line in lines:
                  sources.write(re.sub(r'^(.*?)BIAS_DAC\[.\]\[11\]', str(DAC_matC[i]) + ' ; :BIAS_DAC[0][11]', line))
          print "DAC_matC["+str(n)+"]", DAC_matC[i], ", Delta Middlepoints:", DAC_matC[i]-self.IVDREF1C

          # IVDREF1D
          with open(output_file, "r") as sources:
              lines = sources.readlines()
          with open(output_file, "w") as sources:
              for line in lines:
                  sources.write(re.sub(r'^(.*?)BIAS_DAC\[.\]\[10\]', str(DAC_matD[i]) + ' ; :BIAS_DAC[0][10]', line))
          print "DAC_matD["+str(n)+"]", DAC_matD[i], ", Delta Middlepoints:", DAC_matD[i]-self.IVDREF1D

          # date and time
          with open(output_file, "r") as sources:
              lines = sources.readlines()
          with open(output_file, "w") as sources:
              for line in lines:
                  sources.write(re.sub(r'^\#JTAG\_MS(.*?)$', '#JTAG_MS ' + time.strftime("%c"), line))

          # Disabling columns
          if not len(self.DIS_col):
            print "No columns were disabled."
          else:
            for ii, nn in enumerate(self.DIS_col):
              print "Disabling column:", nn
              with open(output_file, "r") as sources:
                  lines = sources.readlines()
              with open(output_file, "w") as sources:
                  for line in lines:
                      sources.write(re.sub(r'^0 \; \:DIS\_DISCRI\[0\]\[{}\]'.format(nn), '1 ; :DIS_DISCRI[0][' + str(nn) + ']', line))


