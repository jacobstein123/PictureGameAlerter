import praw
import winsound
import time
r = praw.Reddit('Picture Game Alerter')
sub = r.get_subreddit('picturegame')

UNSOLVED = "UNSOLVED"
ROUND_OVER = "ROUND OVER"
state = ROUND_OVER

while 1:
    post_list = sub.get_new(limit=1)
    new_post = post_list.next()
    if "UNSOLVED" in new_post.link_flair_text:
        if state == ROUND_OVER:
            winsound.Beep(440,150);winsound.Beep(440,150);winsound.Beep(440,150)
    elif state == UNSOLVED:
        winsound.Beep(440,150);winsound.Beep(440,150);winsound.Beep(440,150)
    state = new_post.link_flair_text
    time.sleep(10)
