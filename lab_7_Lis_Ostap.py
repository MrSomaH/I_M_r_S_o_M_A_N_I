from sympy import symbols, diff, integrate, pi, sqrt
from sympy.vector import CoordSys3D

def gradient_scalar_field(scalar_field):
    x, y, z = symbols('x y z')
    gradient = [diff(scalar_field, x), diff(scalar_field, y), diff(scalar_field, z)]
    return gradient


def divergence_vector_field(vector_field):
    N = CoordSys3D('N')
    divergence = vector_field.divergence().doit()
    return divergence


def curl_vector_field(vector_field):
    N = CoordSys3D('N')
    curl = vector_field.curl().doit()
    return curl


def flux_through_surface(vector_field, surface):
    N = CoordSys3D('N')
    flux = vector_field.dot(surface.normal())
    return flux


def circulation_along_contour(vector_field, contour):
    N = CoordSys3D('N')
    circulation = vector_field.dot(contour.tangent())
    return circulation



def verify_stokes_theorem(vector_field, surface, contour):
    N = CoordSys3D('N')

    # Ліва частина теореми Стокса (інтеграл по контуру циркуляції векторного поля)
    circulation = circulation_along_contour(vector_field, contour)

    # Права частина теореми Стокса (потік векторного поля через поверхню)
    flux = flux_through_surface(curl_vector_field(vector_field), surface)

    # Обчислення обох сторін теореми і порівняння результатів
    result_left = circulation.doit()
    result_right = flux.doit()
    return result_left == result_right


def verify_divergence_theorem(vector_field, region, surface):
    N = CoordSys3D('N')

    # Ліва частина теореми Остроградського-Гауса (потік векторного поля через поверхню)
    flux = flux_through_surface(vector_field, surface)

    # Права частина теореми Остроградського-Гауса (потрібно обчислити потік дивергенції поля через об'єм)
    divergence = divergence_vector_field(vector_field)
    volume = integrate(divergence, region)
    result_right = volume

    # Обчислення обох сторін теореми і порівняння результатів
    result_left = flux.doit()
    return result_left == result_right


def check_properties_of_vector_field(vector_field):
    N = CoordSys3D('N')

    # Перевірка потенціальності (чи є ротор рівний нулю)
    is_potential = curl_vector_field(vector_field).simplify() == N.zero

    # Перевірка соленоїдальності (чи є дивергенція рівна нулю)
    is_solenoidal = divergence_vector_field(vector_field).simplify() == 0

    # Перевірка гармонічності (чи є обидва умови потенціальності та соленоїдальності виконані)
    is_harmonic = is_potential and is_solenoidal

    return is_potential, is_solenoidal, is_harmonic

check_properties_of_vector_field(x**2+y**2)