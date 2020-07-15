import csv

def get_hashtags(hashtag_list = []):
    with open('hashtags.csv', 'r', encoding='utf-8-sig') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            data = ', '.join(row)
            hashtag_list.append (data)
    print (hashtag_list)
    return hashtag_list