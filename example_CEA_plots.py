from rocketcea.cea_obj_w_units import CEA_Obj
from pylab import *
from matplotlib.pyplot import figure

"""this does not use our CEA object, but it shoul -> TODO """
"""NOTE: if using windows make sure to open xming"""

MR_min = 1.1
MR_max = 10
Pcc = 350.
area_ratio = 3.887
# area_ratio_range = [2., 3.887, 10.]
area_ratio_range = [2.00, 3.90, 10.0]
pcc_range = [100., 200., 350., 500., 600.]
Pcc_temp = Pcc
cea = CEA_Obj(propName='', oxName='N2O', fuelName="Ethanol", temperature_units='K')

'''
ISP Plot: costant area_ratio, vary Pcc
'''
figure()
for Pcc_temp in pcc_range:
    ispArr = []
    MR = MR_min
    mixture_ratios = []
    while MR < MR_max:
        ispArr.append( cea(Pcc_temp, MR, area_ratio ))
        mixture_ratios.append(MR)
        MR += 0.05
    plot(mixture_ratios, ispArr, label='Arearatio = 5, Pcc %g' % Pcc_temp)

legend(loc='best')
grid(True)
title( cea.desc )
xlabel( 'Mixture Ratio' )
ylabel( 'Isp ODE (sec)' )
# savefig('cea_isp_plot.png', dpi=300)
show()

'''
ISP Plot: costant Pcc, vary area_ratio
'''
figure()
# figure(figsize=(6, 3.8), dpi=300)

for area_ratio_temp in area_ratio_range:
    ispArr = []
    MR = MR_min
    mixture_ratios = []
    while MR < MR_max:
        ispArr.append( cea(Pcc, MR, area_ratio_temp ))
        mixture_ratios.append(MR)
        MR += 0.05
    # plot(mixture_ratios, ispArr, label='N$_2$O-Ethanol, P$_{cc}$ = 350 psi, Area Ratio = %g' % area_ratio_temp)
    plot(mixture_ratios, ispArr, label='Area Ratio = %g' % area_ratio_temp)
plot(3, 245.5, 'ro')
legend(loc='best')
grid(True)
# title( cea.desc )
xlabel( 'Oxidizer to Fuel Ratio (OF)' )
ylabel( 'I$_{sp}$ (s)' )
# savefig('isp.png', dpi=300)
show()


'''
Chamber Temp Plot
'''
Pcc = 350.
area_ratio = 3.887

chamber_temperature = []
mixture_ratios = []
MR = MR_min

figure()
# figure(figsize=(6, 3.8), dpi=300)

while MR < MR_max:
    chamber_temperature.append(cea.get_Temperatures( Pc=Pcc, MR=MR, eps=area_ratio, frozen=0, frozenAtThroat=0)[0])
    # chamber_temperature.append(cea.get_Temperatures( Pc=Pcc, MR=MR, eps=area_ratio, frozen=1, frozenAtThroat=1)[0])
    mixture_ratios.append(MR)
    MR += 0.05

# plot(mixture_ratios, chamber_temperature, label='N$_2$O-Ethanol, P$_{cc}$ = 350 psi, Area Ratio = 3.9')
plot(mixture_ratios, chamber_temperature, label='Area Ratio = 3.9')
plot(3, 2676, 'ro')

legend(loc='best')
grid(True)
# title(cea.desc)
xlabel('Oxidizer to Fuel Ratio (OF)')
ylabel( 'Chamber Temperature (K)' )
# savefig('chamberTemperature', dpi=300)
show()
