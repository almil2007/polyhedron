# Метод изображения полиэдра
def draw(self, tk):
    # ...
    # Добавлено
    polyedr_area = 0
    for e in self.edges:
        for f in self.facets:
            e.shadow(f)
        for s in e.gaps:
            tk.draw_line(e.r3(s.beg), e.r3(s.fin))