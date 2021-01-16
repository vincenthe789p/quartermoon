import tweepy

consumerKey = "FrfzOFA2n63hhWzyFKjYzt1Vm"
consumerSecret = "o6ysnCuND1qWPgDe36mgId68lJPusRXLGDflIijVwaHihm6aW5"
accessToken = "1339039382037098497-Th7jCwFuDWBPzpEbrG6i0tHEVciMTO"
accessTokenSecret = "CvwF8UvQv9y36uMJL7A8kvI5awB8VsjINyUrcbFdzfC9G"


authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
authenticate.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(authenticate, wait_on_rate_limit = True)



posts = api.user_timeline(screen_name = "BBCAORG", count = 100, lang = "en", tweet_mode = "extended")

print("Show the 5 recent tweets: \n")
i = 1
for tweet in posts[0:50]:
    print(tweet.full_text + "/n")
    print("\n")
