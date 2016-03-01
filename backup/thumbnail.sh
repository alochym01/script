#: to use the file:
#:  syntax: bash split.sh start_time(00:00:12) end_time_in_second(250) film
#ffmpeg -ss $1 -i $3 -t $2 -vcodec copy -acodec copy -y mon_ngon_moi_ngay_$2.mp4
ffmpeg -i $1 -r 1 -t 15 -s hd720 image-%3d.jpeg
