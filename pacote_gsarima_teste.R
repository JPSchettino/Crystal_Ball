
 setwd("~/arimageneraizada")
 library(readr)
 train <- read_csv("train.csv")

bt<-train[train$Asset_ID==1,]

btt<-bt[1949000:1950000,]
btteste<-bt[1950001,]
bttt<-btt$Count
btttteste<-btteste$Count
bttcountts<-ts(bttt,frequency = 12)
devtools::load_all()
forecast::Arimapoisson(bttcountts)


