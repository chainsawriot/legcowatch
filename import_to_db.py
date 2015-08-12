# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from xml_parse import parse_meeting
from bs4 import BeautifulSoup
import re


con = None

try:
    con = lite.connect('legcowatch.db')
    con.row_factory = lite.Row
    cur = con.cursor()    
    #cur.execute('SELECT SQLITE_VERSION()')
    #data = cur.fetchone()
    #print "SQLite version: %s" % data                
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)


vote = open("cm_vote_20150624.xml", "r").read()
vote_bs = BeautifulSoup(vote, "html.parser")
meeting_data = parse_meeting(vote_bs.find('meeting'))


def query_insert_inv(inv, cur, con):
    data = cur.execute("select * from individuals where name_en = ? and name_ch = ?", (inv['name_en'], inv['name_ch'])).fetchone()
    if data is None:
        # not such data
        #print "No entries, inserting"
        cur.execute("insert into individuals (name_en, name_ch) values (?, ?)", (inv['name_en'], inv['name_ch']))
        con.commit()
        data = cur.execute("select * from individuals where name_en = ? and name_ch = ?", (inv['name_en'], inv['name_ch'])).fetchone()
    return data['inv_id']



print query_insert_inv(meeting_data['vote'][0]['individual_votes'][10], cur, con)

vote_d = meeting_data['vote'][0]
from datetime import datetime
datetime.strptime(vote_d['vote_date'] + " " + vote_d['vote_time'], '%d/%m/%Y %H:%M:%S')

cur.execute("insert into motions (vote_separate_mech, motion_en) values (?, ?)", (1, 'hello_world'))


def insert_vote(vote_d):
    mover_id = query_insert_inv({'name_en': vote_d['mover_en'], 'name_ch': vote_d['mover_ch']}, cur, con)
    if vote_d['vote_separate_mechanism'] == "Yes":
        vote_separate_mech = 1
    else:
        vote_separate_mech = 0
    
