% This is implimentation of the simple Solow growth model as presented in the classroom

% declare simulation horizon

time = 300;

% declare parameter values

alpha = 0.5;  % production function parameter
n     = 0.05;  % population growth
s     = 0.65; % savings rate
d     = 0.04; % depreciation rate
z     = 1;    % productivity

% initial values of variables

Y(1) = 100;              % capital
I(1) = s*Y(1);           % investment
N(1) = 100;              % population
K(1) = I(1) + (1-d)*10; % capital



% model

for t = 1:time

	Y(:,t) = z * ((K(t)^alpha) * N(t)^(1-alpha)); % production function

	N(:,t+1) = (1+n)*N(t);                        % population growth

	I(:,t) = s*Y(t);                              % investment (investment = savings)

	K(:,t+1) = I(t) + (1-d)*K(t);				  % capital

	y(:,t) = Y(t) / N(t);                         % production per capita

	i(:,t) = I(t) / N(t);                         % investment (savings) per capita

	k(:,t) = K(t) / N(t);                         % capital per capita

	breake(:,t) = (d+n)*k(t);                     % break-even investment

	c(:,t) = (1-s)*k(t);                          % consumption per capita

	invest(:,t) = s*y(t);                         % investment

end



figure
plot(y,'k')
hold
plot(c,'r')
xlabel('Time')
ylabel('Y / N')
title('Production and Consumption per Capita')
hleg = legend('Y/N', 'C/N');

figure
plot(k,'k')
hold
plot(((invest-breake)./k).*100,'r')
hleg = legend('Capital per Worker', 'Growth Rate (Magnified x100)');
xlabel('Time')
ylabel('Value')
title('Capital per Worker & Growth Rate')

figure
plot(i,'k')
xlabel('Time')
ylabel('I / N')
title('Investment per Capita')

figure
plot(breake,'k')
hold
plot(invest)
xlabel('Time')
ylabel('Values')
title('Investment per Capita')
hleg = legend('(d+n)k', 'sy(k,1)');

figure
plot(k,breake,'r')
hold
plot(invest)
xlabel('k')
ylabel('i')
title('Capital & Investment')
hleg = legend('(d+n)k','sy(k,1)');
