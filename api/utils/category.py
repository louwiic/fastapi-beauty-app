
from sqlalchemy.orm import Session
from db.models.Category import Category
from pydantic_schemas.category import CategoryCreate
 

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(
                name=category.name,
                description=category.description,
                avatar=category.avatar,
                sku=category.sku
                )

    print(db_category)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


