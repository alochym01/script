ffmpeg -ss $1 -i $3 -t $2 -vcodec copy -acodec copy -y sac_mau_$2.mp4
