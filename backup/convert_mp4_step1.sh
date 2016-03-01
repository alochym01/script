#: to use the file: convert mp4 file to mpegts
#:  syntax: bash convert_mp4_step1 file_mp4_convert($1) file_name(mpegts)
ffmpeg -i $1 -c copy -bsf:v h264_mp4toannexb -f mpegts $2.ts
