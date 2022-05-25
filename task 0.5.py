def triangle_area(sidea,sideb,sidec):
 sides = (sidea + sideb + sidec ) /2
 area = (sides *(sides-sidea)*(sides-sideb)*(sides-sidec)) ** 0.5  

 return area
print(triangle_area(12,14,7))
