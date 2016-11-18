# -*- coding:utf-8 -*-
import baosteel100.model.model as model
import baosteel100.libs.utils as utils
from baosteel100 import status
from baosteel100.libs.utils import options

class UserModel(model.BaseModel,model.Singleton):
    __name = "dxb.user"

    def __init__(self):
        model.BaseModel.__init__(self,UserModel.__name)

    def register(self,mobile,password,sex,name,nickname,add_time,enable_flag,department,position,age,address,marital_status,email,id_card,edit_time):
        if mobile is None or password is None:
            raise ValueError(u"用户或者密码为空")
        user = self.coll.find_one({"mobile":mobile})
        if user is not None:
            raise ValueError(u"手机号已被注册！")
        if marital_status =="0":
            marital_status=status.MARITAL_STATUS_NO
        elif marital_status == "1":
            marital_status = status.MARITAL_STATUS_YES
        else:
            marital_status = status.MARITAL_STATUS_BREAK
        _user = {
            "mobile":mobile,
            "password":password,
            "sex":sex,
            "name":name,
            "nickname":nickname,
            "add_time":add_time,
            "edit_time":edit_time,
            "enable_flag":enable_flag,
            "department":department,
            "position":position,
            "age":age,
            "address":address,
            "marital_status":marital_status,
            "email":email,
            "id_card":id_card

        }
        self.coll.insert_one(_user)
        return utils.dump(_user)

    def get_user(self,mobile):
        if mobile ==None:
            raise ValueError(u"查询条件为空")
        user=self.coll.find_one({"mobile":mobile})
        if not user:
            raise ValueError(u"无符合条件的结果")
        return utils.dump(user)

    def user_edit(self,mobile,password,sex,nickname,edit_time,department,position,age,address,marital_status,email):
        user = self.coll.find_one({"mobile":mobile})
        if not user:
            raise ValueError(u"无此记录")
        if marital_status =="0":
            marital_status=status.MARITAL_STATUS_NO
        elif marital_status == "1":
            marital_status = status.MARITAL_STATUS_YES
        else:
            marital_status = status.MARITAL_STATUS_BREAK
        user["password"]=password
        user["sex"] = sex
        user["nickname"] = nickname
        user["edit_time"] = edit_time
        user["department"] = department
        user["age"]=age
        user["position"] = position
        user["address"] = address
        user["marital_status"] = marital_status
        user["email"] = email
        self.coll.save(user)
        return utils.dump(user)



