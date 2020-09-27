# COURSE EVALUATIONS STATS
## Gathering the data
In this project we used `collect data.py` to get the data from the course evaluations provided
> #### How to use `collect data.py`
> Put the file into a folder containing all the course evaluations pdf and run the py file. it will then procceed to collect the statistical data(mean,mode,median,SD) for the first 6 questions, from the files in that folder and add it to a `data.csv` file
> #### Issues faced using this script
> * some parts of data were not collected, but considering it being very little data it can be added manually by re-tracing it to its original file (course evaluation pdf) and and adding the missing values to the csv file using excel
> * some files have 0 respondants to values for those rows will be N/A but we will deal with those rows when cleaning up the data
> * some files have modes that have recuring values (i.e mode can be 1 and 2). we will come to a convention as to what value we will use

## Analyzing the data
    library(pequod)

    ## Loading required package: ggplot2

    ## Loading required package: car

    ## Loading required package: carData

    library(readr)
    library(janitor)

    ## 
    ## Attaching package: 'janitor'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     chisq.test, fisher.test

    library(gmodels)
    library(productplots)
    library(CGPfunctions)

    ## Registered S3 method overwritten by 'DescTools':
    ##   method         from 
    ##   reorder.factor gdata

    ## Warning in checkMatrixPackageVersion(): Package version inconsistency detected.
    ## TMB was built with Matrix version 1.2.17
    ## Current Matrix version is 1.2.18
    ## Please re-install 'TMB' from source using install.packages('TMB', type = 'source') or ask CRAN for a binary version of 'TMB' matching CRAN's 'Matrix' package

    ## Registered S3 method overwritten by 'broom.mixed':
    ##   method      from 
    ##   tidy.gamlss broom

    ## Registered S3 methods overwritten by 'lme4':
    ##   method                          from
    ##   cooks.distance.influence.merMod car 
    ##   influence.merMod                car 
    ##   dfbeta.influence.merMod         car 
    ##   dfbetas.influence.merMod        car

    library(pequod)
    library(jtools) # for summ()
    library(ggpubr)

    data01 = read_csv("data.csv")

    ## Parsed with column specification:
    ## cols(
    ##   .default = col_character(),
    ##   Invited = col_double(),
    ##   Responded = col_double()
    ## )

    ## See spec(...) for full column specifications.

    data01<-na.omit(data01)
    data01

    ## # A tibble: 92 x 30
    ##    Course Campus Term  Section Invited Responded Mean1 Mean2 Mean3 Mean4 Mean5
    ##    <chr>  <chr>  <chr> <chr>     <dbl>     <dbl> <chr> <chr> <chr> <chr> <chr>
    ##  1 JRE42… UTSG   Fall… LEC0103      55        18 2.4   2.5   2.8   2.7   2.8  
    ##  2 JRE42… UTSG   Fall… LEC0103      54        14 3.2   3.1   3.6   3.2   3.2  
    ##  3 JRE42… UTSG   Fall… LEC0103      55        37 2.5   2.8   3.8   3     3.1  
    ##  4 JRE42… UTSG   Fall… LEC0103      53        14 2.8   3.6   3.6   3.1   3.2  
    ##  5 JRE42… UTSG   Summ… LEC0101      48        20 3.5   3.6   4     3.5   3.4  
    ##  6 JRE42… UTSG   Wint… LEC0103      52        16 2.4   2.1   2.3   2.4   2.5  
    ##  7 JRE42… UTSG   Wint… LEC0103      55        31 2.9   3.2   3.4   2.9   3    
    ##  8 JRE42… UTSG   Wint… LEC0103      46        14 3.7   4     4.3   4.1   4.1  
    ##  9 MGHB0… UTSC   Fall… LEC01        62        18 2.6   2.7   3.2   2.8   2.9  
    ## 10 MGHB0… UTSC   Fall… LEC01        52        28 2.7   2.8   2.9   2.5   2.8  
    ## # … with 82 more rows, and 19 more variables: Mean6 <chr>, Median1 <chr>,
    ## #   Median2 <chr>, Median3 <chr>, Median4 <chr>, Median5 <chr>, Median6 <chr>,
    ## #   Mode1 <chr>, Mode2 <chr>, Mode3 <chr>, Mode4 <chr>, Mode5 <chr>,
    ## #   Mode6 <chr>, StdDev1 <chr>, StdDev2 <chr>, StdDev3 <chr>, StdDev4 <chr>,
    ## #   StdDev5 <chr>, StdDev6 <chr>

    # filter UTSC data
    UTSC_Data <-  data01[data01$Campus=="UTSC",]
    UTSC_Data <- na.omit(UTSC_Data)
    # filter UTM data
    UTM_Data <-  data01[data01$Campus=="UTM",]
    UTM_Data <- na.omit(UTM_Data)
    # filter UTSG data
    UTSG_Data <-  data01[data01$Campus=="UTSG",]
    UTSG_Data <- na.omit(UTSG_Data)

    # calculate response rate for each course
    data_RR<-data01$Responded/data01$Invited
    data_RR<-na.omit(data_RR)

    data_RR_UTSC<-UTSC_Data$Responded/UTSC_Data$Invited
    data_RR_UTSC<-na.omit(data_RR_UTSC)

    data_RR_UTSG<-UTSG_Data$Responded/UTSG_Data$Invited
    data_RR_UTSG<-na.omit(data_RR_UTSG)

    data_RR_UTM<-UTM_Data$Responded/UTM_Data$Invited
    data_RR_UTM<-na.omit(data_RR_UTM)
    # print out the average of the response rate for each campus
    print(paste("Total avg response rate is: ",mean(data_RR)))

    ## [1] "Total avg response rate is:  0.343801101306044"

    print(paste("UTSC avg response rate is: ",mean(data_RR_UTSC)))

    ## [1] "UTSC avg response rate is:  0.335847140407165"

    print(paste("UTM avg response rate is: ",mean(data_RR_UTM)))

    ## [1] "UTM avg response rate is:  0.360746890577574"

    print(paste("UTSG avg response rate is: ",mean(data_RR_UTSG)))

    ## [1] "UTSG avg response rate is:  0.357633288156258"

      g1 <- ggplot(UTSC_Data, aes(x=Term, y=Mean1, color=Course)) +
      geom_point() + 
      geom_smooth(method=lm, se=FALSE, fullrange=TRUE) + theme(axis.text.x = element_text(angle = 90, hjust = 1)) 
      
      g2 <- ggplot(UTSC_Data, aes(x=Term, y=Mean2, color=Course)) +
      geom_point() + 
      geom_smooth(method=lm, se=FALSE, fullrange=TRUE) + theme(axis.text.x = element_text(angle = 90, hjust = 1))
        g3 <- ggplot(UTSC_Data, aes(x=Term, y=Mean3, color=Course)) +
      geom_point() + 
      geom_smooth(method=lm, se=FALSE, fullrange=TRUE) + theme(axis.text.x = element_text(angle = 90, hjust = 1))
          g4 <- ggplot(UTSC_Data, aes(x=Term, y=Mean4, color=Course)) +
      geom_point() + 
      geom_smooth(method=lm, se=FALSE, fullrange=TRUE) + theme(axis.text.x = element_text(angle = 90, hjust = 1))
            g5 <- ggplot(UTSC_Data, aes(x=Term, y=Mean5, color=Course)) +
      geom_point() + 
      geom_smooth(method=lm, se=FALSE, fullrange=TRUE) + theme(axis.text.x = element_text(angle = 90, hjust = 1))
              g6 <- ggplot(UTSC_Data, aes(x=Term, y=Mean6, color=Course)) +
      geom_point() + 
      geom_smooth(method=lm, se=FALSE, fullrange=TRUE) + theme(axis.text.x = element_text(angle = 90, hjust = 1))
              
    ggarrange(g1, g2, g3,g4,g5,g6, 
    ncol = 3, nrow = 3)

![](trial_files/figure-markdown_strict/unnamed-chunk-4-1.png)
