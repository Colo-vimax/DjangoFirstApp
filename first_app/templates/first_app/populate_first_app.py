import os

# CONFIGURE SETTING

os.environ.setdefault('DJANGO_SETTING_MODULE','first_project.settings')


import django
django.setup()

# FAKEUP SCRIPT
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()

topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # GET TOPIC ENTRY
        top = add_topic()
        # CREATE FAKE DATA ENTRY
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # CREATE FAKE NEW WEBPAGE ENTRY
        Webpg= Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]


        # CREATE A FAKE ACCESS RECORD FOR WEBPAGE
        acc_rec = AccessRecord.objects.get_or_create(name=Webpg,date=fake_date)[0]


if __name__ =='__name__':
    print("populating script!")
    populate(20)
    print("populating complete!")









