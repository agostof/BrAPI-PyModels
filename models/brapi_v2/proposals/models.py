from .. core.models import (
        Metadata,
        BaseModel, Field, List, Optional, Context)
    
class ErrorResponseResult(BaseModel):
    data: List[str]  = Field(..., example=[''])
    
class ErrorResponse(BaseModel):
    _context: Optional[Context] = Field(None, alias='@context')
    metadata: Metadata
    result: ErrorResponseResult

from typing import Generic, TypeVar, List, Dict, Optional
from typing_extensions import Literal

import numpy as np
from pydantic.fields import ModelField
from pydantic import AnyUrl, BaseModel, Extra, Field

JSON_ENCODERS = {
    np.ndarray: lambda arr: arr.tolist()
}

DType = TypeVar('DType')


class TypedArray(np.ndarray, Generic[DType]):
    """Wrapper class for numpy arrays that stores and validates type information.
    This can be used in place of a numpy array, but when used in a pydantic BaseModel
    or with pydantic.validate_arguments, its dtype will be *coerced* at runtime to the
    declared type.
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, val, field: ModelField):
        dtype_field = field.sub_fields[0]
        actual_dtype = dtype_field.type_.__args__[0]
        # If numpy cannot create an array with the request dtype, an error will be raised
        # and correctly bubbled up.
        np_array = np.array(val, dtype=actual_dtype)
        return np_array
    
    
class Genotypes(BaseModel):
    genotypes: TypedArray[Literal['int8']]

    class Config:
        json_encoders = JSON_ENCODERS

        
class GenotypeMatrixResult(BaseModel):
    variantsAsRows: bool = Field(
        None, description='Determine variant matrix orientation', example=True
    )

    annotationsCallset: Optional[Dict[str, List[str]]] = Field(
        None, description='arbitrary annotations for each callset in array format', 
        example={'countryOfOrigin':['INDIA','JAPAN']}
    )

    annotationsVariants: Optional[Dict[str, List[str]]] = Field(
        None, description='arbitrary annotations for each variant in an array format', 
        example={'putativeFunction':['STOP','FRAMESHIFT']}
    )

    callsets: List[str] = Field(
        None, description='Callsets contained in the matrix', example=[[0, 1],[0, 2]]
    )

    genotypes: TypedArray[Literal['int8']] = Field(
        None, description='genotype data', example=[[0, 1],[0, 2]]
    )

    class Config:
        json_encoders = JSON_ENCODERS


