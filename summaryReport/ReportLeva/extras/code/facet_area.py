    # Площадь треугольника (вспомогательный метод)
    @staticmethod
    def _area(a, b, c):
        return abs(0.5 * ((a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0])))


    def facet_area(self):
        sum_area = 0
        if self.condition() == True:
            for i in range(len(self.vertexes) - 1):
                sum_area += self._area(R3.xy(self.vertexes[0]), R3.xy(self.vertexes[i]), R3.xy(self.vertexes[i + 1]))
        return sum_area