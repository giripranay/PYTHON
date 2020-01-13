# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
def sample():
    return locals()
def Automatic():
    from twilio.rest import TwilioRestClient
    client = TwilioRestClient("ACce752e8025ff27fe23b43e0f640958a9", "33525a7f25a8ba448ab24b323041e246")
    client.messages.create(to="+919133657988", from_="+19382232685",
                       body="/")
    session.A=1
    redirect(URL('Mode'))
    return locals()
def map():
    return locals()
def sms():
    session.A=0
    return locals()
def sms2():
    part1="*"
    part2="*"
    part3="*"
    for i in range(10):
        if i<4:
            part1=part1+session.phone[i]
        elif i>=4 and i<8:
            part2=part2+session.phone[i]
        else:
            part3=part3+session.phone[i]
    from twilio.rest import TwilioRestClient
    client = TwilioRestClient("ACce752e8025ff27fe23b43e0f640958a9", "33525a7f25a8ba448ab24b323041e246")
    client.messages.create(to="+919133657988", from_="+19382232685",
                       body=part1)
    from twilio.rest import TwilioRestClient
    client = TwilioRestClient("ACce752e8025ff27fe23b43e0f640958a9", "33525a7f25a8ba448ab24b323041e246")
    client.messages.create(to="+919133657988", from_="+19382232685",
                       body=part2)
    from twilio.rest import TwilioRestClient
    client = TwilioRestClient("ACce752e8025ff27fe23b43e0f640958a9", "33525a7f25a8ba448ab24b323041e246")
    client.messages.create(to="+919133657988", from_="+19382232685",
                       body=part3)
    
    redirect(URL('sms'))
def sms1():
    return locals()
def moisture():
    import serial
    x=serial.Serial('/dev/ttyACM0','9600')
    t=0;
    while(t<=4):
        if(x.inWaiting()>0):
            y=x.readline()
            t +=1
            if t==3:
                break
    z=int(y)
    if z<950:
        db.moisture.insert(x=z)
        z=str(z)
        session.flash="Moisture value : "+z
    else :
        redirect(URL('moisture'))
        session.flash="Something went wrong in getting the moisture value"
    redirect(URL('sms'))
    return locals()
def Mode():
    return locals()
def sendon():
    from twilio.rest import TwilioRestClient
    client = TwilioRestClient("ACce752e8025ff27fe23b43e0f640958a9", "33525a7f25a8ba448ab24b323041e246")
    client.messages.create(to="+919581552263", from_="+19382232685",
                       body="#X")
    session.state=1
    redirect(URL('sms'))
    return locals()
def sendoff():
    from twilio.rest import TwilioRestClient
    client = TwilioRestClient("ACce752e8025ff27fe23b43e0f640958a9", "33525a7f25a8ba448ab24b323041e246")
    client.messages.create(to="+919133657988", from_="+19382232685",
                       body="#Y")
    session.state=0
    redirect(URL('sms'))
    return locals()

def index():
    times=db().select(db.moisture.ALL,orderby=db.moisture.recieved)
    flag=0
    return locals()

def register():
    form=SQLFORM(db.visit).process()
    if form.accepted:redirect('login')
    return locals()

def login():
    if session.phone:
        del session.phone
    return locals()

def login1():
    name=request.vars.name
    email=request.vars.email
    password=request.vars.passwd
    flag=0
    hii=5
    names=db().select(db.visit.ALL,orderby=db.visit.name)
    for y in names:
        if y.name==name:
            flag=1
            break
    if flag==1:
        y=db(db.visit.name==name).select(db.visit.email).first().email
        y1=db(db.visit.name==name).select(db.visit.password).first().password
        y3=db(db.visit.name==name).select(db.visit.phone).first()
        if y==email and y1==password:
            times=db().select(db.moisture.ALL,orderby=db.moisture.recieved)
            flag=0
            list1=[]
            list2=[]
            session.phone=str(y3.phone)
            for t in times:
                list1.insert(0,str(t.recieved))
                list2.insert(0,int(t.x))
            pass
            session.m=str(list2[0])
            for t in times:
                if flag==0:
                    last=list1[0];
                    mois=list2[0];
                    flag=1
                    return locals()
            pass
            return locals()   
        else:
            redirect(URL('wrong'))
    else:
        redirect(URL('wrong'))
    return locals()

def wrong():
    return "fill your details currectly"
