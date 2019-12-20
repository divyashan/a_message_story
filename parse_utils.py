from textblob import TextBlob
from bs4 import BeautifulSoup
import os
import numpy as np

#Parse out important info
def reaction_check(msg):
    # TODO: return actual reaction
    reaccs = msg.findAll('ul', recursive=True)
    if len(reaccs):
        return True
    return ""

def sticker_check(msg):
    stickers = msg.findAll('img', recursive=True)
    if len(stickers):
        return True
    return False

def get_sentiment(msg):
    return TextBlob(msg).sentiment.polarity

def map_to_month_no(date_str):
    month = date_str[:3]
    month_no_map = {'Jan': 1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 
                    'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
    return month_no_map[month]

def get_message_files_path(threads_dir, sender2):
    thread_names = os.listdir(threads_dir)
    rel_thread_names = [thread_name for thread_name in thread_names if (sender2.replace(' ', '') in thread_name)]
    rel_thread_sizes = [len(os.listdir(threads_dir + '/' + thread_name)) for thread_name in rel_thread_names]

    thread_name = rel_thread_names[np.argsort(np.array(rel_thread_sizes))[-1]]
    return threads_dir + '/' + thread_name
