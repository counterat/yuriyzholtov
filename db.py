from mongoengine import Document, FileField, ListField, StringField, connect, DateTimeField, IntField, SequenceField, ReferenceField


class Post_blog(Document):
    id = SequenceField(primary_key=True)
    title = StringField()
    content = StringField()
    images = ListField(StringField())
    created_at  = DateTimeField()
    category = StringField()


class Works_blog(Document):
    id = SequenceField(primary_key=True)
    title = StringField()
    content = StringField()
    images = ListField(StringField())
    created_at  = IntField()
    category = StringField()