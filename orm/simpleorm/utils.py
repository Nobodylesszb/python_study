#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: utils.py 
@version:
@time: 2019/12/14
@function： 基本的类型
"""
import numbers


class Field:
    pass


class IntField(Field):
    """
    IntField数据描述符, 内部自定义检查条件
    """

    def __init__(self, db_column, max_value=None):
        self._value = None
        self.db_column = db_column
        if max_value < 0:
            raise ValueError('max_value must be a positive number')

        self.math_length = max_value

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")


class CharField(Field):
    """
    charfield数据描述符，自定义检查条件
    """

    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_column = db_column
        if max_length is None:
            raise ValueError("max length is needed")
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")

        self._value = value


class ModeMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)

        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        # 最后需要创建并返回一个对象,通过type(super())
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModeMetaClass):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))

        sql = "insert {db_table}({fields}) value({values})".format(db_table=self._meta["db_table"],
                                                                   fields=",".join(fields), values=",".join(values))
        pass


class User(BaseModel):
    """
    创建User类时，首先查找参数中是否存在Metaclass元类,如果存在Metaclass元类,那么由Metaclass元类创建User;
    如果User有继承父类(如：BaseModel),那么会从父类中查找Metaclass,如果存在Metaclass元类,先创建父类BaseModel,
    然后再创建User类;如果User类参数中既没有metaclass='',也没有继承父类(BaseModel)或者父类参数中没有元类(metaclass='')，
    那么User及其父类将由type(name, bases, attrs)创建。
    """
    # 类属性同时是CharField和IntFiled的实例，被传递给type(name, bases, attrs)中的attrs。
    name = CharField(db_column="name", max_length=10)
    age = IntField(db_column="age", max_value=100)

    # 类属性，被传递给type(name, bases, attrs)中的attrs。
    class Meta:
        db_table = "user"


if __name__ == "__main__":
    user = User(name="wahaha", age=18)
    print(user.name)
    # user.name = "wahaha"
    # user.age = 18
    user.save()
    pass
