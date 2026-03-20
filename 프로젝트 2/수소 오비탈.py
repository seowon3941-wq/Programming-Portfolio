import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz
from scipy.special import sph_harm

def numerov_wavefunction(n, l, r_max=20, dr=0.01):
    E = -1.0/(2*n*n)
    r = np.arange(dr, r_max, dr)

    def V_eff(rr):
        return -1/rr + l*(l+1)/(2*rr*rr)
    
    g = 2*(E - V_eff(r))
    u = np.zeros_like(r)
    u[0] = 0.0
    u[1] = 1e-6

    for i in range(1, len(r)-1):
        u[i+1] = (2*(1 - 5*dr*dr*g[i]/12)*u[i] - (1 + dr*dr*g[i-1]/12)*u[i-1]) / (1 + dr*dr*g[i+1]/12)

    norm = np.sqrt(cumtrapz(u**2, r, initial=0)[-1])
    u /= norm
    R = u / r
    return r, R

def plot_orbital_numerical(n, l, m, bound=8, n_pts=5000):
    r_vals, R_vals = numerov_wavefunction(n, l)

    u = np.random.rand(n_pts)
    cost = 2*np.random.rand(n_pts) - 1
    phi = 2*np.pi*np.random.rand(n_pts)

    r3d = bound * u**(1/3)
    theta3d = np.arccos(cost)

    x = r3d*np.sin(theta3d)*np.cos(phi)
    y = r3d*np.sin(theta3d)*np.sin(phi)
    z = r3d*np.cos(theta3d)

    r_xyz = np.sqrt(x*x + y*y + z*z)
    R_interp = np.interp(r_xyz, r_vals, R_vals)

    theta = np.arccos(np.clip(z/r_xyz, -1, 1))
    phi_xyz = np.arctan2(y, x)

    Y_lm_vals = sph_harm(m, l, phi_xyz, theta)
    psi_vals = R_interp * Y_lm_vals
    density = np.abs(psi_vals)**2

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')

    sc = ax.scatter(x, y, z, c=density, cmap='viridis', s=3)
    ax.set_title(f"Numerical Orbital n={n}, l={l}, m={m}")
    ax.set_xlim(-bound, bound)
    ax.set_ylim(-bound, bound)
    ax.set_zlim(-bound, bound)

    plt.colorbar(sc, label="Probability density")
    plt.show()

n, l, m = map(int, input().split())
plot_orbital_numerical(n, l, m)