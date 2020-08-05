from flask_appbuilder.api import BaseApi, expose
from app import appbuilder


class ClientApi(BaseApi):
    @expose('/client', ['POST'])
    def client(self):
        return self.response(200, message="Hello")


appbuilder.add_api(ClientApi)
