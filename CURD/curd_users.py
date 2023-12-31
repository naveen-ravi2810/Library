from sqlalchemy.orm import Session
import Validators
from Models.Tables import UsersBase
import bcrypt


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
        return auth_handler.generate_token(user=user, exp=3600)
    raise Exception("Invalid User Credentials")
