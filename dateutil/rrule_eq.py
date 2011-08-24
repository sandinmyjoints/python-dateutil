#!/usr/bin/env python
# encoding: utf-8
"""
rrule_eq.py

Created by William Bert on 2011-08-22.
Copyright (c) 2011 William Bert. All rights reserved.
"""
__license__ = "PSF License"

import unittest

from datetime import datetime, time

from rrule import rrule as rr
from rrule import YEARLY, MONTHLY, DAILY, HOURLY, MINUTELY, SECONDLY 
from rrule import MO, TU, WE, TH, FR, SA, SU
from rrule import weekday


class rrule_eq(rr): 
    """Wrapper class around rrule that provides __eq__ and __ne__ methods."""
        
    def __eq__(self, other):
        """Compare two rrule instances."""
        
        attrs = [
         '_byeaster',
         '_byhour',
         '_byminute',
         '_bymonth',
         '_bymonthday',
         '_bynmonthday',
         '_bynweekday',
         '_bysecond',
         '_bysetpos',
         '_byweekday',
         '_byweekno',
         '_byyearday',
         '_count',
         '_dtstart',
         '_freq',
         '_interval',
         '_timeset',
         '_tzinfo',
         '_until',
         '_wkst',
        ]
         
        for p in attrs:
            if getattr(self, p) != getattr(other, p):
                return False
            
        return True
        
    def __ne__(self, other):
        return not (self == other)
        

class rrule_eqTests(unittest.TestCase):
    def setUp(self):
        # rrule imports some modules (easter, parser) from dateutil. Need to add the 
        # parent directory to the Python path so rrule can find dateutil.
        import sys, os
        ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
        sys.path.insert(0, os.path.abspath(os.path.join(ROOT_PATH, "..")))

    def test_equals(self):
        r1 = rrule_eq(SECONDLY, dtstart=datetime(2012, 8, 15))
        r2 = rrule_eq(SECONDLY, dtstart=datetime(2012, 8, 15))
        self.assertTrue(r1==r2)

        r1 = rrule_eq(MINUTELY, dtstart=datetime(2012, 8, 15), bysecond=4)
        r2 = rrule_eq(MINUTELY, dtstart=datetime(2012, 8, 15), bysecond=4)
        self.assertTrue(r1==r2)

        r1 = rrule_eq(HOURLY, dtstart=datetime(2012, 8, 15), byminute=27)
        r2 = rrule_eq(HOURLY, dtstart=datetime(2012, 8, 15), byminute=27)
        self.assertTrue(r1==r2)

        r1 = rrule_eq(DAILY, dtstart=datetime(2012, 8, 15), byhour=22)
        r2 = rrule_eq(DAILY, dtstart=datetime(2012, 8, 15), byhour=22)
        self.assertTrue(r1==r2)
        
        r1 = rrule_eq(DAILY, dtstart=datetime(2012, 8, 15), byyearday=78)
        r2 = rrule_eq(DAILY, dtstart=datetime(2012, 8, 15), byyearday=78)
        self.assertTrue(r1==r2)

        r1 = rrule_eq(MONTHLY, dtstart=datetime(2012, 8, 15), bymonthday=-1)
        r2 = rrule_eq(MONTHLY, dtstart=datetime(2012, 8, 15), bymonthday=-1)
        self.assertTrue(r1==r2)

        r1 = rrule_eq(MONTHLY, dtstart=datetime(2012, 8, 15), byweekday=MO(+2))
        r2 = rrule_eq(MONTHLY, dtstart=datetime(2012, 8, 15), byweekday=MO(+2))
        self.assertTrue(r1==r2)

        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byweekday=(MO, WE, TH), bysetpos=-1)
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byweekday=(MO, WE, TH), bysetpos=-1)
        self.assertTrue(r1==r2)

        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), wkst=SU, byweekday=(MO, WE, TH), bysetpos=-1)
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), wkst=SU, byweekday=(MO, WE, TH), bysetpos=-1)
        self.assertTrue(r1==r2)
        
        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12))
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12))
        self.assertTrue(r1==r2)

        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), count=13)
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), count=13)
        self.assertTrue(r1==r2)
                
        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), interval=6)
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), interval=6)
        self.assertTrue(r1==r2)        

        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), until=datetime(2013, 8, 15))
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), until=datetime(2013, 8, 15))
        self.assertTrue(r1==r2)        

    def test_not_equals(self):
        r1 = rrule_eq(SECONDLY, dtstart=datetime(2012, 8, 15))
        r2 = rrule_eq(MINUTELY, dtstart=datetime(2012, 8, 15))
        self.assertFalse(r1==r2)

        r1 = rrule_eq(MINUTELY, dtstart=datetime(2012, 8, 15), bysecond=3)
        r2 = rrule_eq(MINUTELY, dtstart=datetime(2012, 8, 15), bysecond=4)
        self.assertFalse(r1==r2)

        r1 = rrule_eq(HOURLY, dtstart=datetime(2012, 8, 15), byminute=27)
        r2 = rrule_eq(DAILY, dtstart=datetime(2012, 8, 15), byminute=27)
        self.assertFalse(r1==r2)

        r1 = rrule_eq(DAILY, dtstart=datetime(2012, 8, 15), byhour=22)
        r2 = rrule_eq(DAILY, dtstart=datetime(2012, 8, 16), byhour=22)
        self.assertFalse(r1==r2)
        
        r1 = rrule_eq(DAILY, dtstart=datetime(2012, 8, 15), byyearday=78, byweekday=TU)
        r2 = rrule_eq(DAILY, dtstart=datetime(2012, 8, 15), byyearday=78)
        self.assertFalse(r1==r2)

        r1 = rrule_eq(MONTHLY, dtstart=datetime(2012, 8, 15), bymonthday=-1)
        r2 = rrule_eq(MONTHLY, dtstart=datetime(2012, 8, 15), bymonthday=-2)
        self.assertFalse(r1==r2)

        r1 = rrule_eq(MONTHLY, dtstart=datetime(2012, 8, 15), byweekday=MO(+2))
        r2 = rrule_eq(MONTHLY, dtstart=datetime(2012, 8, 15), byweekday=WE(+2))
        self.assertFalse(r1==r2)

        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byweekday=(MO, WE, TH), bysetpos=-1)
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byweekday=(MO, WE, TH), bysetpos=1)
        self.assertFalse(r1==r2)

        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), wkst=SU, byweekday=(MO, WE, TH), bysetpos=-1)
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), wkst=FR, byweekday=(MO, WE, TH), bysetpos=-1)
        self.assertFalse(r1==r2)
        
        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12))
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), interval=3)
        self.assertFalse(r1==r2)

        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), count=13)
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), count=12)
        self.assertFalse(r1==r2)
                
        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), interval=5)
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), interval=6)
        self.assertFalse(r1==r2)        

        r1 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), until=datetime(2013, 8, 15))
        r2 = rrule_eq(YEARLY, dtstart=datetime(2012, 8, 15), byeaster=(2, 10, 12), until=datetime(2013, 9, 15))
        self.assertFalse(r1==r2)
        
if __name__ == '__main__':
	unittest.main()