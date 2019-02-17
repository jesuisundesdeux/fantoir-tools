system(paste("wget","http://www.nosdonnees.fr/wiki/images/b/b5/EUCircos_Regions_departements_circonscriptions_communes_gps.csv.gz"))
system(paste('gunzip',"EUCircos_Regions_departements_circonscriptions_communes_gps.csv.gz"))
lat_lon_comm=read.csv('EUCircos_Regions_departements_circonscriptions_communes_gps.csv',sep=";")
names(lat_lon_comm)[5]='codedep'
three_last_chars=function(tt){substr(tt,nchar(tt)-2,nchar(tt))}
lat_lon_comm$codecom=as.numeric(three_last_chars(as.character(lat_lon_comm$code_insee)))
fantoir_bruno_codep_codecom=read.csv('https://raw.githubusercontent.com/jesuisundesdeux/fantoir-tools/master/villes.csv',sep=";")
fantoir_et_lat_lon=merge(fantoir_bruno_codep_codecom,lat_lon_comm)
sorted_extr_fantoir_et_lat_lon=fantoir_et_lat_lon[order(1000*as.numeric(fantoir_et_lat_lon$codedep)+as.numeric(fantoir_et_lat_lon$codecom)),c(1,3,2,4,15,16)]

sorted_extr_fantoir_et_lat_lon$codecom=sprintf("%03i",sorted_extr_fantoir_et_lat_lon$codecom)
write.csv2(sorted_extr_fantoir_et_lat_lon,file =  "villes_lat_lon.csv",quote = FALSE,row.names = FALSE)
