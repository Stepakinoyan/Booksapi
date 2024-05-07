from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class VolumeInfo(BaseModel):
    title: str
    authors: Optional[List[str]] = None
    publishedDate: Optional[datetime] = None
    pageCount: Optional[int] = None
    categories: Optional[List[str]] = None
    language: str
    description: Optional[str] = None
    averageRating: Optional[float] = None


class Item(BaseModel):
    volumeInfo: VolumeInfo


class Books(BaseModel):
    items: List[Item]
