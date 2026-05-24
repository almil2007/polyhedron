def condition(self):
    flag_center = False
    flag_vertex = False
    if R3.xy(self.center())[0] ** 2 + R3.xy(self.center())[1] ** 2 > 1:
        flag_center = True
    for i in range(len(self.vertexes)):
        if R3.xy(self.vertexes[i])[0] ** 2 + R3.xy(self.vertexes[i])[1] ** 2 > 1:
            flag_vertex = True
            break
    if flag_vertex == True and flag_center == True:
        return True
    else:
        return False