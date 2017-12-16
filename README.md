# IGN-Reviews Analysis

the aim is to know how IGN reviews impact the sales of video games
in the last 20 years

## what is [IGN](http://me.ign.com/en/)

[![N|Solid](https://superrepo.org/static/images/icons/original/xplugin.video.ign_com.png.pagespeed.ic.mp10cLVn3C.png)](http://me.ign.com/en/)

IGN is on of the largest video game reviewing site, where many video gamers consider visiting it before purchasing any game

### Datasets 
1- [20 Years Of Games Analysis](https://www.kaggle.com/ash316/20-years-of-games-analysis)

columns of interest:

```
title, score
```

2- [Video Game Sales](https://www.kaggle.com/gregorut/videogamesales)

columns of interest:
```
title, Platform, Global Sales
```
### Testing mapper and reducer

- `merger`
```
cat datasets/merger/dataset_min.csv  | python3 main/merger/mapper.py | sort -k1,1 | python3 main/merger/reducer.py 
```

### Hadoop Analysis Steps

1- merge the two dataset in order to fetch the sales of each game title and it's score 
- use this hadoop commands to start the process on the mapper and reducer in _`merger`_ package

```
hadoop dfs -mkdir -p /user/$USER/ign-reviews

# project directory as the working directory
hadoop dfs -put datasets/merger/ /user/$USER/ign-reviews

#use always an absolute path for mapper and reducer 
hadoop jar $HADOOP_STREAMING_HOME/hadoop-streaming-2.8.1.jar\
-input /user/$USER/ign-reviews/merger\
-output /user/$USER/ign-reviews/merger/out\
-mapper $PROJECT_FOLDER/main/merger/mapper.py\
-reducer $PROJECT_FOLDER/main/merger/reducer.py


```

2- next step is to get the average sold game copies for each score 

ex output:
```
score   sales
10      20m
9       15m
```
 - ``in this example 10 had an average of 20 mil sold copy  `` 
 - ``then the score had an high impact on the sales proccess``
 
- we will use the output file resulted from this first process as our dataset for the next step

- this time i will use the mapper and reducer from the ``analyzer`` package
```
hadoop dfs -mkdir -p /user/$USER/ign-reviews/analyzer

# project directory as the working directory
hadoop dfs -put datasets/merger/titles-scores-sales.csv

# change the sort method since the default one mixing the 10 and 1
hadoop jar $HADOOP_STREAMING_HOME/hadoop-streaming-2.8.1.jar\
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator\
-D  mapred.text.key.comparator.options=-n\
-input /user/$USER/ign-reviews/analyzer\
-output /user/$USER/ign-reviews/analyzer/out\
-mapper $PROJECT_FOLDER/main/analyzer/mapper.py\
-reducer $PROJECT_FOLDER/main/analyzer/reducer.py


```

## Output 

```
1	0.16125
2	0.334047619048
3	0.330053475936
4	0.47115942029
5	0.610474516696
6	0.709524390244
7	1.24264754098
8	1.5580347277
9	3.00887711864
10	10.5872727273

```


### observation

- the relation is strongly linear dependant which lead us to the conclusion that sales and reviews are strongly dependant
- score of 10 has a very high value with respect to the others this resulted from the presence of outlier (GTA V
with sales of 55 million copy)

### Code Explaination

## merger

`mapper`:

the mapper check the 4th column to identify whether the line is from dataset 1 or 2 
then print the line on std out after getting the column of interest

`Reduccer`:

the reducing proccess is litte bit more tricky
- first step is to identify the line's dataset 
- then accumelate the sales of certain title 
- then get the average score of that title 
- lastly make sure there is no missing data to avoid noise

## analyzer

`mapper`:

the mapper this time is ignoring the title and setting the score as the key for the process

`Reduccer`:

- accumulate the sales for each score then get the mean of each score


### usefull hadoop commands

`for folder deleting`

```
hadoop fs -rm -r -f $folder_name
```

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details


