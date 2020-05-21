from __future__ import print_function
from mailmerge import MailMerge
import datetime
def create(audience, topic, event_date, time, venue) :
    template = "./application.docx"
    document = MailMerge(template)
    current_date=str(datetime.date.today())
    document.merge(Application=current_date,Audience=audience,Topic=topic,Date=event_date,Time=time,Venue=venue)
    file_name=str(datetime.datetime.now()).replace(":","_") + ".docx"
    document.write(file_name)
