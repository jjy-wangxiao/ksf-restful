# DTO (Data Transfer Object) 包
# 用于定义数据传输对象，分离数据模型与API传输模型

# 导出矩阵相关的 DTO
from .matrix_dto import (
    FileListQueryDTO,
    FileListResponseDTO,
    PaginationMeta,
    PaginatedResponse,
    ErrorResponse,
    ErrorCode
)

# 导出字典相关的 DTO
from .dict import (
    DwTypeRequestDTO,
    DwTypeUpdateRequestDTO,
    DwTypeResponseDTO,
    DwTypeInternalDTO,
    DwRequestDTO,
    DwUpdateRequestDTO,
    DwResponseDTO,
    DwInternalDTO,
    RcjEjflSxRequestDTO,
    RcjEjflSxUpdateRequestDTO,
    RcjEjflSxResponseDTO,
    RcjEjflSxInternalDTO,
    RcjYjflRequestDTO,
    RcjYjflUpdateRequestDTO,
    RcjYjflResponseDTO,
    RcjYjflInternalDTO,
    RcjEjflRequestDTO,
    RcjEjflUpdateRequestDTO,
    RcjEjflResponseDTO,
    RcjEjflInternalDTO,
    RcjMC2EjflidRequestDTO,
    RcjMC2EjflidUpdateRequestDTO,
    RcjMC2EjflidResponseDTO,
    RcjMC2EjflidInternalDTO,
    RcjMCClassifyRequestDTO,
    RcjMCClassifyUpdateRequestDTO,
    RcjMCClassifyResponseDTO,
    RcjMCClassifyInternalDTO
)

# 导出通用 DTO
from .common import (
    PaginatedResponse as CommonPaginatedResponse,
    ApiResponse,
    ErrorResponse as CommonErrorResponse
) 