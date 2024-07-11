import copy

from enum import Enum
from intbase import InterpreterBase


# Enumerated type for our different language data types
class Type(Enum):
    INT = 1
    BOOL = 2
    STRING = 3
    CLOSURE = 4
    NIL = 5
    OBJECT = 6

class Object:
    def __init__(self):
        self.values = {}
        self.type = Type.OBJECT
        self.proto = None

    def get_values(self):
        return self.values
    
    def set(self, field, symbol):
        self.values[field] = symbol

    def set_proto(self, new_proto):
        self.proto = new_proto

class Closure:
    def __init__(self, func_ast, env):
        self.captured_env = {}
        for var_name, value in env:
            if value.type() in [Type.INT, Type.BOOL, Type.STRING, Type.NIL]:
                self.captured_env[var_name] = copy.deepcopy(value)
            else:
                self.captured_env[var_name] = value
        self.func_ast = func_ast
        self.type = Type.CLOSURE


# Represents a value, which has a type and its value
class Value:
    def __init__(self, t, v=None):
        self.t = t
        self.v = v

    def value(self):
        return self.v

    def type(self):
        return self.t

    def set(self, other):
        self.t = other.t
        self.v = other.v


def create_value(val):
    if val == InterpreterBase.TRUE_DEF:
        return Value(Type.BOOL, True)
    elif val == InterpreterBase.FALSE_DEF:
        return Value(Type.BOOL, False)
    elif isinstance(val, str):
        return Value(Type.STRING, val)
    elif isinstance(val, int):
        return Value(Type.INT, val)
    elif val == InterpreterBase.NIL_DEF:
        return Value(Type.NIL, None)
    elif isinstance(val, Object):
        return Value(Type.OBJECT, val)
    else:
        raise ValueError("Unknown value type")


def get_printable(val):
    if val.type() == Type.INT:
        return str(val.value())
    if val.type() == Type.STRING:
        return val.value()
    if val.type() == Type.BOOL:
        if val.value() is True:
            return "true"
        return "false"
    return None
