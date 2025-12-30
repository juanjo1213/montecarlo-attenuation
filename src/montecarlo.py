import numpy as np 

def montecarlo_attenuation(
    N,
    mu,
    x_max,
    E0=1.0,
    bins=50,
    seed=None
):

     if seed is not None:
            np.random.seed(seed)
     
     transmitted_count=0
     absorbed_energy=0.0
     dose_profile=np.zeros(bins)
     
     bin_width=x_max/bins
     
     for _ in range(N):
        r=np.random.rand()
        s=-np.log(r)/mu
     
        if s < x_max:
            absorbed_energy += E0
            bin_index=int(s/bin_width)
            dose_profile[bin_index] += E0
        else:
            transmitted_count+=1
     
     transmitted_fraction=transmitted_count/N 
     absorbed_fraction=1.0-transmitted_fraction
     
     dose_profile /=N 
     
     sigma_transmission=np.sqrt(     
        transmitted_fraction*(1.0-transmitted_fraction)/N
     )
     
     return{
     "transmitted_fraction": transmitted_fraction,
     "absorbed_fraction": absorbed_fraction,
     "absorbed_energy": absorbed_energy/N,
     "dose_profile": dose_profile,
     "statistical_error":sigma_transmission
     }