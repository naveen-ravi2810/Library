from fastapi import APIRouter, Depends
from Models import session
from CURD import curd_users
from Validators.user_validate import CreateUser, LoginUser
from sqlalchemy.exc import IntegrityError
from authorization.auth_berear import admin_auth, common_auth

router = APIRouter()


@router.get("/")
def get_users(jwt_data: dict = Depends(admin_auth)):
    try:
        return {"status": True, "users": curd_users.list_users(db=session)}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.post("/")
def add_users(user_details: CreateUser, jwt_data: dict = Depends(admin_auth)):
    try:
        return {
            "status": True,
            "message": curd_users.add_user(db=session, user_details=user_details),
        }
    except IntegrityError:
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


@router.get("/me")
def get_users_by_id(jwt_data: dict = Depends(common_auth)):
    try:
        return {
            "status": True,
            "details": curd_users.get_user_by_id(user_id=jwt_data["sub"], db=session),
        }
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.put("/{user_id}")
def update_users(jwt_data: dict = Depends(admin_auth)):
    try:
        return {"status": True}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}


@router.delete("/{user_id}")
def delete_user_by_id(jwt_data: dict = Depends(admin_auth)):
    try:
        return {"status": True}
    except Exception as e:
        return {"status": False, "message": f"Error:{e}"}
