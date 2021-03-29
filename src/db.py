from typing import Dict
from secrets import token_hex


class DataBase:
    def __init__(self) -> None:
        self.db: Dict = {}

    def userInDB(self, email: str) -> Dict:
        for key, value in self.db.items():
            if value['email'] == email:
                return self.db[key]
        return None

    def saveUser(self, data: Dict) -> Dict:
        uid = self.generateRandomId()
        try:
            self.db[uid] = data
            self.db[uid]['id'] = uid
            return True
        except KeyError:
            return False

    def generateRandomId(self) -> str:
        return token_hex(16)

    def checkUserID(self, uid):
        try:
            user = self.db[uid]
            return user
        except KeyError:
            return None

    def saveRedFlag(self, uid: str, data: Dict) -> Dict:
        user = self.checkUserID(uid)
        if user is None:
            return None
        try:
            user['redflags']
        except KeyError:
            user['redflags'] = []

        data['rid'] = self.generateRandomId()
        user['redflags'].append(data)
        return data

    def getUserRedFlags(self, uid):
        user = self.checkUserID(uid)
        if user is None:
            return None
        try:
            return user['redflags']
        except KeyError:
            return None

    def getAllRedFlags(self):
        redflags = []
        for key in self.db:
            try:
                redflags.extend(self.db[key]['redflags'])
            except KeyError:
                pass
        return redflags

    def getRedFlag(self, uid, rid):
        user = self.checkUserID(uid)
        if user is None:
            return None
        try:
            for redflag in user['redflags']:
                if redflag['id'] == rid:
                    return redflag
            return None
        except KeyError:
            return None

    def getARedFlag(self, uid, rid):
        red_flag = self.getRedFlag(uid, rid)
        if red_flag:
            return red_flag
        return None

    def editRedFlag(self, uid, rid, data):
        red_flag = self.getRedFlag(uid, rid)
        if red_flag:
            red_flag = {**red_flag, **data}
            red_flag['id'] = rid
            return red_flag
        return None

    def deleteRedFlag(self, uid, rid):
        red_flag = self.getRedFlag(uid, rid)
        if red_flag:
            self.db[uid]['redflags'].remove(red_flag)
            return self.db[uid]['redflags']
        return None

    def saveIntervention(self, uid, data):
        user = self.checkUserID(uid)
        if user is None:
            return None
        try:
            user['interventions']
        except KeyError:
            user['interventions'] = []

        data['iid'] = self.generateRandomId()
        user['interventions'].append(data)
        return data

    def getAllInterventions(self):
        interventions = []
        for key in self.db:
            try:
                interventions.extend(self.db[key]['interventions'])
            except KeyError:
                pass
        return interventions

    def getUserInterventions(self, uid):
        user = self.checkUserID(uid)
        if user is None:
            return None
        try:
            return user['interventions']
        except KeyError:
            return None

    def getIntervention(self, uid, rid):
        user = self.checkUserID(uid)
        if user is None:
            return None
        try:
            for interventions in user['interventionss']:
                if interventions['id'] == rid:
                    return interventions
            return None
        except KeyError:
            return None

    def getAnIntervention(self, uid, rid):
        intervention = self.getIntervention(uid, rid)
        if intervention:
            return intervention
        return None

    def editIntervention(self, uid, rid, data):
        intervention = self.getIntervention(uid, rid)
        if intervention:
            intervention = {**intervention, **data}
            intervention['id'] = rid
            return intervention
        return None

    def deleteRedFlag(self, uid, rid):
        intervention = self.getIntervention(uid, rid)
        if intervention:
            self.db[uid]['interventions'].remove(intervention)
            return self.db[uid]['interventions']
        return None
