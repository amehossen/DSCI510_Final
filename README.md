# DSCI510_Final
# Dependencies 
 matplotlib == 3.5.1
nltk == 3.7
numpy == 1.21.5
pandas == 1.4.2
requests == 2.27.1
scipy == 1.7.3
session_info == 1.0.0
# Running Project 
To reproduce my results on Jupyter Notebook, please Cell → Run All 
The respective file has been uploaded to this github
# Data Sources 
The data sources I have utilized for my project include leveraging Yelp’s powerful API to assist my determination of a restaurant’s overall rating and the general sentiment of the establishment, presented through the website. Additionally, I also utilized Twitter’s API to collect and read twitter data, including tweets regarding the top 10 restaurants in the aforementioned cities. I collected a sample of 3534 tweet samples from the website to determine the average sentiment the general public had shared online regarding these popular establishments. These tweets are composed of the top 50 restaurants, finding the 100 most recent tweets mentioning the restaurant from the cities: Los Angeles, Miami, San Francisco, Chicago and New York City. My goal was to pinpoint how these consumers felt on Twitter and compare that to the sentiments and reviews Yelp was pushing to its viewers. 
I fetched the data through Yelp API in json format, then converted it to a csv. I queried this data through the querystring = { "location":location, "categories": "food", "sorted by": "rating" } for Yelp and querystring = { "query":name } for Twitter. The saved data files are CSV. For the all_tweets file (Twitter data), the schema of the file has 3534 rows and the column titles: edit_history_tweets_ids, id and text. The all_restaurants file’s (Yelp data) schema has 249 rows and the column names: id, alias, name, image_url, is_closed, url, review count, categories, ratings, coordinates, transactions, price, location, phone, display_phone and distance. 
#Challenges & Changes 
My initial plan for this project was vastly different from the project I am presenting now. In the beginning, I planned on examining if the biggest food influencers’ reviews have altered the trajectory of a restaurant’s performance or their most popular dishes through comparing @TomSietsema’s twitter data to general sentiments expressed by the public on a restaurant’s Yelp page. I planned on collecting at least 1,000 tweet samples from Tom to determine whether or not his opinion had an influence on the actual restaurant’s performance. My goal was to pinpoint the frequency of a dish being ordered, general sentiment and overall rating before and after Tom Sietsema’s review of the aforementioned to truly pinpoint the impact of his critiques. But, in focusing on such a niche food blogger, I had met challenges in the realm of restaurant location, and being able to pinpoint these exact restaurants Tom had tweeted about, on Yelp. I was also unable to query substantial tweets for location-based restaurants on Twitter, from the general public, and thus concluded that this project would be infeasible to carry out, or if it had been carried out, that the conclusion would not be useful personally or professionally in the culinary industry, as I had hoped my project’s conclusion would be. Instead, I chose to restructure my project to revolve around finding if there is a correlation between the public’s sentiment of a restaurant, expressed via Twitter, and how these scores could compare to the restaurant’s Yelp ratings. This project’s data was more abundant, fruitful and straightforward and provided me the foundation to build a meaningful project upon. 
# Analysis 
The analysis I have performed on the data I have obtained can be referred to in three parts.
 a. First, I imported and utilized the nltk library to perform sentiment analysis on the tweets I obtained through Twitter’s API. The dataset this sentiment analysis was performed on is the csv file all_tweets. Since tweets are not numerical, I chose to utilize the sentiment analysis package to transform categorical data into numerical data, allowing me to perform subsequent statistical analyses on the extracted data. 
b. Then, I continued to build upon this analysis by utilizing the scipy package to perform statistical analysis on the aforementioned datasets (all_tweets and all_restaurants). I chose to calculate the pearson’s correlation coefficient and the p-value (statistical significance) of my project to display. The first number is the R value (Pearson's correlation coefficient), while the second is the p-value.
c. Lastly, for ease of visualizing the correlation of my outputs, I chose to plot Yelp review ratings against average Twitter sentiment ratings on a scatter plot with a trend line, as well as generating a histogram of average Twitter sentiment scores to emphasize the lack of correlation between Yelp reviews of these popular restaurants and the general public’s sentiment regarding these establishments on Twitter. 
# Visualization 
The respective visualization for my methodology above is as follows: 
Statistical Analysis: ![image](https://user-images.githubusercontent.com/119716044/207749292-1cc45fdd-5009-4715-afd2-7f8b86536080.png)
Histogram:![image](https://user-images.githubusercontent.com/119716044/207749376-156a73c8-821b-4142-aa74-568da842f323.png)
Scatterplot: ![image](https://user-images.githubusercontent.com/119716044/207749398-c6b65c71-f2af-48b0-a4b8-3c5fae64b9cc.png)
# Conclusion 
The conclusion I have garnered from this project is that there absolutely does not exist a correlation between Yelp review ratings and average sentiment of these restaurants on Twitter by the general public. This is supported by the low, but positive, R value, showing that there is not a strong relationship between the two variables, as well as the high p-value which indicates that there is not a statistically significant relationship between Yelp reviews and Twitter sentiments.
# Future Work 
If I were to have more time, a direction I would take to improve the results of my project would be to further analyze the validity of Yelp reviews. As seen in my project, despite the high ratings for the restaurants, there exists a weak negative correlation between public sentiment and the restaurants reviews, which indicates that Yelp is not showing reviews that are reflective of what people actually think the restaurant’s quality is. This can be troublesome for consumers who are seeking a good dining experience from popular establishments. Thus, I would like to dive deeper into this research problem by examining if the displayed reviews on Yelp are skewed by sponsorships or paid critics, both of which are troubling and may jeopardize the culinary industry in the future by eliminating consumer trust in establishments. 


