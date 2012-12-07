from django.core.management.base import BaseCommand, CommandError
from elements.models import Element, Category
from django.contrib.auth.models import User
import sqlite3 as lite

def process(id, uri, name, descr, depiction, latitude, longitude):
    #print 'ID:', id
    #print 'URI:', uri
    #print 'Name:', name
    #print 'Description:', descr
    #print 'Depiction:', depiction
    #print 'Latitude:', latitude
    #print 'Longitude:', longitude
    #print '======================================'
    el = Element(owner=User.objects.get(id=1), name=name, description=descr, category=Category.objects.get(id=1),
                db_uri=uri, db_id=id, db_img=depiction, latitude=latitude, longitude=longitude)
    el.save()


class Command(BaseCommand):
    args = '<database path>'
    help = 'Imports monuments from Afnarel database'

    def handle(self, *args, **options):
        con = lite.connect(args[0])
        con.text_factory = str

        with con:
            cur = con.cursor()
            req = "SELECT * FROM monument"
            cur.execute(req)
            for row in cur.fetchall():
                process(row[0], row[1], row[2], row[3], row[6], row[7], row[8])

            