from ninja import Schema
from datetime import datetime
from pydantic import EmailStr

class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: EmailStr


class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    timestamp: datetime

class WaitlistEntryDetailSchema(Schema):
    # Get -> Data
    # WaitlistEntryOut
    email: EmailStr
    timestamp: datetime