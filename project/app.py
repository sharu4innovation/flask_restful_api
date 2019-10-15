from flask import Blueprint
from flask_restful import Api
import resources.manage as manage


cloud = ""
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(manage.Manage_Clusters, '/manageClusters')
api.add_resource(manage.Manage_Machines, '/manageMachines')





