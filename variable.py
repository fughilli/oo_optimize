

class Expression(object):
    def __init__(self, op, l, r):
        self.l = l
        self.r = r
        self.op = op

    def __add__(self, other):
        return Expression('+', self, other)

    def __sub__(self, other):
        return Expression('-', self, other)

    def __mul__(self, other):
        return Expression('*', self, other)

    def __div__(self, other):
        return Expression('/', self, other)

    def __pow__(self, other):
        return Expression('**', self, other)

    def __eq__(self, other):
        registry.Bind(self, '=', other)

    def __gt__(self, other):
        registry.Bind(self, '>', other)

    def __lt__(self, other):
        registry.Bind(self, '<', other)

    def __ge__(self, other):
        registry.Bind(self, '>=', other)

    def __le__(self, other):
        registry.Bind(self, '<=', other)

    def __repr__(self):
        return "(%s %s %s)" % (repr(self.l), self.op, repr(self.r))

def _IsScalar(c):
    return isinstance(other, float) or isinstance(other, int)

class Vector(object):
    def __init__(self, members):
        self.members = members


    def __add__(self, other):
        if not isinstance(other, Vector):
            raise Exception('Other operand must be Vector for operator "+"')

    def __mul__(self, other):
        if not _IsScalar(other):
            raise Exception()



class Variable(Expression):
    def __init__(self, registry, name):
        self.name = name
        self.registry = registry

    def __repr__(self):
        return self.name

class VariableRegistry(object):
    def __init__(self):
        self.v_list = []
        self.e_list = []

    def New(self, name=None):
        variable_name = ("Variable_%d" % (len(self.v_list), ))
        if not name is None:
            variable_name = name
        variable = Variable(self, variable_name)
        self.v_list.append(variable)
        return variable

    def Bind(self, l, op, r):
        if isinstance(l, tuple) and isinstance(r, tuple):
            if len(l) != len(r):
                raise Exception('Bind arity mismatch; len(%s) != len(%s)' % (l, r))
            for l_elem,r_elem in zip(l, r):
                self.Bind(l_elem, op, r_elem)
            return
        self.e_list.append(Expression(op, l, r))

    def Dump(self):
        return '\n'.join(repr(x) for x in self.e_list)

registry = VariableRegistry()

class Compound(object):
    def V(self, name):
        return registry.New("%s::%s" % (self.name, name))
