from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField
from datetime import date
"""

Define you MongoEngine Models here

"""

class Contact(Document):
    name = StringField(max_length=60, required=True, unique=True)
    address = StringField(max_length=60)
    birthday = DateTimeField()
    personal_phone = StringField(max_length=20)
    personal_celphone = StringField(max_length=20)
    # contact_group = ReferenceField(ContactGroup, required=True)
    # gender = ReferenceField(Gender, required=True)
    # tags = ListField(ReferenceField(Tags))

# client = Contact(name='sudhir', address='new address', 'birthday'= date(2020, 12, 1))
# client.save()