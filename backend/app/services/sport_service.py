from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.sport import Sport

def get_all_sports(db: Session):
    try:
        sports = db.query(Sport).all()
        sports_data = [sport.to_response_dict() for sport in sports]
        return sports_data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"There was an error in get_all_sports! {e}")
    
def get_sport_by_id(id: int, db: Session):
    try:
        sport = db.query(Sport).filter(Sport.id==id).one()
        return sport
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"There was an error in get_sport_by_id! {e}")