# -*- coding: utf-8 -*-
import config as c
import time
import data_storage as d
import praw


status_data = {
	'time_started':time.time(),
	'num_scanned_comments':0,
	'num_scanned_submissions':0,
	'avg_scanned_comments_per_second':0,
	'avg_scanned_submissions_per_second':0
}

def get_status_string():
	t = ''
	for key in ['num_scanned_comments','avg_scanned_comments_per_second','num_scanned_submissions','avg_scanned_submissions_per_second']:
		t += str(round(status_data[key],1)) + '\t\t\t\t\t'
	return t + '\t\t\t\n'

def update_status_data(key):
	if key == 'comment' or key == 'submission':
		num_key = 'num_scanned_' + key + 's'
		avg_ps_key = 'avg_scanned_' + key + 's_per_second'
		status_data[num_key] += 1
		status_data[avg_ps_key] = status_data[num_key] / (time.time() - status_data['time_started'])

def comment_scanner(submiss):
	submiss.comments.replace_more(limit = 10, threshold = 3)
	tmp = {}
	for comment in submiss.comments.list():
		try:
			if comment.author.name == 'AutoModerator':
				update_status_data('comment')
				continue
			if comment.author.name in tmp.keys():
				tmp[(comment.author.name)][comment.id] = comment.body
			else:
				tmp[comment.author.name] = {comment.id: comment.body}
			update_status_data('comment')
		except:
			pass
	print(get_status_string())
	return tmp

def subreddit_submissions(a_subreddit):
	#c.scanned_comments[a_subreddit] = {}
	for submissions in c.reddit.subreddit(a_subreddit).top('month', limit = 5):
		c.scanned_comments.update(comment_scanner(submissions))
		#c.scanned_comments[a_subreddit][submissions.id] = comment_scanner(submissions)
		update_status_data('submission')
	for controversial_submissions in c.reddit.subreddit(a_subreddit).controversial('month', limit = 5):
		c.scanned_comments.update(comment_scanner(controversial_submissions))
		update_status_data('submission')


def cleanup():
	# Comment out the first three lines to reset file.
	# tmp = {}
	# tmp = d.read_json(c.COMMENTS_SAVED_PATH)
	# c.scanned_comments.update(tmp)
	d.writeto_json(c.COMMENTS_SAVED_PATH, c.scanned_comments)