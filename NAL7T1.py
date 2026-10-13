
import numpy as np
import matplotlib.pyplot as plt

y = np.array([0, 2, 4, 6, 8, 10], dtype=float)
x = np.array([0.0, 1.1, 1.8, 2.4, 2.0, 1.3])

h = 2

# Create forward difference table
n = len(x)
diff = np.zeros((n, n))
diff[:, 0] = x

for j in range(1, n):
    for i in range(n - j):
        diff[i, j] = diff[i + 1, j - 1] - diff[i, j - 1]

# Newton Forward Interpolation
def interpolate(value):
    p = (value - y[0]) / h
    result = diff[0, 0]
    term = 1

    for j in range(1, n):
        term *= (p - j + 1) / j
        result += term * diff[0, j]

    return result

# Generate intermediate points
y_new = np.linspace(0, 10, 500)
x_new = np.array([interpolate(v) for v in y_new])

# Left side has negative x-coordinates
x_left = -x_new

plt.figure(figsize=(6, 9))
plt.plot(x_left, y_new, 'r-', linewidth=2.5,
         label="Interpolated Left Outline")
plt.scatter(-x, y, color='blue',
            label="Original Data Points")

plt.axvline(0, color='green', linestyle='--',
            label="Vertical Midline")

plt.title("Left Half Face")
plt.xlabel("Horizontal Position (x)")
plt.ylabel("Face Height (y)")
plt.xlim(-3.5, 3.5)
plt.ylim(-0.5, 11)
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()


# Mirror the left outline
x_right = -x_left

plt.figure(figsize=(6, 9))

plt.plot(x_left, y_new, 'r-', linewidth=2.5,
         label="Left Half")

plt.plot(x_right, y_new, 'b-', linewidth=2.5,
         label="Right Half (Mirrored)")

plt.scatter(-x, y, color='red')
plt.scatter(x, y, color='blue')

plt.axvline(0, color='green', linestyle='--',
            label="Symmetry Axis")

plt.title("Complete Symmetrical Face")
plt.xlabel("Horizontal Position (x)")
plt.ylabel("Face Height (y)")
plt.xlim(-3.5, 3.5)
plt.ylim(-0.5, 11)
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()


from matplotlib.patches import Ellipse, Circle, Polygon, Arc

fig, ax = plt.subplots(figsize=(7, 10))
ax.set_facecolor('#e6f2ff')

# Fill the reconstructed face
face_x = np.concatenate([x_left, x_right[::-1]])
face_y = np.concatenate([y_new, y_new[::-1]])

ax.fill(face_x, face_y,
        color='#ffdab9',
        edgecolor='#d2a679',
        linewidth=2.5)

# Ears
for side in [-1, 1]:
    ear = Ellipse((side * 2.3, 6.3),
                  0.7, 0.9,
                  color='#ffdab9')
    ax.add_patch(ear)

# Eyes
for side in [-1, 1]:
    eye = Ellipse((side * 0.85, 7.5),
                  0.75, 0.45,
                  color='white')
    ax.add_patch(eye)

    iris = Circle((side * 0.85, 7.5),
                  0.23, color='#3975d7')
    ax.add_patch(iris)

    pupil = Circle((side * 0.85, 7.5),
                   0.12, color='black')
    ax.add_patch(pupil)

# Eyebrows
ax.plot([-1.2, -0.5], [8.2, 8.25],
        color='#4a3020', linewidth=4)

ax.plot([0.5, 1.2], [8.25, 8.2],
        color='#4a3020', linewidth=4)

# Nose
ax.plot([0, 0], [7.0, 5.4],
        color='#c68e68', linewidth=2)

nose = Ellipse((0, 5.3), 0.4, 0.25,
               color='#c68e68')
ax.add_patch(nose)

# Cheeks
for side in [-1, 1]:
    cheek = Ellipse((side * 1.3, 5.9),
                    0.8, 0.55,
                    color='lightcoral',
                    alpha=0.35)
    ax.add_patch(cheek)

# Lips
lips = Arc((0, 2.3), 1.4, 0.7,
           theta1=195, theta2=345,
           color='crimson', linewidth=3)
ax.add_patch(lips)

# Hair
hair = Polygon([
    (-1.5, 9.4),
    (-1.3, 10.4),
    (-0.6, 9.7),
    (0, 10.0),
    (0.7, 9.6),
    (1.3, 10.4),
    (1.5, 9.4)
], closed=True, color='#493126')

ax.add_patch(hair)

# Final display
ax.set_xlim(-3.3, 3.3)
ax.set_ylim(-0.5, 11)
ax.set_aspect('equal')

ax.set_title("Face with Facial Features")
ax.set_xlabel("Horizontal Position (x)")
ax.set_ylabel("Face Height (y)")

plt.show()
