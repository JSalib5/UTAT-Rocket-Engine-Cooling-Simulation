import numpy as np
import time
import matplotlib.pyplot as plt

from liquid_rocket.Data import Data

def main():
    data = Data('data/data_v4.csv')
    t = data.t
    print('The simulation time is:', t)

    plt.figure()
    plt.plot(data.t, data.Pcc, color='k', linewidth=2, label='Combustion Chamber')
    plt.legend(loc='best')
    plt.grid(True)
    plt.xlabel('Time (s)' )
    plt.ylabel('Pressure (psi)' )
    plt.show()

    plt.figure()
    plt.plot(data.t, data.Tcc, color='k', linewidth=2, label='Combustion Chamber')
    plt.legend(loc='best')
    plt.grid(True)
    plt.xlabel('Time (s)' )
    plt.ylabel('Temperature (K)' )
    plt.show()

    plt.figure()
    plt.plot(data.t, data.thrust, color='k', linewidth=2)
    plt.grid(True)
    plt.xlabel('Time (s)' )
    plt.ylabel('Thrust (N)' )
    plt.show()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- computation time: %s seconds ---" % np.around(time.time() - start_time, decimals=3))
