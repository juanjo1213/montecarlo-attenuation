import numpy as np
from src.montecarlo import montecarlo_attenuation

def validate_attenuation(
        N,
        mu,
        x_max,
        bins=50,
        seed=123

):
    
    """
    Validates Monte carlos attenuation against analytical solution.
    """

    # --- Monte Carlo simulation----
    results=montecarlo_attenuation(
        N=N,
        mu=mu,
        x_max=x_max,
        bins=bins,
        seed=seed
    )

    T_mc=results["transmitted_fraction"]
    sigma_mc=results["statistical_error"]

    #---Analytical solution---
    T_analytical=np.exp(-mu*x_max)

    #---Errors---
    absolute_error=abs(T_mc-T_analytical)
    relative_error=absolute_error/T_analytical


    return{
        "T_mc":T_mc,
        "T_analytical": T_analytical,
        "absolute_error":absolute_error,
        "relative_error":relative_error,
        "statistical_error":sigma_mc
    }