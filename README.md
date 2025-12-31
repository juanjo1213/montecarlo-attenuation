\# Monte Carlo Attenuation Simulation



\## Overview



This project implements a Monte Carlo simulation to model the attenuation

of monoenergetic photon radiation in a homogeneous material.



The simulation is designed with an engineering-oriented approach, including:

\- physically consistent modeling,

\- statistical uncertainty estimation,

\- analytical validation,

\- convergence analysis.



The project serves as a reference implementation of Monte Carlo methods

applied to radiation transport problems with industrial relevance.



---



\## Physical Model



The model considers monoenergetic photons propagating through a homogeneous

material of thickness \\( x \\).



Photon interactions are modeled using an exponential free-path distribution

defined by the linear attenuation coefficient \\( \\mu \\).



The analytical solution for the transmission probability is:



\\\[

T(x) = e^{-\\mu x}

\\]



This analytical expression is used to validate the Monte Carlo results.



---



\## Monte Carlo Methodology



For each particle history:



1\. A random free path is sampled from an exponential distribution.

2\. The interaction position is compared against the material thickness.

3\. Energy deposition is recorded if an interaction occurs.

4\. Transmission is counted otherwise.



Statistical quantities are estimated from repeated sampling.



---



\## Project Structure



montecarlo-attenuation/

│

├── src/

│ └── montecarlo.py # Core Monte Carlo simulation

│

├── analysis/

│ ├── validation.py # Analytical validation

│ ├── run\_validation.py # Validation execution script

│ ├── convergence.py # Convergence study

│ └── run\_convergence.py # Convergence execution script

│

├── examples/

│

├── report/

│

└── README.md





---



\## How to Run



\### Requirements



\- Python 3.9+

\- NumPy

\- Matplotlib (for convergence plots)



Install dependencies:



```bash

pip install numpy matplotlib



Run Analytical Validation



From the project root:



python analysis/run\_validation.py



This script compares Monte Carlo results against the analytical solution

and reports relative errors.



Run Convergence Study



python analysis/run\_convergence.py





This produces:



-numerical convergence data,



-log-log convergence plots,



-verification of the  1/sqrt(N) Monte Carlo error scaling.



Validation and Reliability



The simulation is validated by:



direct comparison with the analytical attenuation law,



statistical uncertainty estimation,



convergence analysis over increasing sample sizes.



The observed error behavior follows the expected Monte Carlo convergence rate.





Possible Extensions



This framework is designed to be extensible, including:



additional interaction physics (e.g. Compton scattering),



higher-dimensional geometries,



performance optimization (Numba / GPU),



integration into larger simulation pipelines.





Author



Juan José Salazar

Physicist specialized in computational modeling and Monte Carlo simulation.











