from project import db
from datetime import datetime

class Song(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    Name_of_the_song=db.Column(db.String(100))
    Duration=db.Column(db.Integer)
    Uploaded_time=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __init__(self,Name_of_the_song,Duration):
        self.Name_of_the_song=Name_of_the_song
        self.Duration=Duration

    def json(self):
        return {'Name of the Song':self.Name_of_the_song, 'Duration':self.Duration, 'Uploaded at':self.Uploaded_time}

class Podcast(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Name_of_the_Podcast=db.Column(db.String(100),nullable=False)
    Duration=db.Column(db.Integer,nullable=False)
    Uploaded_time=db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    Host=db.Column(db.String(100),nullable=False)
    Participants=db.relationship("People",backref='participants',lazy=True)

    def __init__(self,Name_of_the_Podcast,Duration,Host,Participants=[]):
        self.Name_of_the_Podcast=Name_of_the_Podcast
        self.Duration=Duration
        self.Host=Host
        self.Participants=Participants

    def json(self):
        return {"Name of Podcast":self.Name_of_the_Podcast,'duration':self.Duration,'Uploaded at':self.Uploaded_time,'Host':self.Host,'Participants':self.Participants}


class People(db.Model):
    people=db.relationship(Podcast)
    id=db.Column(db.Integer,primary_key=True)
    pod_id=db.Column(db.Integer,db.ForeignKey('podcast.id'),nullable=False)
    name=db.Column(db.String(100),nullable=True)
   

class Audiobook(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(100),nullable=False)
    Author=db.Column(db.String(100),nullable=False)
    Narrator=db.Column(db.String(100),nullable=False)
    Duration=db.Column(db.Integer,nullable=False)
    Uploaded_time=db.Column(db.DateTime,nullable=False, default=datetime.utcnow)

    def __init__(self,Title,Author,Narrator,Duration):
        self.Title=Title
        self.Author=Author
        self.Narrator=Narrator
        self.Duration=Duration
        

    def json(self):
        return {"title":self.Title,"Author":self.Author,"Narrator":self.Narrator,"Duration":self.Duration,"Uploaded_time":self.Uploaded_time}
