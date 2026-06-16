from pydanctic import BaseModel
from typing import Optimal

from tensorflow.python.data.ops.optional_ops import Optional


class Item(BaseModel):
    id: Optimal[int] = None
    name: str
    description: Optional[str] = None