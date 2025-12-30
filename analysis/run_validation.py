from analysis.validation import validate_attenuation

# ---Simulation parameters ---
N=200_000
mu=0.5
x_max=10.0

validation=validate_attenuation(
    N=N,
    mu=mu,
    x_max=x_max
)

print("Monte carlo transmission:", validation["T_mc"])
print("Analytical transmission:", validation["T_analytical"])
print("Relative error:", validation["relative_error"])
print("Statistical error:", validation["statistical_error"])
