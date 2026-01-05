from src.montecarlo_scattering import montecarlo_scattering_kn

results = montecarlo_scattering_kn(
    N=50_000,
    mu_abs=0.2,
    mu_scat=0.8,
    x_max=10.0,
    E0=1.0,
    seed=42
)

print(results)
