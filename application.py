from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
def create(A,To,D,T,V) :
    template = "./application.docx"
    document = MailMerge(template)
    w=str(date.today())
    document.merge(Application=w,Audience=A,Topic=To,Date=D,Time=T,Venue=V)
    #document.merge(Application='3rd Feb 2020',Audience='1st year undergraduate student of IT Department',Topic='Python',Date='5th Feb 2020',Time='5 pm',Venue='ATC 203,204')
    document.write('a1-output.docx')
