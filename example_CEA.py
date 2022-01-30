import numpy as np
import time

from liquid_rocket.CEA import CEA

def main():
    # instantiate using default values
    cea = CEA()

    print('--------------------------------------------------')
    print('Temperature values for default engine conditions')
    print('Temperature at the   chamber', cea.T_c, 'K')
    print('Temperature at the throat', cea.T_t, 'K')
    print('Temperature at the exit', cea.T_e, 'K')
    print('--------------------------------------------------')

    # update_conditions -> if you want to update engine conditions and keep using the same object
    cea.update_conditions(Pcc=325, OF=2.5, area_ratio=3, Pamb=15)

    print('Temperature values for updated engine conditions')
    print('Temperature at the chamber', cea.T_c, 'K')
    print('Temperature at the throat', cea.T_t, 'K')
    print('Temperature at the exit', cea.T_e, 'K')
    print('--------------------------------------------------')

    # print(cea.get_full_ouput()) # only for debugging

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- computation time: %s seconds ---" % np.around(time.time() - start_time, decimals=3))
