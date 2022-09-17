
from sqlalchemy.orm import Session
from db.models.Service import Service
from pydantic_schemas.services import ServiceCreate
 

def create_service(db: Session, service: ServiceCreate):
    db_category = Service(
                name=service.name,
                description=service.description,
                is_boosted=service.is_boosted,
                category_id=service.category_id,
                etablissement_id=service.etablissement_id
                )

    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


