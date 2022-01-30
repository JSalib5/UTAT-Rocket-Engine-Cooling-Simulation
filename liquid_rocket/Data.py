import pandas as pd
import numpy as np

class Data():
    """Read and call data.

       Typical usage example:

            data = Data('data/data_v4.csv')
            t = data.t
            print('The simulation time is:', t)
    """

    def __init__(self, data_source):
        """Inits Data with CSV data source."""
        self.data_source = data_source
        self.data = pd.read_csv(self.data_source)
        self.set_variables()

    def set_variables(self):
        """Reads and sets variables from CSV."""
        self.t                  = self.variable('t')
        self.OF                 = self.variable('OF')
        self.Pcc                = self.variable('Pcc')
        self.Tcc                = self.variable('Tcc')
        self.Pe                 = self.variable('Pe')
        self.Te                 = self.variable('Te')
        self.thrust             = self.variable('thrust')
        self.Isp                = self.variable('Isp')
        self.x                  = self.variable('x')
        self.y                  = self.variable('y')
        self.u                  = self.variable('u')
        self.v                  = self.variable('v')
        self.Ax                 = self.variable('Ax')
        self.Ay                 = self.variable('Ay')
        self.m_ox               = self.variable('m_ox')
        self.n_ox               = self.variable('n_ox')
        self.T_ox               = self.variable('T_ox')
        self.P_ox               = self.variable('P_ox')
        self.mdot_ox            = self.variable('mdot_ox')
        self.rho_ox             = self.variable('rho_ox')
        self.m_f                = self.variable('m_f')
        self.n_f                = self.variable('n_f')
        self.T_f                = self.variable('T_f')
        self.P_f                = self.variable('P_f')
        self.mdot_f             = self.variable('mdot_f')
        self.rho_f              = self.variable('rho_f')
        self.t_burn             = self.variable('t_burn')
        self.Pcc_nominal        = self.variable('Pcc_nominal')
        self.mdot_ox_nominal    = self.variable('mdot_ox_nominal')
        self.OF_nominal         = self.variable('OF_nominal')
        self.diameter           = self.variable('diameter')
        self.injector_Cd        = self.variable('injector_Cd')
        self.dt                 = self.variable('dt')
        self.gamma              = self.variable('gamma')
        self.specific_gas_const = self.variable('specific_gas_const')
        self.gas_const          = self.variable('gas_const')

    def variable(self, var):
        """Modifies values from pandas dataframe to 2D numpy column."""
        temp = self.data[var].to_numpy().reshape(-1,1)

        if np.isnan(temp).any():
            return float(temp[0])

        return temp
