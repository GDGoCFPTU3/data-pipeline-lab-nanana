import uuid
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp)."""
    # Khai báo các trường ở đây...

    document_id: str
    source_type: Literal['PDF', 'Video']
    author: str
    category: str
    content: str
    timestamp: str
