# coding : UTF-8

class Meta(type):
    def __new__(mcs, name, bases, attrs):
        attrs['class_attribute'] = "MetaClassValue"
        return super().__new__(mcs, name, bases, attrs)

class MyClass(metaclass=Meta):
    instance_attribute = "InstanceValue"

obj = MyClass()
print(obj.class_attribute)