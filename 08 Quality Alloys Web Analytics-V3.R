install.packages("moments")
install.packages("corrplot")
install.packages("PerformanceAnalytics")
install.packages("psych")
install.packages("rsq")

library(readxl)
library(data.table)
library(ggplot2)
library(plotly)
library(moments)
library(corrplot)
library(PerformanceAnalytics)
library(psych)
library(lmtest)
library(rsq)

#Reading Values

wv  <- read_excel("Web Analytics Case Student Spreadsheet.xls", sheet = "Weekly Visits", skip =3)
fin <- read_excel("Web Analytics Case Student Spreadsheet.xls", sheet = "Financials",    skip =3)
ls  <- read_excel("Web Analytics Case Student Spreadsheet.xls", sheet = "Lbs. Sold",     skip =3)
dv  <- read_excel("Web Analytics Case Student Spreadsheet.xls", sheet = "Daily Visits",  skip =3)
dem <- read_excel("Web Analytics Case Student Spreadsheet.xls", sheet = "Demographics",  skip =3)

sum(is.na(wv))
sum(is.na(fin))
sum(is.na(ls))
sum(is.na(dv))

#Question 1

#Chart 1 : Unique Visits
cc1 <- ggplot(wv, aes(`Week (2008-2009)`, `Unique Visits`)) +
          geom_bar(stat="identity", width = 0.5, fill="blue") + 
          labs(title="Unique Visits Per Week") +
          theme(axis.text.x = element_text(angle=90, vjust=0.8))
cc1

#Chart 2 : Revenue
cc2 <- ggplot(fin, aes(`Week (2008-2009)`, `Revenue`)) + 
          geom_bar(stat="identity", width = 0.5, fill="blue") + 
          labs(title="Revenue Per Week")
          theme(axis.text.x = element_text(angle=90, vjust=0.8))
cc2

#Chart 3 : Profit
cc3 <- ggplot(fin, aes(`Week (2008-2009)`, `Profit`)) + 
          geom_bar(stat="identity", width = 0.5, fill="blue") +
          labs(title="Profit Per Week") +
           theme(axis.text.x = element_text(angle=90, vjust=0.8))

cc3

#Chart 4: Lbs. Sold
cc4 <- ggplot(fin, aes(`Week (2008-2009)`, `Lbs. Sold`)) + 
       geom_bar(stat="identity", width = 0.5, fill="blue") +
       labs(title="Lbs. Sold") +
       theme(axis.text.x = element_text(angle=90, vjust=0.8))
cc4

#Question 2

S1<-c()
stats <- function (t) {
  S1$mean<- mean(t)
  S1$med <- median(t)
  S1$std <- sd(t)
  S1$min <- min(t)
  S1$max <- max(t)
  return(S1)
}

com_data <- as.data.frame(cbind(wv, fin))
com_data <- com_data[-c(9)]
View(com_data)

ini_data  <- com_data[1:14,]
pre_data  <- com_data[15:35,]
pro_data  <- com_data[36:51,]
post_data <- com_data[52:66,]

#Summary Statistics
com<-c()
com$visit <-stats(com_data$Visits)
com$univ  <-stats(com_data$`Unique Visits`)
com$rev   <-stats(com_data$Revenue)
com$pro   <-stats(com_data$Profit)
com$lb    <-stats(com_data$`Lbs. Sold`)

stat_table_com <- data.table(c("Mean","Median","STD.DEV","Minimum","Maximum"),
                             Visits       <-com$visit,
                             Unique_Visits<-com$univ,
                             Revenue      <-com$rev,
                             Profit       <-com$pro,
                             Lbs_Sold     <-com$lb)
stat_table_com

ini<-c()
ini$visit<-stats(ini_data$Visits)
ini$univ <-stats(ini_data$`Unique Visits`)
ini$rev  <-stats(ini_data$Revenue)
ini$pro  <-stats(ini_data$Profit)
ini$lb   <-stats(ini_data$`Lbs. Sold`)

stat_table_ini <- data.table(c("Mean","Median","STD.DEV","Minimum","Maximum"),
                             Visits       <-ini$visit,
                             Unique_Visits<-ini$univ,
                             Revenue      <-ini$rev,
                             Profit       <-ini$pro,
                             Lbs_Sold     <-ini$lb)
stat_table_ini

pre<-c()
pre$visit<-stats(pre_data$Visits)
pre$univ <-stats(pre_data$`Unique Visits`)
pre$rev  <-stats(pre_data$Revenue)
pre$pro  <-stats(pre_data$Profit)
pre$lb   <-stats(pre_data$`Lbs. Sold`)

stat_table_pre <- data.table(c("Mean","Median","STD.DEV","Minimum","Maximum"),
                             Visits       <-pre$visit,
                             Unique_Visits<-pre$univ,
                             Revenue      <-pre$rev,
                             Profit       <-pre$pro,
                             Lbs_Sold     <-pre$lb)
stat_table_pre

pro<-c()
pro$visit<-stats(pro_data$Visits)
pro$univ <-stats(pro_data$`Unique Visits`)
pro$rev  <-stats(pro_data$Revenue)
pro$pro  <-stats(pro_data$Profit)
pro$lb   <-stats(pro_data$`Lbs. Sold`)

stat_table_pro <- data.table(c("Mean","Median","STD.DEV","Minimum","Maximum"),
                             Visits       <-pro$visit,
                             Unique_Visits<-pro$univ,
                             Revenue      <-pro$rev,
                             Profit       <-pro$pro,
                             Lbs_Sold     <-pro$lb)
stat_table_pro

pos<-c()
pos$visit<-stats(post_data$Visits)
pos$univ <-stats(post_data$`Unique Visits`)
pos$rev  <-stats(post_data$Revenue)
pos$pro  <-stats(post_data$Profit)
pos$lb   <-stats(post_data$`Lbs. Sold`)

stat_table_pos <- data.table(c("Mean","Median","STD.DEV","Minimum","Maximum"),
                             Visits       <-pos$visit,
                             Unique_Visits<-pos$univ,
                             Revenue      <-pos$rev,
                             Profit       <-pos$pro,
                             Lbs_Sold     <-pos$lb)
stat_table_pos

#Profit Regression
com_reg_pro<- lm(Profit ~ Visits + `Unique Visits` + Pageviews + `Pages/Visit` + `Avg. Time on Site (secs.)` + `Bounce Rate` + `Lbs. Sold` + Inquiries + `% New Visits`, data = ini_data)
summary(com_reg_pro)

ini_reg_pro<- lm(Profit ~ Visits + `Unique Visits` + Pageviews + `Pages/Visit` + `Avg. Time on Site (secs.)` + `Bounce Rate` + `Lbs. Sold` + Inquiries + `% New Visits`, data = ini_data)
summary(ini_reg_pro)

pre_reg_pro<- lm(Profit ~ Visits + `Unique Visits` + Pageviews + `Pages/Visit` + `Avg. Time on Site (secs.)` + `Bounce Rate` + `Lbs. Sold` + Inquiries + `% New Visits`, data = pre_data)
summary(pre_reg_pro)

pro_reg_pro<- lm(Profit ~ Visits + `Unique Visits` + Pageviews + `Pages/Visit` + `Avg. Time on Site (secs.)` + `Bounce Rate` + `Lbs. Sold` + Inquiries + `% New Visits`, data = pro_data)
summary(pro_reg_pro)

pos_reg_pro<- lm(Profit ~ Visits + `Unique Visits` + Pageviews + `Pages/Visit` + `Avg. Time on Site (secs.)` + `Bounce Rate` + `Lbs. Sold` + Inquiries + `% New Visits`, data = pro_data)
summary(pos_reg_pro)

#Revenue Regression
com_reg_rev<- lm(Revenue ~ Visits + `Unique Visits` + Pageviews + `Pages/Visit` + `Avg. Time on Site (secs.)` + `Bounce Rate` + `Lbs. Sold` + Inquiries + `% New Visits`, data = com_data)
summary(com_reg_rev)

ini_reg_rev<- lm(Revenue ~ Visits + `Unique Visits` + Pageviews + `Pages/Visit` + `Avg. Time on Site (secs.)` + `Bounce Rate` + `Lbs. Sold` + Inquiries + `% New Visits`, data = ini_data)
summary(ini_reg_rev)

pre_reg_rev<- lm(Revenue ~ Visits + `Unique Visits` + Pageviews + `Pages/Visit` + `Avg. Time on Site (secs.)` + `Bounce Rate` + `Lbs. Sold` + Inquiries + `% New Visits`, data = pre_data)
summary(pre_reg_rev)

pro_reg_rev<- lm(Revenue ~ Visits + `Unique Visits` + Pageviews + `Pages/Visit` + `Avg. Time on Site (secs.)` + `Bounce Rate` + `Lbs. Sold` + Inquiries + `% New Visits`, data = pro_data)
summary(pro_reg_rev)

pos_reg_rev<- lm(Revenue ~ Visits + `Unique Visits` + Pageviews + `Pages/Visit` + `Avg. Time on Site (secs.)` + `Bounce Rate` + `Lbs. Sold` + Inquiries + `% New Visits`, data = pro_data)
summary(pos_reg_rev)

br<- com_data$`Bounce Rate`
wd<- com_data$`Week (2008-2009)`
pv<- com_data$`Pages/Visit`
uv<- com_data$`Unique Visits`
avgtime<- com_data$`Avg. Time on Site (secs.)`

#Chart 1 : Bounce Rate
chart1 <- ggplot(com_data, aes(wd, br)) +
  geom_bar(stat="identity", width = 0.5, fill="blue") +
  labs(title="Bounce Rate")+ labs(x="Week", y= "Bounce Rate") 
chart1
#Chart 2 : Average time on site
chart3 <- ggplot(com_data, aes(wd, avgtime)) +
  geom_bar(stat="identity", width = 0.5, fill="blue") +
  labs(title="Average time on site")+ labs(x="Week", y= "Average time on site")
chart3
#Chart 3 : Page/visit
chart2 <- ggplot(com_data, aes(wd, pv)) +
  geom_bar(stat="identity", width = 0.5, fill="blue") +
  labs(title="Visit")+ labs(x="Week", y= "Page Visit")
chart2

#Chart 4 : Unique visit
chart4 <- ggplot(com_data, aes(wd, uv)) +
  geom_bar(stat="identity", width = 0.5, fill="blue") +
  labs(title="Average time on site")+ labs(x="Week", y= "Average time on site")
chart4

#############Visits/Profit (Scatter)
#complete
scatter<-ggplot(com_data, aes(Visits,Profit))
scatter +geom_point() +geom_smooth(method="lm", colour = "Red") + labs(x="Visits", y= "Profit")

#initial
scatter<-ggplot(ini_data, aes(Visits,Profit))
scatter +geom_point() +geom_smooth(method="lm", colour = "Red") + labs(x="Visits", y= "Profit")
#pre
scatter<-ggplot(pre_data, aes(Visits,Profit))
scatter +geom_point() +geom_smooth(method="lm", colour = "Red") + labs(x="Visits", y= "Profit")
#prom
scatter<-ggplot(pro_data, aes(Visits,Profit))
scatter +geom_point() +geom_smooth(method="lm", colour = "Red") + labs(x="Visits", y= "Profit")
#post
scatter<-ggplot(post_data, aes(Visits,Profit))
scatter +geom_point() +geom_smooth(method="lm", colour = "Red") + labs(x="Visits", y= "Profit")




