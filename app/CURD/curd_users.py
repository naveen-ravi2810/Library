from sqlalchemy.orm import Session
import Validators
from Models.Tables import UsersBase
import bcrypt
from authorization import auth_handler
from sqlalchemy.orm import defer


def add_user(db: Session, user_details: Validators.CreateUser):
    new_user = UsersBase()
    new_user.user_name = user_details.user_name
    hash_pw = bcrypt.hashpw(user_details.password.encode("utf-8"), bcrypt.gensalt())
    new_user.password = hash_pw.decode("utf-8")
    print(hash_pw)
    db.add(new_user)
    db.commit()
    print(new_user.password)
    return True


def login_user(db: Session, user_details: Validators.user_validate.LoginUser):
    user = (
        db.query(UsersBase)
        .filter(UsersBase.user_name == user_details.user_name)
        .first()
    )
    if user and bcrypt.checkpw(
        user_details.user_password.encode("utf-8"), user.password.encode("utf-8")
    ):
        return auth_handler.signJWT(user=user)
    raise Exception("Invalid User Credentials")


def list_users(db: Session):
    return db.query(UsersBase).options(defer(UsersBase.password)).all()


def get_user_by_id(db: Session, user_id: int):
    user_details = (
        db.query(
            UsersBase.user_name,
            UsersBase.user_role,
            UsersBase.user_id,
            UsersBase.user_nick_name,
        )
        .filter(UsersBase.user_id == user_id)
        .first()
    )
    user_details_dict = {
        "user_name": user_details.user_name,
        "user_role": user_details.user_role,
        "user_nick_name": user_details.user_nick_name,
        "user_id": user_details.user_id,
    }
    return user_details_dict
