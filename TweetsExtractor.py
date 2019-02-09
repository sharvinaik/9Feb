from __future__ import print_function
import pandas as pd
from sklearn import tree
import tweepy
import time
import os
import json
import sys
from watson_developer_cloud import PersonalityInsightsV3
from MovieClassifier import movieRecommendation
from MusicClassifier import musicRecommendation
from JobClassifier import jobRecommendation
from BookClassifier import bookRecommendation

class PersonalityInsights:
    def __init__(self):
        self.settings = self.loadSettings()
        if self.settings == None:
            # No settings no deal
            exit(0)
        self.access_key = self.settings["twitter_access_key"]
        self.access_secret = self.settings["twitter_access_secret"]
        self.consumer_key = self.settings["twitter_consumer_key"]
        self.consumer_secret = self.settings["twitter_consumer_secret"]        
        self.pi_url = self.settings["watson_pi_url"]
        self.pi_apikey = self.settings["watson_iam_apikey"]
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        
        self.auth.set_access_token(self.access_key, self.access_secret)
        self.twitter_api = tweepy.API(self.auth)

    def loadSettings(self):
        if(os.path.exists("settings.json")):
            with open("settings.json", "r") as settings:
                try:
                    jsonSettings = json.loads(settings.read())
                    # We need to verify all needed fields are present
                    requiredKeys = ["twitter_access_key", "twitter_access_secret", "twitter_consumer_key", "twitter_consumer_secret", "watson_pi_url", "watson_iam_apikey"]
                    for key in requiredKeys:
                        if not key in jsonSettings.keys():
                            print("Settings is missing key: \"%s" % key + "\". Please add it in to continue!")
                            return None
                    return jsonSettings
                except Exception as e:
                    print("Could not read settings file, make sure it is formatted correctly!")
                    return None
                    
        else:
            print("Could not find settings.json, cannot continue!")
            return None

    def pullTweets(self,sc_nm):
        max_id = None
        statuses = []
        for x in range(0, 16):  # Pulls max number of tweets from an account
            if x == 0:
                statuses_portion = self.twitter_api.user_timeline(screen_name=sc_nm, count=200, include_rts=False)
                status_count = len(statuses_portion)
                # get id of last tweet and bump below for next tweet set
                max_id = statuses_portion[status_count - 1].id - 1
            else:
                statuses_portion = self.twitter_api.user_timeline(screen_name=sc_nm, count=200, max_id=max_id, include_rts=False)
                status_count = len(statuses_portion)
                try:
                    # get id of last tweet and bump below for next tweet set
                    max_id = statuses_portion[status_count - 1].id - 1
                except Exception:
                    pass
            for status in statuses_portion:
                statuses.append(status)


        print('Number of Tweets user have: %s' % str(len(statuses)))
        return statuses

    def convert_status_to_pi_content_item(self, s):
        return {
            'userid': str(s.user.id),
            'id': str(s.id),
            'sourceid': 'python-twitter',
            'contenttype': 'text/plain',
            'language': s.lang,
            'content': s.text,
            'created': str(int(time.time())),
            'reply': (s.in_reply_to_status_id is None),
            'forward': False
        }

    def printFormatted(self, jsonData, user):
        interested_traits = ["personality"]   
        traits = []     
        for trait in interested_traits:
            trait_data = jsonData[trait]
            for extra_data in trait_data:
                if trait == "personality":
                    #print("\t %s" % extra_data["name"] + " -> %s" % extra_data["percentile"])
                    traits.append(float(str(extra_data["percentile"])))
        return traits
    def watsonSubmission(self, statuses, user):
        pi_content_items_array = list(map(self.convert_status_to_pi_content_item, statuses))
        pi_content_items = {'contentItems': pi_content_items_array}

        personality_insights = PersonalityInsightsV3(
            version='2017-10-13',
            iam_apikey='ffEc4QumFvMhXsr5cQjCB8-KHIkYdrK7qJx6ASycI_rR',
            url=self.pi_url
        )
        profile = personality_insights.profile(pi_content_items, content_type='application/json',consumption_preferences=True, raw_scores=True).get_result()
        traits = self.printFormatted(profile, user)
        return traits     
    
    def getRecommendations(self, traits):
        # MOVIES
        movies = movieRecommendation(traits)
        # for i in range(0, 5):
        #     for m in movies[i]:
        #         print(m['title'])

        #JOBS
        # job = jobRecommendation(traits)
        # for j in job:
        #     print(j[0], " :: ", j[1])  

        #BOOKS
        # book = bookRecommendation(traits)
        # for b in book:
        #     print(b[0], " :: ", b[1])     
        
        #MUSIC
        # music = musicRecommendation(traits)
        # for i in range(0, 5):
        #     for m in music[i]:
        #         print(m['title'])
        return movies        
        
