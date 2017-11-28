# RandomWalk

An implementation of a random walk on a regular 1D lattice.

At each step in time (amount_time_stamps) the location of n particles (n_particles)
jumps to another site according to some probability distribution (probability_threshold).
The output of this process creates the following figure:

![alt tag](https://user-images.githubusercontent.com/14283557/33336135-4ddd14f2-d46f-11e7-8145-2919ab567402.png)


Furthermore, the program also shows the behaviour of the variance which is computed as follows:
<img src="https://latex.codecogs.com/gif.latex?$\sigma^2=&space;\langle&space;x^2(t)&space;\rangle&space;-&space;\langle&space;x(t)&space;\rangle^2&space;)$" title="$\sigma^2= \langle x^2(t) \rangle - \langle x(t) \rangle^2 )$" />
The output of this computation can be seen in the following figure:

![alt tag](https://user-images.githubusercontent.com/14283557/33336178-6c7799c8-d46f-11e7-8d7b-5bc7aaa57cdf.png)
