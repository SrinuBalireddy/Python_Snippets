#!python3
# chapter.py

import ezgmail, os
#ezgmail.init()
#print(ezgmail.EMAIL_ADDRESS)
unreadThreads = ezgmail.unread()
#print(ezgmail.summary(unreadThreads))
#print(len(unreadThreads))
#print(str(unreadThreads[0]))
print(unreadThreads[0].messages[0].subject)
#print(unreadThreads[0].messages[0].body)
print(unreadThreads[0].messages[0].timestamp)
print(unreadThreads[0].messages[0].sender)
print(unreadThreads[0].messages[0].recipient)

recentThread = ezgmail.recent(maxResults=1)
print(len(recentThread))
print(recentThread[0].messages[0].subject)

