
setwd("~/GitHub/Crystal_Ball")
 library(readr)
 train <- read_csv("train.csv")
 bt<-train[train$Asset_ID==1,]


 targ<-bt$Target
 
seasonal::seas(ts(targ[1955982:1956262],start = c(2000,0),frequency = 12))




