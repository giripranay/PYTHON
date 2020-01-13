# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
from gluon.tools import Mail
mail = Mail()
mail = auth.settings.mailer
mail.settings.server = 'smtp.gmail.com:465'
mail.settings.sender = 'waterportalsricity@gmail.com'
mail.settings.login = 'waterportalsricity@gmail.com:swaggers@123'

def Servicetype1():
    return locals()

def MineralDaily():
    session.mineral=1
    redirect(URL('Daily'))
    return locals()
def logout():
    if session.mineral:
        del session.mineral
    if session.y:
        del session.y
        if session.Type:
            del session.Type
            del session.H_no
            del session.Street
            del session.Town
            del session.District
            del session.Pin
        if session.cost:
            del session.cost
    redirect(URL('index'))
    return locals()
def confirm():
    return locals()

def Instance():
    form=SQLFORM(db.Inst).process()
    if form.accepted:
        x = mail.send(to=[session.y.email],
            subject='Water Portal Sricity', message="Your registration is successfully. We will process it very soon.")
    return locals()

def Daily():
    session.Type="Daily"
    session.k=1
    session.H_no=request.vars.H_no
    session.Street=request.vars.street
    session.Town=request.vars.town
    session.District=request.vars.district
    session.Pin=request.vars.pincode
    if session.mineral and session.H_no:
             session.cans=request.vars.cans
             session.cost=int(session.cans)*25
    if session.H_no and session.Street and session.Town and session.District:
        redirect(URL('confirm'))
        x = mail.send(to=[session.y.email],
            subject='Water Portal Sricity', message="Your registration is successfully. We will process it very soon.")
        session.flash='Than Q'
    else:
         session.flash='Enter correct details '
    return locals()
def edit():
    if session.k==1:
        session.k=session.k+1
        pass
    else:
        session.Type="Daily"
        session.H_no=request.vars.H_no
        session.Street=request.vars.street
        session.Town=request.vars.town
        session.District=request.vars.district
        session.Pin=request.vars.pincode
        if session.cans:
            session.cans=request.vars.cans
        redirect(URL('payment'))
    return locals()

def payment():
    return locals()

def register():
    Name=request.vars.name
    Email=request.vars.email
    Phone=request.vars.phone
    passwd=request.vars.passwd
    if Name:
        x = mail.send(to=[Email],
            subject='Water Portal Sricity', message="Your registration is successfully. We will process it very soon."
        )

        if x == True:
            response.flash = 'You are Successfully Registered'
            db.visit.insert(name=Name,email=Email,password=passwd,phone=Phone)
        else:
            response.flash = 'Sorry,enter your details correctly...'
    return locals()

def Servicetype():
    return locals()

def small():
    session.cost=5000
    session.size="Small"
    redirect(URL('Daily'))
    return locals()

def medium():
    session.cost=10000
    session.size="Medium"
    redirect(URL('Daily'))
    return locals()

def large():
    session.cost=15000
    session.size="Large"
    redirect(URL('Daily'))
    return locals()

def mineral():
    return locals()

def login():
    email=request.vars.email
    password=request.vars.passwd
    flag=0
    if email:
        names=db().select(db.visit.ALL,orderby=db.visit.name)
        for y in names:
            if y.email==email and y.password==password:
                flag=1
                break
        if flag==1:
            session.y=y
            redirect(URL('USER'))
        else:
            response.flash="INVALID CREDENTIALS"
    return locals()
def USER():
    import datetime
    d = datetime.datetime.now()
    k=getattr(d, 'hour')
    if k<12:
        greeting="Good Morning "+session.y.name
    elif k>=12 and k<16:
        greeting="Good Afternoon "+session.y.name
    elif k>=16 and k<20:
        greeting="Good Evening "+session.y.name
    else:
        greeting="poyi paduko ra puka"
    return locals()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Water Supply Portal")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
