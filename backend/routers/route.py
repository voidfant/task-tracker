
from models.user import User
from routers.oauth import get_current_active_user

from fastapi import Depends, APIRouter

router = APIRouter()


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "ownr": current_user.username}]


