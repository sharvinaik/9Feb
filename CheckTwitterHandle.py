import tweepy
from tweepy import OAuthHandler

def checkTwitterID(user):
    consumer_key = "01bslizkj9aza9UCsu82vA6ci"
    consumer_secret = "M6Zt7ntZGD8Pua1NSe9m4qhBWeD5GjWTuMk4iKexZ5lPDY0zoV"
    access_key = "850580974702297089-j9VbB2nfG8MIV3gDM2iLeF1NGB3JSx5"
    access_secret = "C8UEGhS3fJq3Kh1a1XIQlKCFbeLSdiDr4kY9n7s9eNmfG" 

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    flag = 0
    try:
        u = api.get_user(x)
        print (u.id_str)
        print (u.screen_name)
        flag = 0
    except Exception:
        print("Error User name doesn't exists")
        flag  = 1
    if flag == 0:
        return True
    else:
        return False
