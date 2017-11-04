make.age <- function(birth){
  df <- NULL
  for(i in 1:length(birth)){
      if(is.na(birth[i])){
          df[i] <- NA
      }else{
          df[i] <- (length(seq(as.Date(birth[i]), Sys.Date(), "year"))-1)
      }
  }
  return(df)
}

d <- read.csv("cv.csv",header=F)
birth.date <- as.Date(d[,4])

anime.start <- as.Date("2015-01-01")
vote5th <- as.Date("2016-5-9")

zissou <- as.Date(d[,3])


age <- make.age(birth.date)

png("hist.png")
hist(age+1,breaks=seq(min(na.omit(age)),max(na.omit(age)+1),1),main="CINDERELLA_CV 2017/10/28",xlab="age",col="skyblue")
hist(age[zissou>anime.start]+1,breaks=seq(min(na.omit(age)),max(na.omit(age)+1),1),main="CINDERELLA_CV",add=TRUE,col="pink")
hist(age[zissou>vote5th]+1,breaks=seq(min(na.omit(age)),max(na.omit(age)+1),1),main="CINDERELLA_CV",add=TRUE,col="lightgreen")

legend("topleft",legend=c("anime-izen","anime-ikou","5thVote-ikou"),col=c("blue","red","green"),pch=19)
dev.off()
