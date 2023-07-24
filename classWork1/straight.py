import matplotlib.pyplot as plt

def draw_straight_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    error = dx // 2
    y_step = 1 if y1 < y2 else -1

    y = y1
    points = []

    for x in range(x1, x2 + 1):
        coord = (y, x) if steep else (x, y)
        points.append(coord)
        error -= dy
        if error < 0:
            y += y_step
            error += dx

    x_points, y_points = zip(*points)

    plt.plot(x_points, y_points, marker='o', linestyle='-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Straight Line')
    plt.grid()
    plt.show()

# Example usage
draw_straight_line(1, 2, 8, 12)
