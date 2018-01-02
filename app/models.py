from app import db

class Sti_gtshmed(db.Model):
    caseNo = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    gender = db.Column(db.Integer)
    birth = db.Column(db.DateTime)
    idType = db.Column(db.Integer)
    idNo = db.Column(db.String())
    checkStatus = db.Column(db.Integer)
    contactWay = db.Column(db.String())
    createdAt = db.Column(db.DateTime)
    createName=db.Column(db.String())

    # height = db.Column(db.Integer)
    # weight = db.Column(db.Integer)
    # leftEyeDiopter = db.Column(db.Integer)
    # leftEyeSph = db.Column(db.Integer)
    # leftEyeCyl = db.Column(db.Integer)
    # leftEyeAxis = db.Column(db.Integer)
    # leftEyeIop = db.Column(db.Integer)
    # rightEyeDiopter = db.Column(db.Integer)
    # rightEyeSph = db.Column(db.Integer)
    # rightEyeCyl = db.Column(db.Integer)
    # rightEyeAxis = db.Column(db.Integer)
    # rightEyeIop = db.Column(db.Integer)
    # fileInfo=CharField()
    # type=IntegerField()
    # url=CharField()
    # cameraPosition=CharField()

    def __repr__(self):
        return '<Sti_gtshmed %s>' % self.idNo

    __str__ = __repr__


class Sti_gtshmed_device(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    device_name=db.Column(db.String())
    hospital_name=db.Column(db.String())
    provice=db.Column(db.String())
    city=db.Column(db.String())

    def __repr__(self):
        return '<Sti_gtshmed_device %s>'%self.device_name

    __str__=__repr__