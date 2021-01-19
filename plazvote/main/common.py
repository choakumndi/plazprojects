from enum import Enum
from typing import Any, List, Tuple

def get_choices(constants_class: Any) -> List[Tuple[str, str]]:
    return constants_class.choices()
    
class EnumChoice(Enum):

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
        

class TransactionType(EnumChoice):

    IN = "IN",
    OUT = "OUT"


class TransactionStatus(EnumChoice):

    INITIATED = "INITIATED",
    PENDING = "PENDING",
    COMPLETED = "COMPLETED",
    FAILED = "FAILED"
    ERROR = "ERROR"

class AdType(EnumChoice):
    BANNER = "BANNER"
    BRAND = "BRAND"

class ContestType(EnumChoice):
    FREE = "FREE"
    PAID = "PAID"

class SocialMediaType(EnumChoice):
    FACEBOOK = "FACEBOOK"
    INSTAGRAM = "INSTAGRAM"
    YOUTUBE = "YOUTUBE"
    LINKEDIN = "LINKEDIN"
    PINTEREST = "PINTEREST"
    TWITTER = "TWITTER"
    WHATSAPP = "WHATSAPP"
    
CONTEST_TYPES = get_choices(ContestType)

SOCIAL_MEDIA_TYPES = get_choices(SocialMediaType)

AD_TYPES = get_choices(AdType)
