from fastapi import APIRouter, HTTPException, status
from models.users import NewUser, User, UserSignIn


user_router = APIRouter(
    tags=["User"]
)

users = {}

#route de l'endpoint pour l'inscription d'un nouvel utilisateur
@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Un utilisateur avec cet email existe"
        )
    users[data.email] = data
    return {
        "message": "Utilisateur enregitré avec succès"
    }


#route de l'endpoint pour la connexion d'un utilisateur
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="L'utilisateur n'existe pas"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="les données entrées sont incorrectes"
        )
    return {
        "message": "Utilisateur connecté avec succès"
    }
