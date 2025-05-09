from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Category:
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = None
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now()
    )
