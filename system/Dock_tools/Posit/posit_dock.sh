#!/bin/bash
import sys


#param=sys.argv
#n=param[1]
#m=param[2]
n=
m=
rec=_receptor.oeb.gz


#############outputdirから開始です######################

#全体ループ
while  [ $n -le $m ] 
    do
# 命名
    if [ $n -lt 10 ]
        then
        DXX=D0$n
        else
        DXX=D$n
    fi
##################################
    mkdir $DXX

    cd ./$DXX
    omega2 -in ../sdf/$DXX.sdf -out multiconformer_$DXX.oeb.gz -rms 0.1 
    posit -receptor ../$rec -in multiconformer_$DXX.oeb.gz -docked_molecule_file $DXX.sdf -clashed_molecule_file $DXX.sdf -minimum_probability 0
    cp ./$DXX.sdf ../Docked_pose/$DXX.sdf

    cd ..


#nの再定義
    n=`expr $n + 1 `
    done

