#!/bin/bash

# Bash script to replace
# the names with alphabetically sorted names
# It accepts a file name as input and outputs
# a new file

FILE=$1 

sed -e 's/HindIII_1_2_flt/A_HindIII_1_2_flt/g' $FILE | sed -e 's/NcoI_1_2_flt/B_NcoI_1_2_flt/g' | sed -e 's/HindIII_NcoI_1_flt/C_HindIII_NcoI_1_flt/g' |\
sed -e 's/HindIII_NcoI_2_flt/D_HindIII_NcoI_2_flt/g' | sed -e 's/HindIII_1_2_cor/A_HindIII_1_2_cor/g' | sed -e 's/NcoI_1_2_cor/B_NcoI_1_2_cor/g' |\
sed -e 's/HindIII_NcoI_1_cor/C_HindIII_NcoI_1_cor/g' | sed -e 's/HindIII_NcoI_2_cor/D_HindIII_NcoI_2_cor/g'> ${FILE%.txt}.new.txt
