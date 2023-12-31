from fastapi import APIRouter
from Models import session
from CURD import curd_users
from Validators.user_validate import CreateUser, LoginUser
from sqlalchemy.exc import IntegrityError

router = APIRouter()


@router.get("/")
def get_users():
    try:
        return {"status": True}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.post("/")
def add_users(user_details: CreateUser):
    try:
        return {
            "status": True,
            "message": curd_users.add_user(db=session, user_details=user_details),
        }
    except IntegrityError as e:
        return {"status": False, "message": "Username already Exist"}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.post("/login")
def login_user(user_details: LoginUser):
    try:
        return {
            "status": True,
            "access-token": curd_users.login_user(
                db=session, user_details=user_details
            ),
        }
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.get("/{user_id}")
def get_users_by_id():
    try:
        return {"status": True}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.put("/{user_id}")
def update_users():
    try:
        return {"status": True}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.delete("/{user_id}")
def delete_user_by_id():
    try:
        return {"status": True}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}
