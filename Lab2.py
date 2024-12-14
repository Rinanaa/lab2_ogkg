import matplotlib.pyplot as plt

file_path = "DS1.txt"  
points = []

with open(file_path, "r") as file:
    for line in file:
        x, y = map(int, line.strip().split())
        points.append((x, y))

canvas_width = 960
canvas_height = 540
dpi = 72

x_coords = [x for x, y in points]
y_coords = [y for x, y in points]

plt.figure(figsize=(canvas_width / dpi, canvas_height / dpi), dpi=dpi)
plt.scatter(x_coords, y_coords, c="red", marker="o", s=5)
plt.axis("off")

output_file = "DS1.png"
plt.savefig(output_file)
plt.show()

print(f"Графік збережено у файл: {output_file}")
