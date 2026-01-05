import numpy as np
from src.klein_nishina import sample_compton_kn

def montecarlo_scattering_kn(
    N,
    mu_abs,
    mu_scat,
    x_max,
    E0=1.0,
    seed=None
):
    if seed is not None:
        np.random.seed(seed)

    transmitted = 0
    absorbed = 0

    for _ in range(N):

        x = 0.0
        mu_dir = 1.0
        E = E0
        alive = True

        while alive:

            mu_tot = mu_abs + mu_scat
            s = -np.log(np.random.rand()) / mu_tot
            x_new = x + mu_dir * s

            if x_new >= x_max:
                transmitted += 1
                break

            # Interaction
            if np.random.rand() < mu_scat / mu_tot:
                # --- Klein–Nishina Compton ---
                cos_theta, E = sample_compton_kn(E)
                mu_dir = cos_theta
                x = x_new
            else:
                absorbed += 1
                alive = False

    return {
        "transmitted_fraction": transmitted / N,
        "absorbed_fraction": absorbed / N
    }
