#_____________________________________________________________________________
#Q1-a
#Calculate Skewness, Kurtosis using R/Python code & draw inferences on the following data.
#(dataset is given in seperate folder please refer)
#_____________________________________________________________________________
# importing packages needed for problem
import pandas as pd
from scipy import stats


#importing data set required for analysis
q1_csv = pd.read_csv("C:\\Users\\hp\\Downloads\\Statistical Datasets\\Q1_a.csv")

#calculating skewness and kurtosis for speed
skew_speed = q1_csv.speed.skew()
print("skewness for speed", skew_speed)
kurt_speed = q1_csv.speed.kurt()
print("kurtosis for speed" , kurt_speed)

#calculating skewness and kurtosis for dist
skew_dist = q1_csv.dist.skew()
print("skewness for dist ",skew_dist)
kurt_dist = q1_csv.dist.kurt()
print("kurtosis for dist " , kurt_dist)

#calculating mean median varience standard deviation range for speed
mean_speed = q1_csv.speed.mean()
print("mean of speed", mean_speed)
median_speed = q1_csv.speed.median()
print("median of speed", median_speed)
var_speed = q1_csv.speed.var()
print("varience of speed", var_speed)
std_speed = q1_csv.speed.std()
print("standard deviation of speed", std_speed)
range_spd = max(q1_csv.speed) - min(q1_csv.speed)
print("range of speed", range_spd)


#calculating mean median varience standard deviation range for dist
mean_dist = q1_csv.dist.mean()
print("mean of dist", mean_dist)
median_dist = q1_csv.dist.median()
print("median of dist", median_dist)
var_distd = q1_csv.dist.var()
print("varience of dist", var_distd)
std_dist = q1_csv.dist.std()
print("standard deviation of dist", std_dist)
range_dist = max(q1_csv.dist) - min(q1_csv.dist)
print("range of dist", range_dist)


print("##############################Q2####################################")
#Top Speed (SP) and Weight (WT) 
#Calculate Skewness, Kurtosis using R/Python code & draw inferences on the following data.
#(dataset is given in seperate folder please refer)
      
#importing data set required for analysis
q2_csv = pd.read_csv("C:\\Users\\hp\\Downloads\\Statistical Datasets\\Q2_b.csv")

#calculating and printing skewness and kurtosis for SP
skew_SP = q2_csv.SP.skew()
print("skewness for SP", skew_SP)

kurt_SP = q2_csv.SP.kurt()
print("kurtosis for SP" , kurt_SP)

#calculating and printing skewness and kurtosis for WT
skew_WT = q2_csv.WT.skew()
print("skewness for WT ",skew_WT)

kurt_WT = q2_csv.WT.kurt()
print("kurtosis for WT " , kurt_WT)

#calculating and printing mean median varience standard deviation range for speed
mean_SP = q2_csv.SP.mean()
print("mean of SP", mean_SP)

median_SP = q2_csv.SP.median()
print("median of SP", median_SP)

var_SP = q2_csv.SP.var()
print("varience of SP", var_SP)

std_SP = q2_csv.SP.std()
print("standard deviation of SP", std_SP)

range_SP = max(q2_csv.SP) - min(q2_csv.SP)
print("range of SP", range_SP)


#calculating and printing mean median varience standard deviation range for WT
mean_WT = q2_csv.WT.mean()
print("mean of WT", mean_WT)

median_WT = q2_csv.WT.median()
print("median of WT", median_WT)

var_WT = q2_csv.WT.var()
print("varience of WT", var_WT)

std_WT = q2_csv.WT.std()
print("standard deviation of WT", std_WT)

range_WT = max(q2_csv.WT) - min(q2_csv.WT)
print("range of WT", range_WT)
