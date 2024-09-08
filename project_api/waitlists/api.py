from typing import List
from ninja import Router
from .models import WaitlistEntry
from .schemas import WaitlistEntryListSchema,WaitlistEntryCreateSchema,WaitlistEntryDetailSchema
from django.shortcuts import get_object_or_404
from ninja_jwt.authentication import JWTAuth
import helpers
router = Router()



# /api/waitlists/
@router.get("", response=List[WaitlistEntryListSchema],auth=helpers.api_auth_user_required)
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.filter(user=request.user)
    return qs

# /api/waitlists/
@router.post("", response=WaitlistEntryDetailSchema,auth=helpers.api_auth_user_or_annon)
def create_waitlist_entry(request,data:WaitlistEntryCreateSchema):
    obj = WaitlistEntry(**data.dict())
    if request.user.is_authenticated:
        obj.user = request.user
        # obj.user_id = request.user.id
    obj.save()
    return obj

# /api/waitlists/1
@router.get("{entry_id}/", response=WaitlistEntryListSchema,auth=helpers.api_auth_user_required)
def get_waitlist_entry(request,entry_id:int):
    obj = get_object_or_404(WaitlistEntry,id=entry_id,user=request.user)
    return obj