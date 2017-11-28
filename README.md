# RandomWalk

An implementation of a random walk on a regular 1D lattice: at each step in time (amount_time_stamps) the location of n particles (n_particles)
jumps to another site according to some probability distribution (probability_threshold).

The program visualizes the behavior of the particles in time and shows the behaviour of the variance which is computed as follows:
$\sigma^2= \langle x^2(t) \rangle - \langle x(t) \rangle^2 )$ as a function of $t$. 
