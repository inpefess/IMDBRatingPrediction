IMDBUrl="ftp://ftp.fu-berlin.de/pub/misc/movies/database"
rm -r sources
mkdir sources
cd sources
for name in $(cat ../sourceNames)
do
	wget $IMDBUrl/${name}.list.gz
done
