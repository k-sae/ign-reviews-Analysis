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
title, score, platform
```

2- [Video Game Sales](https://www.kaggle.com/gregorut/videogamesales)

columns of interest:
```
title, Platform, Global Sales
```
### Testing mapper and reducer
- `merger`
```
    #command will be added later
```

### steps

1- to merge the two dataset in order to fetch the sales of each game title and it's score 
- use this hadoop commands to start the process on the mapper and reducer in _`merger`_ package

```
#commands will be added on 12/12/2017
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
#commands will be added on 12/12/2017
```

## Output 
```
this section will Contain the output
```


### observation
```
this section will Contain the observation
```

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details


