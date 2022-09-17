import imp
from unittest import result
from sqlalchemy.orm import Session

from db.models.Etablissement import Etablissement
from pydantic_schemas.etablissements import EtablissementCreate
 

def create_etablissement(db: Session, etablissement: EtablissementCreate):
    db_etablissement = Etablissement(
                name=etablissement.name,
                description=etablissement.description,
                address=etablissement.address,
                city=etablissement.city, 
                zipcode=etablissement.zipcode, 
                lat=etablissement.lat,
                lng= etablissement.lng,
                phone= etablissement.phone,
                logo= etablissement.logo,
                banner= etablissement.banner,
                schedules= etablissement.schedules,
                user_id=etablissement.user_id
                )

    print(db_etablissement)
    db.add(db_etablissement)
    db.commit()
    db.refresh(db_etablissement)
    return db_etablissement


''' def get_user_courses(db: Session, user_id: int):
    course = db.query(Course).filter(Course.user_id == user_id).all()
    return course
 '''