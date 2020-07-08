library(xts)
library(forecast)

url <- "http://ichart.finance.yahoo.com/table.csv?s=WMT&a=00&b=2&c=1990&d=05&e=26&f=2015&g=d&ignore=.csv"
WMT.df <- read.table(url,header=TRUE,sep=",")	
WMT <- xts(WMT.df$Close,as.Date(WMT.df$Date))	
head(WMT.df)	
decade <- window(WMT,start="2005-01-01", end="2015-01-01")	
wmt.fit <- HoltWinters(decade, beta=FALSE, gamma=FALSE)#, l.start=23.56)		
plot(wmt.fit)
plot(forecast(wmt.fit, level=c(0.75, 0.9)), col="red", lwd=2)