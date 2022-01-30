%NASA B - Analytical model for liquid film cooling (pg 54)

%(list of constants and unknowns)
%-------------------------------Constants--------------------------------------------------%
W_e=100;     %Entrained flow rate                                                    [lbm/s]              
W_c=100;     %Coolant flow rate                                                      [lbm/s]
W=100;       %Total combustion chamber flow rate                                     [lbm/s]
A=100;       %Liquid Entrainment parameter                                              [in]
%Note:       %A was expressed in [in^-1] in Figure 4.7 (PDF file)
L=100;       %Liquid film cooled length                                                 [in]
z=100;       %Effective contour distance [integral will be need]                        [in]
V=100;       %Vaporization rate of the liquid surface
r=100;       %Reference entrainment factor                                               [-]
s=100;       %Mixing layer length                                                       [in]
u_e=100;     %Entrained velocity                                                      [mi/h]
u_c=100;     %Coolant velocity                                                        [mi/h]
rho_c=100;   %Density of coolant                                                  [lbm/ft^3]                                                         
rho_e=100;   %Density of entrained                                                [lbm/ft^3] 
X_e=100;     %Liquid entrainment correlation parameter
g=10;        %Gravity                                                               [ft/s^2]
T_e=100;     %Core flow 
T_if=120;    %Liquid interface temperature
delta=10;    %An empirical entrainment augmentation factor
sigma=10;    %Surface tension
D=200;       %Combustion chamber diameter                                               [in]
St=100;       
B=190;
W_eL=100;
psi=100;
z1=100;
r_i=100;
theta=100;
h_totNe=100;
Pr_w=100;    %Prandtl number
h_e=100;
h_c=100;
H_aw=100;
H_candsv=100;
c_pv=100;
T_totande=100;
c_pe=100;
%Eta=100;    %film cooling effectiveness
%ratio between the total and static core flow enthalpy difference and the  % 
%difference between the static enthalpy of the coolant saturated vapor and % 
%the static enthalpy of the coolant.                                       %
a=10;        %heat transfer augmentation factor for liquid surface roughness
R=100;       %universal gas constant
a1=-4.22*10^5;
a2=-5.58*10^3;
a3=1.52*10^2;
a4=-8.61*10^-1;
a5=3.07*10^-3;
a6=-4.70*10^-6;
a7=2.74*10^-9;

%-------------------------------Subequations-----------------------------------------------%
%First subequation- Calculating liquid entrainment correlation parameter
X_e=(delta*((rho_e/g)^0.5)*u_e*((T_e/T_if)^0.25))/sigma
%Second subequation- Calculating vaporization rate of the liquid surface

%--------------------------------Equation--------------------------------------------------%
%First step- Calculating L- liquid film cooled length)
%This length is defined as the distance beyond which the film ceases to
%exists.
L=(1/A)*log(1+(A*W_c)/V)
%Second step- Calculating film cooling effectivenes
Part1=(W_e/W_c)
Part2=(1-(W_eL/(W-W_c)))^0.5
Part3=(psi*z1/r_i)^2
eta=1/(theta*(1+(Part1)*(Part2)-(Part3)))
%Third step- Calculating adiabatic wall enthalpy
h_aw=h_totNe-eta*(h_totNe-h_c)-(1-(Pr_w)^(0.333))*(h_totNe-h_e)
%Forth step- Calculating specific heat of the vapor
c_pv=(R)((a1*T_c^-2)+(a2*T_c^-1)+a3+a4*T_c+(a5*T_c^2)+(a6*T_c^3)+(a7*T_c^4))
%Final step- Calculating adiabatic wall temperature
PartA=H_aw-eta*H_candsv+eta*c_pv*T_if+(1-eta)*((c_pv*T_totande)-h_e)
PartB=eta*c_pv+(1-eta)*c_pe
T_aw=(PartA/PartB)
