def test_facet_area_positive(self):
    """Площадь треугольника в проекции при порядке вершин против часовой стрелки"""
    # Грань далеко от начала координат, чтобы condition() == True
    verts = [R3(3.0, 0.0, 0.0), R3(5.0, 0.0, 0.0), R3(3.0, 2.0, 0.0)]
    f = Facet(verts)
    # Ожидаемая площадь: 0.5 * |2*2| = 2.0
    self.assertAlmostEqual(f.area, 2.0)
def test_facet_area_zero_when_bad(self):
    """Если условие 'хорошести' не выполняется, area должна быть 0 (согласно текущей реализации)"""
    verts = [R3(0.1, 0.0, 0.0), R3(0.2, 0.0, 0.0), R3(0.0, 0.3, 0.0)]
    f = Facet(verts)
    self.assertAlmostEqual(f.area, 0.0)