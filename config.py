# -*- coding: utf-8 -*-
from collections import defaultdict

DATA_DIR = 'data/'
COMMENTS_SAVED_PATH = DATA_DIR + 'comments_saved.json'
LOG_PATH = DATA_DIR + 'log.json'

#subreddits_to_scan = ['politics', 'news', 'bestof', 'sadcringe', 'drumpf', 'impeach_trump', 'conservative', 'hillaryclinton' 'worldnews', 'the_donald', 'cringeanarchy','latestagecapitalism', 'Enoughtrumpspam', 'Libertarian', 'neoliberal', 'nottheonion', 'politicalhumor', 'facepalm', 'twoxchromosomes', 'iamverysmart',  'blackpeopletwitter', 'esist', 'fuckthealtright', 'technology', 'againsthatesubreddits', 'antitrumpalliance', 'bannedfromthe_donald', 'BlueMidterm2018', 'Delete_the_donald', ]
subreddits_to_scan = ['politics', 'news', 'worldnews', 'the_donald']
scanned_comments = {}
reddit = ''
count = 0
num_scanned = 0
user_that_scanned = 0