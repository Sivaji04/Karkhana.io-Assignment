import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import simpson



class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=100):
        self.R = R          # Radius from center to the strip
        self.w = w          # Width of the strip
        self.n = n          # Resolution
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, n),
            np.linspace(-w / 2, w / 2, n)
        )
        self.x, self.y, self.z = self._compute_coordinates()

    def _compute_coordinates(self):
        """Compute (x, y, z) coordinates from parametric equations."""
        u = self.u
        v = self.v
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def surface_area(self):
        """Approximate the surface area using numerical integration."""
        # Calculate partial derivatives
        du = 2 * np.pi / (self.n - 1)
        dv = self.w / (self.n - 1)

        xu, xv = np.gradient(self.x, du, dv, axis=(0, 1))
        yu, yv = np.gradient(self.y, du, dv, axis=(0, 1))
        zu, zv = np.gradient(self.z, du, dv, axis=(0, 1))

        # Cross product of partial derivatives
        cross_x = yu * zv - zu * yv
        cross_y = zu * xv - xu * zv
        cross_z = xu * yv - yu * xv

        area_element = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        area = simpson(simpson(area_element, self.v[0]), self.u[:, 0])
        return area

    def edge_length(self):
        """Approximate the edge length along the boundary of the strip."""
        # Only use v = -w/2 and v = w/2 edges
        edges = [self.v[0], self.v[-1]]
        total_length = 0

        for edge_v in edges:
            u_vals = np.linspace(0, 2 * np.pi, self.n)
            x = (self.R + edge_v * np.cos(u_vals / 2)) * np.cos(u_vals)
            y = (self.R + edge_v * np.cos(u_vals / 2)) * np.sin(u_vals)
            z = edge_v * np.sin(u_vals / 2)

            dx = np.gradient(x)
            dy = np.gradient(y)
            dz = np.gradient(z)

            ds = np.sqrt(dx**2 + dy**2 + dz**2)
            total_length += simpson(ds, u_vals)

        return total_length

    def plot(self):
        """Visualize the Möbius strip in 3D."""
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, color='skyblue', edgecolor='gray', alpha=0.8)
        ax.set_title("Möbius Strip")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == "__main__":
    mobius = MobiusStrip(R=1.0, w=0.4, n=200)
    mobius.plot()
    print(f"Surface Area ≈ {mobius.surface_area():.4f}")
    print(f"Edge Length ≈ {mobius.edge_length():.4f}")
