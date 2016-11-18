# -*- coding:utf-8 -*-
from baosteel100.handler import APIHandler
import baosteel100.libs.utils as utils
import baosteel100.model.user as user_model

class UserHandler(APIHandler):
    _model = "user.UserModel"
    def post(self):
        result = utils.init_response_data()
        user_model_obj = user_model.UserModel()
        try:
            mobile = self.get_argument("mobile","")
            password = self.get_argument("password","")
            sex = self.get_argument("sex","")
            name = self.get_argument("name","")
            nickname= self.get_argument("nickname","")
            add_time = self.get_argument("add_time",utils.get_current_time())
            edit_time = self.get_argument("edit_time",utils.get_current_time())
            enable_flag = self.get_argument("enable_flag","1")
            department = self.get_argument("department","")
            position = self.get_argument("position","")
            age = self.get_argument("age","")
            address = self.get_argument("address","")
            marital_status = self.get_argument("marital_status", "")
            email = self.get_argument("email","")
            id_card = self.get_argument("id_card","")
            user=user_model_obj.register(mobile,password,sex,name,nickname,add_time,enable_flag,department,position,age,address,marital_status,email,id_card,edit_time)
            result["data"]=utils.dump(user)
        except Exception as e:
            result = utils.reset_response_data(0,str(e))
        self.finish(result)

    def get(self):
        result = utils.init_response_data()
        user_model_obj = user_model.UserModel()
        try:
            mobile = self.get_argument("mobile","")
            user = user_model_obj.get_user(mobile)
            result["data"] = utils.dump(user)
        except Exception as e:
            result = utils.reset_response_data(0,str(e))
        self.finish(result)

    def put(self):
        result = utils.init_response_data()
        user_model_obj = user_model.UserModel()
        try:
            mobile = self.get_argument("mobile","")
            password = self.get_argument("password", "")
            sex = self.get_argument("sex", "")
            nickname = self.get_argument("nickname", "")
            edit_time = self.get_argument("edit_time", utils.get_current_time())
            department = self.get_argument("department", "")
            position = self.get_argument("position", "")
            age = self.get_argument("age", "")
            address = self.get_argument("address", "")
            marital_status = self.get_argument("marital_status", "")
            email = self.get_argument("email", "")
            user=user_model_obj.user_edit(mobile,password,sex,nickname,edit_time,department,position,age,address,marital_status,email)
            result["data"] = utils.dump(user)
        except Exception as e:
            result=utils.reset_response_data(0,str(e))
        self.finish(result)







handlers = [(r"/api/user",UserHandler)

            ]



