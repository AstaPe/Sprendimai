from namu_darbai.classes.circle2 import Circle

circle = Circle(radius=5)

circle_area = circle.area()
circle_circumference = circle.circumference()

print(f'Apskritimo plotas: {circle_area:.2f}')
print(f'Apskritimo perimetras: {circle_circumference:.2f}')
