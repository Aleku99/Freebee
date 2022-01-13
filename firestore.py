import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

if __name__ == "__main__":
    cred = credentials.Certificate("resources/freebee-b4e15-firebase-adminsdk-hy6nd-b846df60f2.json")
    firebase_admin.initialize_app(cred)

    firestoreService = firestore.client()

    with open("out.json", "r", encoding='utf-8') as jsonFile:
        objs: dict = json.loads(jsonFile.read())
        cityArray = objs["cities"]
        for cityObj in cityArray:
            for city in cityObj:
                cityData = cityObj[city]
                docs = firestoreService.collection(u'countries/Romania/cities').where(u'name', '==',
                                                                                      cityData["name"]).stream()
                cityUid = next(docs).id
                firestoreService.collection(u'countries/Romania/cities').document(u'' + cityUid).update({
                        'restaurants': cityData['restaurants']
                })
