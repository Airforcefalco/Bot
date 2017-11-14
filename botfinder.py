# -*- coding: utf-8 -*-
import sys
import praw
import bot_functions as b
import config as c
import json
import data_storage as d
import sentence_splitter as ss
import re

from matchedusers import *

#from importlib import reload

#reload(sys)
#sys.setdefaultencoding('utf8')

def authenticate():
    print('Authenticating...\n')
    c.reddit = praw.Reddit('bot1')
    print('Authenticated as {}\n'.format(c.reddit.user.me()))
    #Header for terminal output
    print('comments scanned\tcomments per second\t\tsubmissions scanned\t\tsubmissions per second')

def main():
	authenticate()
	#c.scanned_comments = d.read_json(c.COMMENTS_SAVED_PATH)
	for sub in c.subreddits_to_scan:
		b.subreddit_submissions(sub)
	b.cleanup()
	data = d.read_json(c.COMMENTS_SAVED_PATH)
	#print(json.dumps(c.scanned_comments, sort_keys = True, indent = 4))
	return data

def sentence(post):
	sentences = ss.split_into_sentences(post)
	return sentences

def file_scanner(user, users_sentence, data):
	for each_user in data:
		c.count += 1
		if each_user != user:
			# This checks comments based on how many comments they made 
			if len(data[each_user]) > 1:
				scanned_comments = data[each_user]
				for each_comment in scanned_comments:
					scanned_comment = sentence(scanned_comments[each_comment])
					for each_sentence in scanned_comment:
						if len(each_sentence) > 20:
						# print("$$$$$$$$$$$")
						# print(each_sentence)
						# print(users_sentence)
						# print("**************")
							if users_sentence == each_sentence:
								match = MatchedUsers(user, each_user, each_comment, users_sentence)
								return match
		if c.count % 1000000 == 0:
			print(c.count)

if __name__ == '__main__':
	all_comments = main()
	print(b.get_status_string())
	results = {}
	matches = 0
	for each_user in all_comments:
		# This checks comments based on how many comments they made 
		if len(all_comments[each_user]) > 3:
			c.user_that_scanned += 1
			users_comments = all_comments[each_user]
			for each_comment in users_comments:
				sentences = sentence(users_comments[each_comment])
				for each in sentences:
					if len(each) > 20:
						hold = file_scanner(each_user, each, all_comments)
						if isinstance(hold, MatchedUsers):
							hold.comment_ids.append(each_comment)
							results[matches] = hold
							matches += 1
	print("Done!\n")
	print(matches)
	print(c.count)
	print(c.user_that_scanned)
	print(c.num_scanned)
	print()
	for each in results:
		print(each)
		results[each].get_redditor_ids()
		results[each].get_comment_links()
		print(results[each])