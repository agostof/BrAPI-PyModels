from .. core.models import (
        Metadata,
        BaseModel, Field, List, Optional, Context)
    
class ErrorResponseResult(BaseModel):
    data: List[str]  = Field(..., example=[''])
    
class ErrorResponse(BaseModel):
    _context: Optional[Context] = Field(None, alias='@context')
    metadata: Metadata
    result: ErrorResponseResult