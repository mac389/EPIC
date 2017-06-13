#!/usr/bin/env python
import json, tweepy, string, os

from getpass import getpass
from textwrap import TextWrapper
from datetime import datetime
from optparse import OptionParser

#---Define constants for more legible code
READ = 'rb'
WRITE = 'wb'
CURRENT_DIRECTORY = '.'
START_FILE = '['
CLOSE_FILE = ']'
TAB = '\t'
NEWLINE = '\n'
#-----------------------------------------

#----Context-specific code----------------
START_AGE = 12
STOP_AGE = 40
keywords= ['%d years old'%age for age in range(START_AGE,STOP_AGE+1)]
#-----------------------------------------

#----Parse command line options-----------
op = OptionParser()
op.add_option('--o', dest='output', type='str',default=CURRENT_DIRECTORY, 
      help='path to output to')
op.add_option('--m', dest='mode', type='str',default='filter', 
      help='mode of acquisition-- SAMPLE or filter')

op.print_help()
opts,args = op.parse_args()
if len(args) > 0:
      op.error('This script only takes arguments preceded by command line options.')
      sys.exit(1)
#----------------------------------------
directory = json.load(open('directory.json',READ))

if os.path.isdir(opts.output):
    output_file_name = os.path.join(opts.output,'record-%s.json'%(datetime.now().strftime('%Y-%m-%d-%H')))
else:
    dirname,_ = os.path.splitext(opts.output)
    output_file_name = os.path.join(dirname,'record-%s.json'%(datetime.now().strftime('%Y-%m-%d-%H')))

file_handle = open(output_file_name,WRITE)
file_handle.write('[')

def partition(enumerable,criterion):
    #Assuming that it's a binary criterion
    trues = []
    falses = [] 
    for item in enumerable:
        if criterion(item):
            trues.append(item)
        else:
            falses.append(item)
    return trues,falses

class StreamWatcherListener(tweepy.StreamListener):

    status_wrapper = TextWrapper(width=120, initial_indent=TAB, subsequent_indent=TAB*2)

    def on_status(self, status):
        try:
            print self.status_wrapper.fill(status.text)
            print '%s  %s  via %s' % (status.author.screen_name, status.created_at, status.source)
            words = ''.join(c if c.isalnum() else ' ' for c in status.text).split()
            words
            print 'location: %s  -  Geo On? %s  -   coordinates: %s' % (status.user.location, status.user.geo_enabled, status.coordinates) 
            print '%s characters  -   %s words' % (len(status.text), len(words))
            print '\n'
            
            output = {"author": str(status.author.screen_name),"text":status.text.encode('ascii','ignore'),"geo":status.coordinates}
            print>>file_handle,output

        except:
            pass

    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        self.file_handle.write(self.CLOSE)
        return True  # keep stream alive

    def on_timeout(self):
        print 'Snoozing Zzzzzz'

def main():
    # Prompt for login credentials and setup stream object
    auth = tweepy.auth.OAuthHandler(directory['credentials']['consumer_key'], directory['credentials']['consumer_secret'])
    auth.set_access_token(directory['credentials']['access_token'], directory['credentials']['access_token_secret'])
    stream = tweepy.Stream(auth, StreamWatcherListener(), timeout=None)

    valid_modes = ['sample', 'filter']
    if opts.mode == 'sample':
        stream.sample()

    elif opts.mode == 'filter':
        if 'users' in globals():
            ids,handles = partition(users,string.isdigit)            
            ids += [tweepy.API().get_user(handle).id for handle in handles]
            if 'keywords' in globals():          
                stream.filter(users,keywords)
            else:
                stream.filter(users,None)
        else:
            stream.filter(None,keywords)
    else:
        raise ValueError('Selected mode was %s. Valid modes are %s'%(opts.mode,' '.join(mode for mode in valid_modes)))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print>>file_handle,CLOSE_FILE
        print NEWLINE*4
        print 'Output saved to %s'%output_file_name
