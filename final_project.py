#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:06:02 2022

@author: amehossen
"""
import requests 
import json
import pandas as pd 

def find_food(location: str) -> list:
    url = 'https://api.yelp.com/v3/businesses/search'
    querystring = {
    "location":location,
    "categories": "food",
    "sorted by": "rating"
    }
    headers = {
	"Authorization": "Bearer 28Vdm5unvcF2eREFQ9EALBwceVKaEimHnq61xdcSBpHxYl5R4dvDmDZUXCFsVsu8dvjrGh3QxQR7J45Ypw7kvu9wT_S5DIneUobrst89ioh_HJsX8Eb696AWJ1RkY3Yx",
    }
    response = requests.get(url, headers=headers, params=querystring).json()
    ratings = response["businesses"][:10] #top 10 businesses of a location 
    return ratings 

    
def find_tweet(location: str, name:str) -> list:
    url = "https://api.twitter.com/2/tweets/search/recent"
    querystring = {
    "query":name
    } 
    

    headers = {
	"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAN6ciwEAAAAAPScXDOC3s4UdKe1owiT%2BQwR%2FRxg%3D8RcetPfN8RKQVjqLovxXfc4UAqsuW2KG12hhRRdD6RHJGRGrE3",
    }
    tweets = requests.get(url, headers=headers, params=querystring).json()
    return tweets




if __name__ == "__main__":
    # build list of locations to look at 
    location = 'Los Angeles'
    #get top restaurants for each location 
    ratings = find_food(location)
    restaurantdf = pd.DataFrame.from_dict(ratings) #converting json to df
    restaurantdf.to_csv("restaurant.csv")#converting df to csv
    print(ratings[0]['name'])
    tweets = find_tweet(location, ratings[0]['name'])
    tweetsdf = pd.DataFrame.from_dict(tweets['data']) #converting json to df
    tweetsdf.to_csv("restauranttweets.csv") #converting
    print(tweets)
    
    
    