from instapy import InstaPy


session = InstaPy(username="Your IG Username", password="Your IF Password") #,, headless_browser=True)
session.login()

session.set_relationship_bounds(enabled=True, max_followers=3000) # Ignore users with >3000 followers
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21) # Sets limit to avoid IG ban 


# session.set_dont_like(["iot", "bot"])
# session.set_do_follow(True, percentage=25)
session.set_do_comment(True, comment_liked_photo=True, percentage=50)

comments = ["The pace of progress in artificial intelligence is incredibly fast.",
"I believe that artificial intelligence we'll augment our intelligence.",
"Machine learning is set to automate jobs that most people thought could only be done by people.",
"Computers are able to see, hear and learn.  Welcome to the future."]

session.set_comments(comments)

session.like_by_tags(["coding", "datascience", "ai"], amount=1)
session.end()
