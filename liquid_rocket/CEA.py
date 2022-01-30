import rocketcea.cea_obj_w_units as cea_obj_SI
import rocketcea.cea_obj as CEA_Obj_imperial

# TODO
# - change to S.I. units for the following: viscosity_units, thermal_cond_units -> see "User Units" https://rocketcea.readthedocs.io/en/latest/functions.html#cea-obj-with-units

class CEA():
    """Calls NASA CEA via RocketCEA.

        NOTE:
        - look through calculate() function to see output variables
        - reference: https://rocketcea.readthedocs.io

       Typical usage example:

           cea = CEA()                                                                             # instantiate using default values
           cea = CEA(Pcc=350, OF=3, area_ratio=3.887, Pamb=14.7, oxName='N2O', fuelName='Ethanol') # instantiate using custom values

           # Major variables are below. Can change between chamber, nozzle throat,
           # and nozzle exit plane conditions by changing the end subscript:
           # _c (chamber), _t (throat), _e (exit)

           # cea.P_c	 # chamber pressure
           # cea.T_c	 # Temperatures
           # cea.rho_c	 # Densities
           # cea.Cp_c	 # HeatCapacities
           # cea.H_c	 # Enthalpies

           print('Temperature at the chamber', cea.T_c, 'K')
           print('Temperature at the throat', cea.T_t, 'K')
           print('Temperature at the exit', cea.T_e, 'K')

           cea.update_conditions(Pcc=325, OF=2.5, area_ratio=3, Pamb=15)

           cea.calculate()

           print(cea.get_full_ouput())
    """

    def __init__(self, Pcc=350, OF=3, area_ratio=3.887, Pamb=14.7, oxName='N2O', fuelName='Ethanol'):
        """Inits CEA with defaut engine values."""

        self.Pcc        = Pcc        # psia
        self.OF         = OF         # -
        self.area_ratio = area_ratio # -
        self.Pamb       = Pamb       # psia
        self.oxName     = oxName
        self.fuelName   = fuelName

        # aux
        self.frozen         = 0
        self.frozenAtThroat = 0

        #:  parameter             default             options
        #: isp_units           = 'sec',         # N-s/kg, m/s, km/s
        #: cstar_units         = 'm/s',         # m/s
        #: pressure_units      = 'psia',        # MPa, KPa, Pa, Bar, Atm, Torr
        #: temperature_units   = 'K',           # K, C, F
        #: sonic_velocity_units= 'm/sec',       # m/s
        #: enthalpy_units      = 'J/kg',        # J/g, kJ/kg, J/kg, kcal/kg, cal/g
        #: density_units       = 'kg/m^3',      # g/cc, sg, kg/m^3
        #: specific_heat_units = 'J/kg-K'       # kJ/kg-K, cal/g-C, J/kg-K (# note: cal/g K== BTU/lbm degR)
        #: viscosity_units     = 'millipoise'   # lbf-sec/sqin, lbf-sec/sqft, lbm/ft-sec, poise, centipoise
        #: thermal_cond_units  = 'mcal/cm-K-s'  # millical/cm-degK-sec, BTU/hr-ft-degF, BTU/s-in-degF, cal/s-cm-degC, W/cm-degC
        #: fac_CR, Contraction Ratio of finite area combustor (None=infinite)
        #: if make_debug_prints is True, print debugging info to terminal.

        # units
        self.isp_units            = 'sec'
        self.cstar_units          = 'm/s'
        self.pressure_units       = 'psia'
        self.temperature_units    = 'K'
        self.sonic_velocity_units = 'm/sec'
        self.enthalpy_units       = 'J/kg'
        self.density_units        = 'kg/m^3'
        self.specific_heat_units  = 'J/kg-K'
        self.viscosity_units      = 'millipoise'
        self.thermal_cond_units   = 'mcal/cm-K-s'

        # other
        self.fac_CR            = None
        self.useFastLookup     = 0
        self.makeOutput        = 0
        self.make_debug_prints = False
        self.short_output      = 1
        self.show_transport    = 1

        self.cea_imperial = CEA_Obj_imperial.CEA_Obj(oxName         = self.oxName,
                                                    fuelName        = self.fuelName)
        self.cea          = cea_obj_SI.CEA_Obj(oxName               = self.oxName,
                                               fuelName             = self.fuelName,
                                               fac_CR               = self.fac_CR,
                                               useFastLookup        = self.useFastLookup,
                                               makeOutput           = self.makeOutput,
                                               make_debug_prints    = self.make_debug_prints,
                                               isp_units            = self.isp_units,
                                               cstar_units          = self.cstar_units,
                                               pressure_units       = self.pressure_units,
                                               temperature_units    = self.temperature_units,
                                               sonic_velocity_units = self.sonic_velocity_units,
                                               enthalpy_units       = self.enthalpy_units,
                                               density_units        = self.density_units,
                                               specific_heat_units  = self.specific_heat_units,
                                               viscosity_units      = self.viscosity_units,
                                               thermal_cond_units   = self.thermal_cond_units                                        )

        self.calculate()

    def update_conditions(self, Pcc=350, OF=3, area_ratio=3.887, Pamb=14.7):
        """Updates engine conditions for an existing object."""

        self.Pcc        = Pcc        # psia
        self.OF         = OF         # -
        self.area_ratio = area_ratio # -
        self.Pamb       = Pamb       # psia
        self.calculate()

    def calculate(self):
        """Calculate/re-calculate NASA CEA values."""

        # chamber=[0], throat=[1] and exit=[2]
        self.Temperatures        = self.cea.get_Temperatures       ( Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen, frozenAtThroat=self.frozenAtThroat)
        self.Densities           = self.cea.get_Densities          ( Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen, frozenAtThroat=self.frozenAtThroat)
        self.Enthalpies          = self.cea.get_Enthalpies         ( Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen, frozenAtThroat=self.frozenAtThroat)
        # self.Entropies           = self.cea.get_Entropies          ( Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen, frozenAtThroat=self.frozenAtThroat)
        self.HeatCapacities      = self.cea.get_HeatCapacities     ( Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen, frozenAtThroat=self.frozenAtThroat)

        self.Chamber_MolWt_gamma = self.cea.get_Chamber_MolWt_gamma(Pc=self.Pcc, MR=self.OF, eps=self.area_ratio                                                         )
        self.Throat_MolWt_gamma  = self.cea.get_Throat_MolWt_gamma (Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen                                     )
        self.exit_MolWt_gamma    = self.cea.get_exit_MolWt_gamma   (Pc=self.Pcc, MR=self.OF, eps=self.area_ratio )
        # self.exit_MolWt_gamma    = self.cea.get_exit_MolWt_gamma   (Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen, frozenAtThroat=self.frozenAtThroat )

        self.Chamber_Transport   = self.cea.get_Chamber_Transport  (Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen                                     )
        self.Throat_Transport    = self.cea.get_Throat_Transport   (Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen                                     )
        self.Exit_Transport      = self.cea.get_Exit_Transport     (Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen                                     )

        self.estimate_Ambient_Isp = self.cea.estimate_Ambient_Isp (Pc =self.Pcc, MR =self.OF, eps =self.area_ratio, Pamb   =self.Pamb, frozen           =self.frozen, frozenAtThroat =self.frozenAtThroat)
        self.Isp                  = self.cea.get_Isp              (Pc =self.Pcc, MR =self.OF, eps =self.area_ratio, frozen =self.frozen, frozenAtThroat =self.frozenAtThroat                             )
        self.Cstar                = self.cea.get_Cstar            (Pc =self.Pcc, MR =self.OF                                                                                                             )

        # self.Chamber_MachNumber  = self.cea.get_Chamber_MachNumber (Pc=self.Pcc, MR=self.OF, fac_CR=self.fac_CR                                                           )
        self.MachNumber          = self.cea.get_MachNumber         (Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen, frozenAtThroat=self.frozenAtThroat  )
        self.SonicVelocities     = self.cea.get_SonicVelocities    (Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen, frozenAtThroat=self.frozenAtThroat  )

        self.PcOvPe              = self.cea.get_PcOvPe             (Pc=self.Pcc, MR=self.OF, eps=self.area_ratio, frozen=self.frozen, frozenAtThroat=self.frozenAtThroat  )
        # self.Pinj_over_Pcomb     = self.cea.get_Pinj_over_Pcomb    (Pc=self.Pcc, MR=self.OF, fac_CR=self.fac_CR                                                           )
        self.Throat_PcOvPe       = self.cea.get_Throat_PcOvPe      (Pc=self.Pcc, MR=self.OF                                                                               )

        self.P_c	= self.Pcc
        self.P_t	= self.Pcc/self.Throat_PcOvPe
        self.P_e	= self.Pcc/self.PcOvPe
        self.T_c	= self.Temperatures[0]
        self.T_t	= self.Temperatures[1]
        self.T_e	= self.Temperatures[2]
        self.rho_c	= self.Densities[0]
        self.rho_t	= self.Densities[1]
        self.rho_e	= self.Densities[2]
        self.Cp_c	= self.HeatCapacities[0]
        self.Cp_t	= self.HeatCapacities[1]
        self.Cp_e	= self.HeatCapacities[2]
        self.H_c	= self.Enthalpies[0]
        self.H_t	= self.Enthalpies[1]
        self.H_e	= self.Enthalpies[2]
        # self.S_c	= self.Entropies[0]
        # self.S_t	= self.Entropies[1]
        # self.S_e	= self.Entropies[2]

    def get_full_ouput(self):
        """Generates full text-based NASA CEA output. Use for debugging."""

        return self.cea_imperial.get_full_cea_output(Pc=self.Pcc, MR=self.OF, eps=self.area_ratio,
                                                     frozen=self.frozen, frozenAtThroat=self.frozenAtThroat,
                                                     short_output=self.short_output, show_transport=self.show_transport)
