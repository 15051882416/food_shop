from app.libs.error import APIException


class Success(APIException):
    code = 201
    error_code = 1
    msg = '添加或修改成功'


class DeleteSuccess(Success):
    code = 202
    error_code = -1
    msg = '删除成功'


class ClientTypeException(APIException):
    code = 400
    error_code = 1006
    msg = '客户端类型无效'


class ParameterException(APIException):
    code = 400
    error_code = 1000
    msg = '参数校验失败'


class ServerException(APIException):
    code = 500
    error_code = 999
    msg = '对不起，服务器错误'


class NotFound(APIException):
    code = 404
    error_code = 1001
    msg = '资源未找到'


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = '用户名或密码不对'


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = '禁止访问，权限不够'


class OrderException(APIException):
    code = 404
    error_code = 8000
    msg = '订单不存在，请检查ID'


class OrderStatusException(APIException):
    code = 404
    error_code = 8001
    msg = '订单状态不符合规范'


class UnderStock(APIException):
    code = 400
    error_code = 8002
    msg = '对不起，库存不足'


class ScoreException(APIException):
    code = 400
    error_code = 3001
    msg = '评分不符合规范'


class CartException(APIException):
    code = 400
    error_code = 4001
    msg = '购物车内商品数量不能小于0'


class WeChatException(APIException):
    code = 500
    error_code = 5001
    msg = '微信服务器异常'
