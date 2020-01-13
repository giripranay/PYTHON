# -*- coding: utf-8 -*-

db.define_table('moisture',
                Field('recieved','datetime'),
                Field('x','integer'))



db.define_table('visit',
               Field('name','string',requires=IS_NOT_IN_DB(db,'visit.name')),
               Field('email','string',requires=IS_NOT_IN_DB(db,'visit.email')),
               Field('password','password',requires=IS_NOT_EMPTY()), 
               Field('phone','string',requires=IS_NOT_EMPTY()))
db.moisture.recieved.default=request.now
