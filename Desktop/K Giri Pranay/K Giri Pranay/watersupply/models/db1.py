# -*- coding: utf-8 -*-
db.define_table('visit',
               Field('name','string',requires=IS_NOT_IN_DB(db,'visit.name')),
               Field('email','string',requires=IS_NOT_IN_DB(db,'visit.email')),
               Field('password','password',requires=IS_NOT_EMPTY()),
               Field('phone','integer',requires=IS_NOT_EMPTY()))
# -*- coding: utf-8 -*-
db.define_table('Dist',Field('DistName'),format='%(DistName)s')

db.define_table('Daily',
               Field('H_no','string',requires=IS_NOT_IN_DB(db,'visit.name')),
               Field('Street','string',requires=IS_NOT_IN_DB(db,'visit.email')),
               Field('Town','string',requires=IS_NOT_EMPTY()),
               Field('District',db.Dist))


db.define_table('Inst',
               Field('H_no','string',requires=IS_NOT_IN_DB(db,'visit.name')),
               Field('Street','string',requires=IS_NOT_IN_DB(db,'visit.email')),
               Field('Town','string',requires=IS_NOT_EMPTY()),
               Field('District',db.Dist))
