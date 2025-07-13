from flask import Blueprint
from flask_restful import Api

api_v1 = Blueprint('api_v1', __name__)
api = Api(api_v1)


from app.api.v1.resources.dict import DwTypeListResource, DwTypeResource, DwListResource, DwResource, RcjEjflSxListResource, RcjEjflSxResource, RcjYjflListResource, RcjYjflResource, RcjEjflListResource, RcjEjflResource, RcjMC2EjflidListResource, RcjMC2EjflidResource, RcjMCClassifyListResource, RcjMCClassifyResource
api.add_resource(DwTypeListResource, '/dict/dw-types')
api.add_resource(DwTypeResource, '/dict/dw-types/<string:type_id>')
api.add_resource(DwListResource, '/dict/dws')
api.add_resource(DwResource, '/dict/dws/<string:dw_id>')
api.add_resource(RcjEjflSxListResource, '/dict/rcj-ejfl-sxs')
api.add_resource(RcjEjflSxResource, '/dict/rcj-ejfl-sxs/<string:sx_id>')
api.add_resource(RcjYjflListResource, '/dict/rcj-yjfls')   
