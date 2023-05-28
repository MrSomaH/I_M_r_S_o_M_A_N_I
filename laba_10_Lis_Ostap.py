import sympy as sp

class CCS:
    def __init__(self, x_func, y_func, z_func):
        self.x = sp.Symbol('x')
        self.y = sp.Symbol('y')
        self.z = sp.Symbol('z')
        self.x_func = x_func
        self.y_func = y_func
        self.z_func = z_func

    def local_basis(self):
        basis = [self.x_func.diff(self.x), self.y_func.diff(self.y), self.z_func.diff(self.z)]
        return basis

    def dual_basis(self):
        basis = [sp.integrate(self.x_func.diff(self.x), self.x),
                 sp.integrate(self.y_func.diff(self.y), self.y),
                 sp.integrate(self.z_func.diff(self.z), self.z)]
        return basis

    def metric_tensor(self):
        g = sp.zeros(3)
        basis = self.local_basis()
        for i in range(3):
            for j in range(3):
                g[i, j] = sp.integrate(basis[i] * basis[j], (self.x, 0, self.x), (self.y, 0, self.y), (self.z, 0, self.z))
        return g

    def is_orthogonal(self):
        g = self.metric_tensor()
        for i in range(3):
            for j in range(i + 1, 3):
                if g[i, j] != 0:
                    return False
        return True

    def lame_coefficients(self):
        basis = self.local_basis()
        lam = [sp.sqrt(basis[i].doit(basis[i])) for i in range(3)]
        return lam

    def vector_length(self):
        lam = self.lame_coefficients()
        length = sp.sqrt(self.x_func.diff(self.x)**2 + self.y_func.diff(self.y)**2 + self.z_func.diff(self.z)**2)
        return length.subs([(self.x, self.x_func), (self.y, self.y_func), (self.z, self.z_func)]), lam

    def surface_elements(self):
        lam = self.lame_coefficients()
        dx = self.x_func.diff(self.x)
        dy = self.y_func.diff(self.y)
        dz = self.z_func.diff(self.z)
        area = sp.sqrt((dy*dz)**2 + (dz*dx)**2 + (dx*dy)**2)
        volume = dx * dy * dz
        return area.subs([(self.x, self.x_func), (self.y, self.y_func), (self.z, self.z_func)]), volume.subs([(self.x, self.x_func), (self.y, self.y_func), (self.z, self.z_func)]), lam

    def jacobian(self):
        j = sp.zeros(3)
        basis = self.local_basis()
        j[0, 0] = sp.integrate(basis[0], self.x)
        j[1, 1] = sp.integrate(basis[1], self.y)
        j[2, 2] = sp.integrate(basis[2], self.z)
        return j

    def coordinate_surfaces(self):
        # Ваш код для побудови координатних поверхонь
        pass

    def coordinate_lines(self):
        # Ваш код для побудови координатних ліній
        pass


x_func = sp.sin(sp.symbols('u')) * sp.cos(sp.symbols('v'))
y_func = sp.sin(sp.symbols('u')) * sp.sin(sp.symbols('v'))
z_func = sp.cos(sp.symbols('u'))
ccs = CCS(x_func, y_func, z_func)
local_basis = ccs.local_basis()
dual_basis = ccs.dual_basis()
metric_tensor = ccs.metric_tensor()
is_orthogonal = ccs.is_orthogonal()
lame_coeffs = ccs.lame_coefficients()
vector_length, lam = ccs.vector_length()
area, volume, lam = ccs.surface_elements()
jacobian = ccs.jacobian()

print(local_basis)
print(dual_basis)
print(metric_tensor)
print(is_orthogonal)
print(lame_coeffs)
print(vector_length)
print(area)
print(volume)
print(jacobian)