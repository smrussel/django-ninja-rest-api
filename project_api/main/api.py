from ninja import NinjaAPI, Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController
import helpers

api = NinjaExtraAPI(auth=helpers.api_auth_user_or_annon)
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlists/","waitlists.api.router")

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    # is not request.user.is_authenticated
    email: str = None

@api.get("/hello")
def hello(request):
    print(request)
    return "Hello world"


@api.get("/me",response=UserSchema, auth=helpers.api_auth_user_required)
def me(request):
    return request.user