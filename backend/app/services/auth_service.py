
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.models.user import User


password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    return password_context.hash(password)


def register_user(
    db: Session,
    full_name: str,
    email: str,
    password: str
):
    # Check whether the email is already registered
    existing_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_user:
        return None

    # Create user with hashed password
    new_user = User(
        full_name=full_name,
        email=email,
        hashed_password=hash_password(password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
