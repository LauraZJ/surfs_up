# Surfs Up Analysis

## Purpose
The purpose of this analysis is to gather Time of Observation (TOBs) statistics for Hawaii in the months of June and December.  To complete this analysis, we used jupyter notebook and sqlite.

## Results

* Average temperature:
    * June: ~75 degrees (74.944118)
    * December:  ~71 degrees (71.041529)
* Max temperature
    * June:  85 degrees
    * December:  83 degrees
* Min temperature
    * June: 64 degrees
    * December:  56 degrees

![June stats](https://github.com/LauraZJ/surfs_up/blob/main/resources/June_stats.png)
![December stats](https://github.com/LauraZJ/surfs_up/blob/main/resources/december_stats.png) 
#### *Note:  we have no data for December 2017*

### How it was done
To perform this analysis, we connected to the hawaii.sqlite database and extracted June and December specific TOBs data. 
(*images below are for June but similar actions were taken to gather December data*)

![query june data](https://github.com/LauraZJ/surfs_up/blob/main/resources/query_june_data.png)

We then converted the data to a list and following that step, converted the data to a dataframe, named the columns and set the date as the index (see below).  Once that was completed, we used dataframe.describe() to print the statistics.
![June list](https://github.com/LauraZJ/surfs_up/blob/main/resources/convert_to_list.png)

![june dataframe](https://github.com/LauraZJ/surfs_up/blob/main/resources/create_june_dataframe.png)



## Summary
In reviewing the June and December data, we see that the temperatures are fairly consistent with the differences between the average temps (June 75 / December 71) and max temps (June 85 / December 83) being 4 and 2 degrees respectively.  However, the variance in the minimum is 8 degrees which shows that the December minimum temp is twice the variance between the average temps.

### Additional analysis
Additional analysis that would be helpful is analysis of preciptation data for both months, June and December.  Below, you will see that I have provided the statistics for each month as well as a plot of the data for each month.   When looking at the statistics, we see that the average rainfall in June is 0.136360 inches with the highest rainfall amount of 4.43 inches.  In contrast, the average precipitation in December is 0.216819 with a maximum of 6.42 inches.   
![June_precip_stats](https://github.com/LauraZJ/surfs_up/blob/main/resources/june_precip_stats.png)
![December precip stats](https://github.com/LauraZJ/surfs_up/blob/main/resources/dec_precip_stats.png)
![June precipitation](https://github.com/LauraZJ/surfs_up/blob/main/resources/jun_precip.png)
![Dec preciptation](https://github.com/LauraZJ/surfs_up/blob/main/resources/dec_precip.png)
