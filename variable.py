class Expression(object):
    def __init__(self, op, l, r):
        self.l = l
        self.r = r
        self.op = op

    def __add__(self, other):
        return Expression('+', self, other)

    def __radd__(self, other):
        return self.__add__(other)

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
        if self.op == '**':
            if not _IsScalar(self.r):
                raise Exception("Non-scalar powers not supported")
            if self.r == 0.5:
                return "sqrt(%s)" % (repr(self.l), )
            return "*".join(repr(self.l) for _ in range(int(self.r)))
        return "(%s %s %s)" % (repr(self.l), self.op, repr(self.r))


def _IsScalar(c):
    return isinstance(c, float) or isinstance(c, int)


class Vector(Expression):
    def __init__(self, members):
        self.members = members

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise Exception('Other operand must be Vector for operator "+"')
        return Vector([
            elem + other_elem
            for elem, other_elem in zip(self.members, other.members)
        ])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise Exception('Other operand must be Vector for operator "+"')
        return Vector([
            elem - other_elem
            for elem, other_elem in zip(self.members, other.members)
        ])

    def __mul__(self, other):
        if not _IsScalar(other):
            raise Exception('Vector multiplier must be scalar')
        return Vector([elem * other for elem in self.members])

    def __pow__(self, other):
        raise Exception('Vectors cannot be exponentiated')

    def Magnitude(self):
        return sum([elem**2 for elem in self.members])**0.5

    def Unit(self):
        return Vector([elem / self.Magnitude() for elem in self.members])

    def __repr__(self):
        return "<%s>" % (', '.join(str(member) for member in self.members), )


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

    def BindIterables(self, l, op, r):
        if len(l) != len(r):
            raise Exception('Bind arity mismatch; len(%s) != len(%s)' % (l, r))
        for l_elem, r_elem in zip(l, r):
            self.Bind(l_elem, op, r_elem)

    def Bind(self, l, op, r):
        # print("Bind invoked with %s %s %s" % (l, op, r))
        if isinstance(l, tuple) and isinstance(r, tuple):
            self.BindIterables(l, op, r)
            return
        if isinstance(l, Vector) and isinstance(r, Vector):
            self.BindIterables(l.members, op, r.members)
            return
        self.e_list.append(Expression(op, l, r))

    def Dump(self):
        return (('\n'.join(
            ('var float: %s;' % (v.name, ))
            for v in self.v_list)) + '\n' + ('\n'.join(
                ('constraint %s;' % (repr(x), )) for x in self.e_list)))


registry = VariableRegistry()


class Compound(object):
    def V(self, name):
        return registry.New("%s_%s" % (self.name, name))
