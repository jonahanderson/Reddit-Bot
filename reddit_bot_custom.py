#!/usr/bin/python
import praw
import random
import time
import datetime

#Enter your correct Reddit information into the variable below

userAgent = 'cryptotime'

cID = '5m836AlAJTTDfCL9dtJxfA'

cSC= 'iZA8k8o7sj93LOcInTxIRzQRG8YzJA'

userN = 'justjoner'

userP ='G0pher10!'

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

subreddit = reddit.subreddit('cryptocurrency') #any subreddit you want to monitor

start_time = time.time() # this will make sure to only look at new submissions after the stream starts

for submission in subreddit.stream.submissions(): 
#for submission in subreddit.hot(limit=100):

	if not submission.saved:
		if not submission.created_utc < start_time:


			numFound = numFound + 1

			print('Bot replying to: ') #replies and outputs to the command line

			print("Title: ", submission.title)

			print(" ")

			print("Text: ", submission.selftext)

			print("Score: ", submission.score)

			print("SUBMISSION ID: ", submission.id)

			print("SAVED???: ", submission.saved)

			print(datetime.datetime.fromtimestamp(int(submission.created)).strftime('%Y-%m-%d %H:%M:%S'))
			
			x = input("Some input please: ")

			if x == ("SKIP"):
				submission.save()

			else: 
				print('Bot saying: ', x)

				submission.reply(x)
				submission.save()

			print('GOING NEXT')

			print("NEW POST ------------------------------------------------ NEW POST")


	else:
		pass
if numFound == 0:

	print()

	print("Sorry, didn't find any posts with those keywords, try again!")