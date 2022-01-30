x = linspace(5,10,25);
t = linspace(0,10,50);
%t_prime = logspace(0.00001, 100, 8);
m = 1;
sol = pdepe(m,@heatcyl,@heatic,@heatbc,x,t);

u = sol(:,:,1);

figure(1) %test
surf(x,t,u)
xlabel('x')
ylabel('t')
zlabel('u(x,t)')
view([150 25])

figure(2)
plot(t,sol(:,1))
xlabel('Time')
ylabel('Temperature u(5,t)')
title('Temperature as a function of time at the inner hot wall')

abc = sol(:,1)
function [c,f,s] = heatcyl(x,t,u,dudx)
c = 1;
f = dudx;
s = 0;
end
%----------------------------------------------
function u0 = heatic(x)
 
u0 = 1;
end
%----------------------------------------------
function [pl,ql,pr,qr] = heatbc(xl,ul,xr,ur,t)
 
pl = -50*ul; 
ql = 1; 
pr = 0;
qr = 1; 
end