#!/bin/bash
#STR="Hello World!"
#echo $STR

#find a file with extension ".info"
DBS='find ./ -name *.info'
for file in $DBS
do
    #print a result
    echo $file
    #split string with(-) into an array
    #nga-soan-thao-hoc-thuyet-suc-manh-mem-chong-chien-tranh-uy-nhiem-post192332.info
    IFS='-' read -r -a chym <<< "$file"
    #print the last element of the array
    echo "${chym[-1]}"
    #IFS='.' read -r -a cucku <<< "${chym[-1]}"
    #echo "${cucku[-2]}"
done
