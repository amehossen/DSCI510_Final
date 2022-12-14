#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:06:02 2022

@author: amehossen
"""
import requests 
import json
import pandas as pd 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import matplotlib.pyplot as plt 
import numpy as np 

def find_food(location: str, n) -> list:
    url = 'https://api.yelp.com/v3/businesses/search'
    querystring = {
    "location":location,
    "categories": "food",
    #"sorted by": "rating"
    "limit": 10
    }
    headers = {
	"Authorization": "Bearer 28Vdm5unvcF2eREFQ9EALBwceVKaEimHnq61xdcSBpHxYl5R4dvDmDZUXCFsVsu8dvjrGh3QxQR7J45Ypw7kvu9wT_S5DIneUobrst89ioh_HJsX8Eb696AWJ1RkY3Yx",
    }
    response = requests.get(url, headers=headers, params=querystring).json()
    ratings = response["businesses"] #top 10 businesses of a location 
    return ratings 

    
def find_tweet(name:str) -> list:
    url = "https://api.twitter.com/2/tweets/search/recent"
    querystring = {
    "query":name
    } 
    

    headers = {
	"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAERzUwEAAAAAt7fYxbA7j2P4n7R80nlo9GvnVUc%3DNFjB0C9tMJ1BjrhHr7AHj6p56d2Ux0EnKeS0a7pVJNdE55BfQY",
    }
    tweets = requests.get(url, headers=headers, params=querystring).json()
    return tweets

def get_avg_score(tweets):
    scores_sum = 0
    for tweet in tweets['data']:
        tweet = tweet['text']
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(tweet)
        scores_sum += ss['compound']
    return scores_sum / len(tweets['data'])
        




if __name__ == "__main__":
    # build list of locations to look at 
    locations = ['Los Angeles'] #put in 10 cities 
    ratings = []
    scores = []
    for location in locations:
        restaurants = find_food(location,10)
        #print(restaurants)
        for restaurant in restaurants: 
            keyword = '"'+restaurant['name']+'"'
            tweets = find_tweet(keyword)
            print(tweets)
            if 'errors' in tweets: 
                print('There was an error with',keyword)
                print(tweets['errors'])
            if 'data' in tweets: 
                #print(tweets)
                score = get_avg_score(tweets)
                scores.append(score)
                rating = restaurant['rating']
                ratings.append(rating)
    print(ratings)
    print(scores)
    plt.scatter(ratings,scores)
        #calculate equation for trendline
    z = np.polyfit(ratings,scores, 1)
    p = np.poly1d(z)
    
    #add trendline to plot
    plt.plot(ratings, p(ratings))
    plt.xlabel("Restaurant Ratings")
    plt.ylabel("Tweet Sentiments")
    plt.title("Ratings versus Sentiments")
    plt.show()
            
            
    #get top restaurants for each location 
    #ratings = find_food(location)
    #restaurantdf = pd.DataFrame.from_dict(ratings) #converting json to df
    #restaurantdf.to_csv("restaurant.csv")#converting df to csv
    #print(ratings[0]['name'])
    #tweets = find_tweet(location, ratings[0]['name'])
    #tweetsdf = pd.DataFrame.from_dict(tweets['data']) #converting json to df
    #tweetsdf.to_csv("restauranttweets.csv") #converting
    #print(tweets)
    
    
    