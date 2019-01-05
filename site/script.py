# -*- coding: utf-8 -*

import sys
import sqlite3
import tweepy
import datetime
import logging


def get_list(date):
    date = "%%%%" + date[4:]
    result = []
    conn = sqlite3.connect('databases/birthday.db')
    try:
        c = conn.cursor()
        c.execute('SELECT * FROM birthday WHERE birthday LIKE ? AND country = "France"', (date,))
        result = c.fetchall()
    except sqlite3.Error as e:
        logging.error("SQLite Error:" + e.args[0])
    conn.close()
    return result


def process(users):
    queue = []
    with_account = []
    without_account = []
    for user in users:
        if len(user[2]) > 0:
            with_account.append((user[1].strip(), user[2]))
        else:
            without_account.append(user[1].strip())

    for user, acc in with_account:
        txt = "Aujourd'hui est un jour important, c'est l'anniversaire de {}. Joyeux anniversaire {} ! \N{birthday cake}".format(
            user, acc)
        queue.append(txt)

    txt = "Et c'est aussi l'anniversaire de :\n{}".format(
        "".join([" - " + x + "\N{birthday cake}" + "\n" for x in without_account]))
    queue.append(txt)
    return queue


def post(tweets, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    try:
        for txt in tweets:
            api.update_status(txt)
            logging.info(txt)
    except:
        logging.error(txt)

def getKey():
    logs = {}
    with open("key.txt", "r") as f:
        for line in f:
            key, value = line.split(":")
            logs[key] = value.rstrip('\n')
    return logs

if __name__ == "__main__":
    LOG_FILENAME = 'status.log'
    logging.basicConfig(filename=LOG_FILENAME, format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)

    today = datetime.datetime.now().strftime("%Y-%m-%d")

    logging.info('Querying list of celebrities')
    list_user = get_list(today)
    if len(list_user) == 0:
        logging.info('List is empty')
        sys.exit()

    logging.info('Parsing list of celebrities (len = {})'.format(len(list_user)))
    list_tweets = process(list_user)
    logging.info('Posting message (total : {})'.format(len(list_tweets)))
    login = getKey()
    post(list_tweets, **login)
    logging.info('Script finalized with success')
