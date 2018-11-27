######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "68"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 208
IVDREF1B = 160
IVDREF1C = 119
IVDREF1D = 163

# Thermal noise: TN
THN_matA = 1.053
THN_matB = 1.016
THN_matC = 1.055
THN_matD = 0.9633

# Fixed pattern noise: FPN
FPN_matA = 0.3524
FPN_matB = 0.3566
FPN_matC = 0.6797
FPN_matD = 0.5559

# Offset
OFF_matA = 0.3375
OFF_matB = 0.5 #4.988
OFF_matC = 0.3816
OFF_matD = 0.5665

# Disable columns/discriminators
DIS_col = []

######################################
# Generate using Jtag class
from generate_jtag import Jtag
# Constructor
chip = Jtag(sensor_name, IVDREF2, IVDREF1A, IVDREF1B, IVDREF1C, IVDREF1D, THN_matA, THN_matB, THN_matC, THN_matD, FPN_matA, FPN_matB, FPN_matC, FPN_matD, OFF_matA, OFF_matB, OFF_matC, OFF_matD, DIS_col)
# Print values
chip.values()
# Generate txt-files from threshold minimum to maximum
chip.generate(3, 12)
