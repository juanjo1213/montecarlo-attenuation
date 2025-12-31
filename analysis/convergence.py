import numpy as np
from src.montecarlo import montecarlo_attenuation

def convergence_study(
        N_values,
        mu,
        x_max,
        bins=50,
        seed=42
):
    """
    Performs a Monte Carloconvergence study comparing numerical
    and analytical transmission.
    """

    T_analytical=np.exp(-mu*x_max)
    results=[]

    for N in N_values:
        sim=montecarlo_attenuation(
            N=N,
            mu=mu,
            x_max=x_max,
            bins=bins,
            seed=seed
        )

        T_mc=sim["transmitted_fraction"]
        stat_err=sim["statistical_error"]

        abs_error=abs(T_mc-T_analytical)
        rel_error=abs_error/T_analytical

        results.append({
            "N": N,
            "T_mc": T_mc,
            "T_analytical": T_analytical,
            "absolute_error": abs_error,
            "relative_error": rel_error,
            "statistical_error": stat_err
        })

    return results