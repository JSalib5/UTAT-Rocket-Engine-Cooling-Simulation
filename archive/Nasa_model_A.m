%NASA A - Analytical model for gaseous film cooling

%list of constants and unknowns
%All unknowns,constants are required to express in the american units system
%-------------------------------Constants---------------------------------%
W_e=100;     %Entrained flow rate                                       [lbm/s]              
W_c=100;     %Coolant flow rate                                         [lbm/s]
W=100;       %Total combustion chamber flow rate                        [lbm/s]
z=100;       %Effective contour distance [integral will be need]           [in]
r=100;       %Reference entrainment factor                                  [-]
s=100;       %Mixing layer length                                          [in]
u_e=100;     %Entrained velocity                                         [mi/h]
u_c=100;     %Coolant velocity                                           [mi/h]
rho_c=100;   %Density of coolant                                     [lbm/ft^3]                                                         
rho_e=100;   %Density of entrained                                   [lbm/ft^3]  
    

%-------------------------------Subequation--------------------------------%
%integral for Effective contour distance
%subequation for reference entrainment factor 
%function of entrained flow ratio
eta=eta(W_e/W_c)
%the above function can be approximated as:
eta_1=(1.32/(1+(W_e/W_c)))      %if (W_e/W_c)>1.4
eta_2=1                         %if (W_e/W_c)>0.06


%-------------------------------Entrained Ratio--------------------------------%
%Entrained_Ratio=(W_e/W_c)
Entrained_Ratio=((W-W_c)/W_c)-(((2*r*z)/(r-s))-((r*z)/(r-s))^2)



