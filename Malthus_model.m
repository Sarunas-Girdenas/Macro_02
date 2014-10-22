% This is implimentation of the simple Malthusian growth model

% declare simulation horizon

time = 300;

% declare parameter values

alpha = 0.5;
gamma = 0.18;
z     = 1;
L     = 200;
N(1)  = 1; % initial value of population

% define shock to L

shock                      = zeros(time,1);
shock(time/3,1)            = 0;
shock(time/3:time*(2/3),1) = 200;
shock(time*(2/3):end,1)    = 0;


% model

for t = 1:time

	Y(:,t) = z * ((L + shock(t))^alpha) * N(t)^(1-alpha);

	N(:,t+1) = ((Y(t) / N(t))^gamma )* N(t);

	% marginal product of land

	MPL(:,t) = z * alpha * ((L+shock(t))^(alpha-1)) * N(t)^(1-alpha);

end

figure
plot(N,'k')
xlabel('Time');
ylabel('N (Number of Workers)')
title('Population Growth')

figure
plot(MPL,'k')
xlabel('Time')
ylabel('Marginal Product of Land')
title('Marginal Product of Land')



