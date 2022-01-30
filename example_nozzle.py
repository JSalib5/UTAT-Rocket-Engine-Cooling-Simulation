import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

def main():
    nozzle = pd.read_csv('data/liquid_rocket_nozzle_SI.csv')

    nozzle_x = nozzle['x'].to_numpy().reshape(-1,1)
    nozzle_y = nozzle['y'].to_numpy().reshape(-1,1)
    nozzle_z = nozzle['z'].to_numpy().reshape(-1,1)

    fig, ax = plt.subplots()
    plt.plot(nozzle_x, nozzle_y, color='k', linewidth=2)
    plt.xlabel('x-coordinates (m)' )
    plt.ylabel('y-coordinates (m)' )
    ax.axis('equal')
    ax.set(xlim=(-0.02, 0.05), ylim=(0, 0.03))
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- computation time: %s seconds ---" % np.around(time.time() - start_time, decimals=3))
