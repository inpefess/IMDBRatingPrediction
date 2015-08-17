IMDBUrl="ftp://ftp.fu-berlin.de/pub/misc/movies/database"
rm -r sources
mkdir sources
for name in $(cat sourceNames)
do
	wget $IMDBUrl/${name}.list.gz
	cp ${name}.list.gz sources
	gunzip ${name}.list.gz
done
