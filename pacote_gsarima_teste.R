
 setwd("~/arimageneraizada")
 library(readr)
 train <- read_csv("train.csv")
 library(gsarima)
bt<-train[train$Asset_ID==1,]

btt<-bt[1949000:1950000,]

bttt<-btt$Count
bttcountts<-ts(bttt,frequency = 12)

gsarima::garsim(n=1,bttcountts,family = "poisson", link= "log")

bttt
