import numpy as np
import matplotlib.pyplot as plt
from analysis.convergence import convergence_study

mu=0.5
x_max=10.0

N_values = [10**2, 10**3, 10**4, 10**5, 10**6]

results = convergence_study(
    N_values=N_values,
    mu=mu,
    x_max=x_max
)

# --- Extract data ---
N=np.array([r["N"] for r in results])
abs_err=np.array([r["absolute_error"] for r in results])
stat_err=np.array([r["statistical_error"] for r in results])

# --- Print table ---
for r in results:
    print(
        f"N={r['N']:>8} | "
        f"T_MC={r['T_mc']:.6f} | "
        f"RelErr={r['relative_error']:.2e}"
    )




# --- Plot convergence ---
plt.figure()
plt.loglog(N, abs_err, marker="o", label="Absolute error")
plt.loglog(N, stat_err, marker="s", linestyle="--", label="Statistical error")
plt.loglog(N, 1 / np.sqrt(N), linestyle=":", label="1/sqrt(N) reference")
plt.xlabel("Number of histories N")
plt.ylabel("Error")
plt.title("Monte Carlo Convergence Study")
plt.legend()
plt.grid(True, which="both")
plt.show()    

print(results)