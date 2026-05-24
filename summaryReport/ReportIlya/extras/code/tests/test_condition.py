def test_condition_good(self):
    """Центр и хотя бы одна вершина строго вне x^2+y^2=1"""
    verts = [R3(2.0, 0.0, 0.0), R3(3.0, 0.0, 0.0), R3(2.5, 1.5, 0.0)]
    f = Facet(verts)
    self.assertTrue(f.condition())
def test_condition_center_inside(self):
    """Центр внутри круга, условие должно быть False"""
    verts = [R3(0.1, 0.0, 0.0), R3(1.5, 0.0, 0.0), R3(0.0, 1.5, 0.0)]
    f = Facet(verts)
    self.assertFalse(f.condition())
def test_condition_all_inside(self):
    """Все точки внутри круга"""
    verts = [R3(0.2, 0.0, 0.0), R3(0.3, 0.0, 0.0), R3(0.0, 0.4, 0.0)]
    f = Facet(verts)
    self.assertFalse(f.condition())
def test_condition_boundary_point(self):
    """Вершина точно на окружности (x^2+y^2=1) -> не считается 'хорошей'"""
    verts = [R3(1.0, 0.0, 0.0), R3(0.0, 1.0, 0.0), R3(0.7, 0.7, 0.0)]
    f = Facet(verts)
    # Если все вершины <= 1, условие должно быть False
    self.assertFalse(f.condition())