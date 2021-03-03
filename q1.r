
#_____________________________________________________________________________
#Q1-a
#_____________________________________________________________________________

install.packages("readr")   #installing packages and including in library
library(readr)  

install.packages()


#Loading csv file into R
q1_csv = read.csv("C:\\Users\\hp\\Downloads\\Statistical Datasets\\Q1_a.csv")

#installing packages for skewness and kurtosis
install.packages("moments")
library(moments)


#calculating skewness for speed
skewness(q1_csv$speed)

#calculating kurtosis for speed
kurtosis(q1_csv$speed)


#calculating skewness for dist
skewness(q1_csv$dist)

#calculating kurtosis for dist
kurtosis(q1_csv$dist)


#calculating mean median variance and std.deviation range for speed
mean(q1_csv$speed)
median(q1_csv$speed)
var(q1_csv$speed)
sd(q1_csv$speed)
range_speed =  max(q1_csv$speed) - min(q1_csv$speed)
print(range_speed)

#calculating mean median variance and std.deviation range for dist
mean(q1_csv$dist)
median(q1_csv$dist)
var(q1_csv$dist)
sd(q1_csv$dist)
range_dist =  max(q1_csv$dist) - min(q1_csv$dist)
print(range_dist)
#_____________________________________________________________________________
#Q1-b
#_____________________________________________________________________________

#loading csv file into R
q2_csv <- read.csv("C:\\Users\\hp\\Downloads\\Statistical Datasets\\Q2_b.csv")

#packages are installed and loaded in previous code

#calculating skewness for SP
skewness(q2_csv$SP)

#calculating kurtosis for SP
kurtosis(q2_csv$SP)


#calculating skewness for WT
skewness(q2_csv$WT)

#calculating kurtosis for WT
kurtosis(q2_csv$WT)


#calculating mean median variance and std.deviation range for SP
mean(q2_csv$SP)
median(q2_csv$SP)
var(q2_csv$SP)
sd(q2_csv$SP)
range_SP = max(q2_csv$SP) - min(q2_csv$SP)
print(range_SP)


#calculating mean median variance and std.deviation range for WT
mean(q2_csv$WT)
median(q2_csv$WT)
var(q2_csv$WT)
sd(q2_csv$WT)
range_WT = max(q2_csv$WT) - min(q2_csv$WT)
print(range_WT)

#_____________________________________________________________________________
#Q3
#_____________________________________________________________________________

#storing student scores in a array called score

score <- c(34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56)
print(score)

#calculating mean median variance and std.deviation for score
mean(score)
median(score)
var(score)
sd(score)
