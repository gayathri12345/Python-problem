from models import Song,Podcast,Audiobook
from flask import jsonify
from project import api

Obj={'Song':Song,'Podcast':Podcast,'Audiobook':Audiobook}
##### Sample Data  #####
Metadata={'Name':'Another_New_Song',
        'Title':'NewTitle',
        'Author':'NewAuthor',
        'Narrator':'NewNarrator',
        'Duration':7,
        'Podcast':"NewPodcast",
        "Host":'NewHost',
        'Participants':['XYZ','ABC','123']
        }
#######  

class Songs(Resource):

    def get(audioFileType,audioFileID):
        
        res=Obj[audioFileType].query.filter_by(id=audioFileID).first()
        if res:
            return jsonify(res.json())
        else:
            return jsonify({"Song" : "None"}),404

    def post(audioFileType,audioFileID=0):
        if audioFileType=='Song':
            song=Song(Name_of_the_song=Metadata['Name'],Duration=Metadata['Duration'])
        if audioFileType=='Podcast':
            song=Podcast(Name_of_the_Podcast=Metadata['Podcast'],Duration=Metadata['Duration'],Host=Metadata['Host'])
        if audioFileType=='Audiobook':
            song=Audiobook(Title=Metadata['Title'],Duration=Metadata['Duration'],Author=Metadata['Author'],Narrator=Metadata['Narrator'])
        db.session.add(song)
        db.session.commit()
        return jsonify(song.json())
       
    def delete(audioFileType,audioFileID):
        
        res=Obj[audioFileType].query.filter_by(id=audioFileID).first()
        if res:
            db.session.delete(res)
            db.session.commit()
            return jsonify({'note':'deleted successfully'})
        else:
            return jsonify({"Note":"ID not found"}),404
        

    def put(audioFileType,audioFileID):
        
        song=Obj[audioFileType].query.filter_by(id=audioFileID).first()
        if song:
            if audioFileType=='Song':
                song.Name_of_the_song=Metadata['Name']

            if audioFileType=='Podcast':
                song.Name_of_the_Podcast=Metadata['Podcast']
                song.Host=Metadata['Host']
                if 'Participants' in Metadata.keys():
                    song.Participants=Metadata['Participants']

            if audioFileType=='Audiobook':
                song.Title=Metadata['Title']
                song.Author=Metadata['Author']
                song.Narrator=Metadata['Narrator']

            song.Duration=Metadata['Duration']
            db.session.commit()
            return jsonify(song.json())
        else:
            return jsonify({'note':'Id not found'}),404
        
   
class allsongs(Resource):

    def get(audioFileType):
        
        songs=Obj[audioFileType].query.all()
        return jsonify([song.json() for song in songs])
        
api.add_resource(Songs,'/<audioFileType>/<int:audioFileID>/')
api.add_resource(allsongs,'/<audioFileType>')
