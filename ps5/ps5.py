# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
    
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
    


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError
        
        #assume 'story' is of type NewsStory

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
        
class PhaseTrigger(Trigger):
    
    def __init__(self, phrase):
        self.phrase = phrase
    
    def get_phrase(self):
        return self.phrase
        
    def get_story(self):
        return self.story
    
    def is_phrase_in(self, phrase, story):
        
        phraselist = self.string_to_slist(phrase)
        storylist = self.string_to_slist(story)
                
        
        if phraselist[0] in storylist:
            j = storylist.index(phraselist[0])
        else: return False
        
        try:
            for i in range(len(phraselist)):
                if phraselist[i] != storylist[j+i]:
                    return False
                
                else: pass
        except: return False

        return True
        
    def string_to_slist(self, astring):
        
        astring = astring.lower()
        newstring = ''
        
        for char in astring:
            if char not in string.punctuation:
                newstring += char
            else:
                newstring += ' '
                
        newstring = ' '.join(newstring.split())

        slist = newstring.split(' ')
        
        return slist

# Problem 3
# TODO: TitleTrigger
        
class TitleTrigger(PhaseTrigger):
       
    def evaluate(self, story):
        
        title = story.get_title()
                
        if self.is_phrase_in(self.get_phrase(),title) == True:
            return True
        
        else: return False
    
        

# Problem 4
# TODO: DescriptionTrigger
        
class DescriptionTrigger(PhaseTrigger):
       
    def evaluate(self, story):
        
        description = story.get_description()
                
        if self.is_phrase_in(self.get_phrase(),description) == True:
            return True
        
        else: return False
    


# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
        
class TimeTrigger(Trigger):
    def __init__(self, datestring):
                
        self.datestring = datestring
        
    def get_datestring(self):
        return self.datestring
        
    #get_datetime can be called on any datestring
    
    def get_datetime(self, datestring):
        date_string = self.datestring
        
        date_time = datetime.strptime(date_string, "%d %b %Y %H:%M:%S")
        
        date_time = date_time.replace(tzinfo=pytz.timezone("EST"))

                
        return date_time
    
# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    
    
    def evaluate(self, story):
        
        control = self.get_datetime(self.get_datestring)
    
        test = story.get_pubdate()
        
        #add timezone to test datetime
        test = test.replace(tzinfo=pytz.timezone("EST"))

        if test < control:
            return True
                
        else: return False
        

class AfterTrigger(TimeTrigger):    
    
    def evaluate(self, story):
        
        control = self.get_datetime(self.get_datestring)
    
        test = story.get_pubdate()
        
        #add timezone to test datetime
        test = test.replace(tzinfo=pytz.timezone("EST"))

        if test > control:
            return True
                
        else: return False


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

#This NotTrigger returns True if TitleTrigger returns false & vice versa
class NotTrigger(Trigger):
    
    def __init__(self, TitleTrigger):
        tri
        self.TitleTrigger = TitleTrigger
    
    def evaluate(self, story):
        if self.TitleTrigger.evaluate(story) == True:
            return False
                
        else: return True

# Problem 8
# TODO: AndTrigger
        
#This AndTrigger returns True if TitleTrigger and DescriptionTrigger both return True
        
class AndTrigger(Trigger):
    
    def __init__(self, TitleTrigger, DescriptionTrigger):
        
        self.TitleTrigger = TitleTrigger
        self.DescriptionTrigger = DescriptionTrigger
    
    def evaluate(self, story):
        if self.TitleTrigger.evaluate(story) == True and self.DescriptionTrigger.evaluate(story) == True:
            return True
                
        else: return False        

# Problem 9
# TODO: OrTrigger
        
#This OrTrigger returns True if either TitleTrigger or DescriptionTrigger return True
        
class OrTrigger(Trigger):
    
    def __init__(self, TitleTrigger, DescriptionTrigger):
        
        self.TitleTrigger = TitleTrigger
        self.DescriptionTrigger = DescriptionTrigger
    
    def evaluate(self, story):
        if self.TitleTrigger.evaluate(story) == True or self.DescriptionTrigger.evaluate(story) == True:
            return True
                
        else: return False 

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    
    filtered_list = []
    
    
    for i in range(len(stories)):
        for j in range(len(triggerlist)):
            if triggerlist[j].evaluate(stories[i]) == True:
                filtered_list.append(stories[i])
                
                
    return filtered_list



#======================
# User-Specified Triggers
#======================
# Problem 11
    

def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    
    triggerlist = []
    
    for i in range(len(lines)):
    
        trig = lines[i].split(',')
        
        if trig[0] == 'ADD':
            
            for j, trig in enumerate(trig, start=1):
                triggerlist.append(j)
                
            
        elif 'AND' in trig:
            name = trig[0]
    
            #trig[0].AndTrigger(trig[2],trig[3])
            print(trig[0],trig[2],trig[3])
            triggerlist.append(name)
            
        else: 
            name = trig[0]
    
            if trig[1] == 'TITLE':
                print(trig[0],'title trigger',trig[2])
                
                #name = TitleTrigger (trig[2]) ... syntax update
                #triggerlist.append(name) 
            
            elif trig[1] == 'DESCRIPTION':
                print(trig[0],'description trigger',trig[2])
                
            elif trig[1] == 'AFTER':
                print(trig[0],'after trigger',trig[2])
            
            elif trig[1] == 'BEFORE':
                print(trig[0],'before trigger',trig[2])

            elif trig[1] == 'NOT':
                print(trig[0],'not trigger',trig[2])
                
            elif trig[1] == 'AND':
                print(trig[0],'and trigger',trig[2])

            elif trig[1] == 'OR':
                print(trig[0],'or trigger',trig[2])


            
    #return triggerlist                

    print(lines) # for now, print it so you see what it contains!


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

