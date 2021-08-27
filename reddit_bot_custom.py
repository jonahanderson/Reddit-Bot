#!/usr/bin/python
import praw
import random
import time
import datetime

#Enter your correct Reddit information into the variable below

userAgent = ''

cID = ''

cSC= ''

userN = ''

userP =''

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

subreddit = reddit.subreddit('cryptocurrency') #any subreddit you want to monitor

start_time = time.time() # this will make sure to only look at new submissions after the stream starts

for submission in subreddit.stream.submissions(): 
#for submission in subreddit.hot(limit=100):

	if not submission.saved:
		if not submission.created_utc < start_time:


			numFound = numFound + 1
			
			print(" ")

			print('*NEW SUBMISSION*') #replies and outputs to the command line

			print("Title: ", submission.title)

			print(" ")

			print("Text: ", submission.selftext)
			
			print(" --- ")

			print("Karma: ", submission.score)

			print("SUBMISSION ID: ", submission.id)

			print("SUBMISSION SAVED?: ", submission.saved)

			print("DATE AND TIME: ", datetime.datetime.fromtimestamp(int(submission.created)).strftime('%Y-%m-%d %H:%M:%S'))
			
			print(" --- ")
			
			x = input("Enter your comment: ")
			
			print(" ")

			if x == ("SKIP"):
				submission.save()
				print("SKIPPING THIS POST")
				

			else: 
				print('Posting Comment: ', x)

				submission.reply(x)
				submission.save()
				
				print("")
				print("Comment Posted")
				print("")

			print('GOING TO NEXT POST')

			print("NEW POST -------------------------------------------------------------------------------------- NEW POST")


	else:
		pass
if numFound == 0:

	print()

	print("Sorry, didn't find any posts with those keywords, try again!")
