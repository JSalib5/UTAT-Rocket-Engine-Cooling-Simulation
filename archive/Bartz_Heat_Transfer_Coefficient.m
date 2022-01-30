% Calculation Convective Heat Transfer Coefficient using Bartz Equation %

%% (Need to determine the actual values of constants in the next step)
%-------------------------------Constants---------------------------------%
lambda = 100;   % Thermal Conductivity                              [W/m-K]
D_cc = 0.1;     % Diameter of Combustion Chamber                        [m]
D_t = 0.01;     % Diameter of the Nozzle Throat                         [m]
mu = 0.1;       % Dynamic Viscosity                                  [Pa-s]
rho = 1;        % Density                                          [kg/m^3]
v = 100;        % Velocity (Static velocity of freestream)            [m/s]
Cp = 100;       % Specific Heat Capacity                           [J/kg-K]
gamma = 1;      % Heat Capacity Ratio (Isentropic coefficient)          [-]
M = 1;          % Mach Number                                           [-]
T_aw = 1000;    % Temperature of Hot Wall (Inner Wall)                  [K]
T_0 = 1000;     % The Adiabatic (Stagnation) Wall Temperature           [K]

%-------------------------------Quantities--------------------------------%
Re = (rho * v * D_cc)/mu;       % Reynolds number (for coolant)
Pr = (mu * Cp)/lambda;          % Prandtl number (for coolant)

%-------------------------Heat Transfer Coefficient-----------------------%
sigma = 1/(((0.5*(T_aw/T_0)*(1+((gamma-1)/2)*M^2)+0.5)^0.68)*(1+ ...
    ((gamma-1)/2)*M^2)^0.12);

alpha_hc = sigma * (0.026*lambda/D_cc) * Re^0.8 * Pr^0.4 * (D_t/D_cc)^0.1;

disp(['Heat Transfer Coefficient = ', num2str(alpha_hc), ' [W/m^2-K]']);
