import config as c

class MatchedUsers(object):

	def __init__(self, user_scanned, user_matched, comment_ids, sentence):
		"""Class to hold matched users"""
		self.user_scanned = user_scanned
		self.user_matched = user_matched
		self.comment_ids = [comment_ids]
		self.sentence = sentence

	def __str__(self):
		self.get_redditor_ids()
		self.get_comment_links()
		return u'User Scanned:\t%s\t\t\t\tUser ID:\t%s\nUser Matched:\t%s\t\t\t\tUser ID:\t%s\nMatched Sentence:\t%s\nLink Matched:\t%s\nLink Scanned:\t%s\n' \
		% (self.user_scanned, self.user_scanned_id, self.user_matched, self.user_matched_id,
		self.sentence, self.scanned_comment_link, self.matched_comment_link)

	def get_redditor_ids(self):
		self.user_scanned_id = c.reddit.redditor(self.user_scanned).id
		self.user_matched_id = c.reddit.redditor(self.user_matched).id

	def get_comment_links(self):
		self.scanned_comment_link = c.reddit.comment(self.comment_ids[0]).permalink
		self.matched_comment_link = c.reddit.comment(self.comment_ids[1]).permalink