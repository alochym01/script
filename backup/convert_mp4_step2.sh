#: to use the file:
#:  syntax: bash convert_mp4_step2.sh file_name_01 file_name_02
ffmpeg -i "concat:$1|$2" -c copy -bsf:a aac_adtstoasc output.mp4
