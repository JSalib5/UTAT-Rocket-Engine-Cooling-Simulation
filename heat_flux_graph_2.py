import numpy as np
import matplotlib.pyplot as plt
from rocketcea.cea_obj import CEA_Obj

### References
# [1]

### Required functions
def get_hg(A, Dt, visc, c_p, Pr, Pcc, g, c_star, r_c, At, sigma):
    '''
    (float) --> (float)

    returns the h_g  value as function of local cross sectional area in W/m^2-K

    '''

    h_g = (41.8565/(Dt**0.2)) * (((visc**0.2) * c_p)/(Pr**0.6)) * (((Pcc * g )/c_star)**0.8) * ((Dt/r_c)**0.1) * ((At/A)**0.9) * sigma

    return h_g

if __name__ == "__main__":

    ### Reading in x-coordiantes and y_coordinates of nozzle
    f = open("liquid_rocket_nozzle_SI.txt", "r")
    coord_list = f.read().split()
                                                                  # units
    x_coord = []                                                  # m
    y_coord = []                                                  # m
    A = []                                                        # m^2, position varying quantity

    for i in range(0, len(coord_list), 3):
        x_coord.append(float(coord_list[i]))

    for i in range(1, len(coord_list), 3):
        y_coord.append(float(coord_list[i]))

    for i in range(len(y_coord)):
        A.append(np.pi*(y_coord[i])**2)

    x_coord_mod = [element * 1000 for element in x_coord]         # mm
    y_coord_mod = [element * 1000 for element in y_coord]         # mm


    ### Computing heat transfer coefficient

    # create CEA object
    isp_obj = CEA_Obj(propName = "", oxName = "N2O", fuelName = "ETHANOL")

    ### Time varying quantities
    f = open("rocket_parameter_data.txt", "r")
    data = f.read().split()

    t_list = []                                                    # s
    Pcc_list = []                                                  # bar
    Tcc_list = []                                                  # K
    OF_list = []

    for i in range(4, len(data), 4):
        t_list.append(float(data[i]))

    for i in range(5, len(data), 4):
        OF_list.append(float(data[i]))

    for i in range(6, len(data), 4):
        Pcc_list.append(float(data[i])* 0.0689476 )

    for i in range(7, len(data), 4):
        Tcc_list.append(float(data[i]))

    q_max = 0
    q_max_list = []
    hg_max_list = []
    xy_list = []

    ### Iterative approach to finding the timestep pertaining to highest q_max

    for j in range(len(t_list)):

        # constant quantities                                                                      # units
        exp_ratio = 3.9
        OF = OF_list[j]
        Tw = 1000                                                                                  # K
        Tcc = Tcc_list[j]                                                                          # K
        Pcc = Pcc_list[j]                                                                          # bar
        M = isp_obj.get_MachNumber(Pc=Pcc, MR=OF, eps=exp_ratio, frozen=0, frozenAtThroat=0)       #: frozen = flag (0=equilibrium, 1=frozen)
                                                                                                   #: frozenAtThroat=flag, 0=frozen in chamber, 1=frozen at throat

        u_son = isp_obj.get_Chamber_SonicVel(Pc=Pcc, MR=OF, eps=exp_ratio)                         # ft/s
        u_e = M * u_son * 0.3048                                                                   # ft/s -> m/s


        Dt = 1.1828914173 * 0.0254                                                                 # m
        At = (np.pi/4) * (Dt**2)                                                                   # m^2
        r_c = 0.5*Dt                                                                               # m
        g = 9.81                                                                                   # m/s
        c_star = isp_obj.get_Cstar(Pc=Pcc, MR=OF) * 0.3048                                         # ft/s -> m/s

        # transport properties
        tp_1 = isp_obj.get_Chamber_Transport(Pc=Pcc, MR=OF, eps=exp_ratio, frozen=0)
        tp_2 = isp_obj.get_Chamber_MolWt_gamma(Pc=Pcc, MR=OF, eps=exp_ratio)

        # constant quantities
        c_p = tp_1[0] * 4.184e3                                                                    # BTU/(lbm-degR) -> J/kgK
        visc = tp_1[1] * 0.0001                                                                    # millipoise -> Pa-s
        Pr = tp_1[3]
        gamma = tp_2[1]
        R = Pr**(1/3)
        To = Tcc + 0.5 *(((u_e)**2)/(c_p * 4.184e3))                                               # K


        # Bartz model
        zeta = 1 + (((gamma - 1)/2) * M**2)
        Taw = To * (1 + (((gamma - 1)/2) * R * M**2))/(1 + ((gamma - 1)/2) * M**2)                 # K

        sigma = 1/((((0.5 * (Tw/To)) * zeta + 0.5)**0.68) * ((zeta)**0.12))

        # heat transfer coefficient iteration
        hg_list = []
        for area in A:
            hg_list.append(get_hg(area, Dt, visc, c_p, Pr, Pcc, g, c_star, r_c, At, sigma))

        # computing heat flux

        q_list = []

        for coefficents in hg_list:
            q_list.append(coefficents * (Taw - Tw))

        q_max = max(q_list)
        q_max_list.append(q_max)
        hg_max_list.append(max(hg_list))
        xy_list.append((x_coord[q_list.index(q_max)],y_coord[q_list.index(q_max)]))


    ### Graph 1 (note: highest q_max was last timestep)
    superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

    fig, (ax1, ax3) = plt.subplots(2)
    ax2 = ax1.twinx()
    ax1.plot(x_coord, hg_list, 'b-')
    ax2.plot(x_coord, q_list, 'r-' ,)
    ax1.set_ylim(0, 30000)
    ax2.set_ylim(0, 3e7)

    ax1.set_xlabel('Axial Station Along Chamber, m')
    ax1.set_ylabel('Gas Side Convective Coeff., W/' + 'm2'.translate(superscript) + 'K', color = 'b')
    ax2.set_ylabel('Heat Flux, W/' + 'm2'.translate(superscript), color = 'r')

    ax3.plot(x_coord_mod, y_coord_mod, '-', color = 'g' )
    ax3.set_xlabel('Axial Station Along Chamber, mm')
    ax3.set_ylabel('Thrust Chamber Radius, mm', color = "g")
    ax3.set_ylim(0,None)

    plt.title('Gas Side Convective Coeff. & Heat Flux vs. Axial Station' )
    plt.show()

    ### Graph 2

    superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

    fig, ax4 = plt.subplots(1)
    ax5 = ax4.twinx()
    ax4.plot(t_list, hg_max_list, 'b-')
    ax5.plot(t_list, q_max_list, 'r-' ,)
    ax4.set_ylim(18850, 21000)
    ax5.set_ylim(2.5e7, 2.85e7)

    ax4.set_xlabel('Time, s')
    ax4.set_ylabel('Max. Gas Side Convective Coeff., W/' + 'm2'.translate(superscript) + 'K', color = 'b')
    ax5.set_ylabel('Max. Heat Flux, W/' + 'm2'.translate(superscript), color = 'r')

    plt.title('Max. Gas Side Convective Coeff. & Max. Heat Flux vs. Time' )
    plt.show()













