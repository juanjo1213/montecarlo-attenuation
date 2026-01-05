import numpy as np

MEC2 = 0.511  # MeV


def sample_compton_kn(E):
    """
    Samples Compton scattering angle and energy
    using the Klein–Nishina formula (Kahn method).
    """

    alpha = E / MEC2

    while True:
        r1 = np.random.rand()
        r2 = np.random.rand()
        r3 = np.random.rand()

        if r1 < (1 + 2 * alpha) / (1 + 3 * alpha):
            eps = 1.0 / (1.0 + 2.0 * alpha * r2)
        else:
            eps = 1.0 + 2.0 * alpha * r2

        cos_theta = 1.0 - (eps - 1.0) / alpha

        g = 1.0 - eps + 1.0 / (1.0 - eps)

        if r3 <= g:
            E_new = eps * E
            return cos_theta, E_new
