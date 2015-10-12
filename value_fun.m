% this is value function iteration based on Ellison notes

beta = 1;

Q=zeros(1,1);
R=zeros(2,2);
A=zeros(2,2);
B=zeros(2,1);
Q(1,1)=0;
R(1,1)=1;
R(1,2)=0;
R(2,1)=0;
R(2,2)=1;
A(1,1)=1;
A(1,2)=0.1;
A(2,1)=0;
A(2,2)=0.5;
B(1,1)=0;
B(2,1)=-1;

d=1;
i=0;
P0=-0.000001*eye(2);

% store value function

Vals   = zeros(50,17);
Policy = zeros(50,17);

mat1 = linspace(0,1,50); % inflation
mat2 = linspace(1,1,50); % output

while d > 1e-10

	P1=R+beta*A'*P0*A-(beta*A'*P0*B)*(inv(Q+beta*B'*P0*B))*(beta*B'*P0*A);
	Pd=P1-P0;
	d=max(abs(Pd));
	d=max(d');
	P0=P1;

	i=i+1;

	% compute value function

	Vals(:,i) = P0(1,1)*(mat1.^2) + P0(2,2)*(mat2.^2) + 2*P0(1,2)*mat1*mat2';

	% compute policy

	F=-inv(Q+beta*B'*P0*B)*(beta*B'*P0*A);

	Policy(:,i) = F(1,1)*mat1 +F(1,2)*mat2;


end

P=P0;

F=-inv(Q+beta*B'*P*B)*(beta*B'*P*A);

% % create inflation and output

% plot value function

figure
plot(Vals)
xlabel('Inflation = Output')
ylabel('Value Function Values')

figure
plot(Policy)
xlabel('Inflation = Output')
ylabel('Policy')

% so now we can compute optimal policy for given parameters

time = 100;

%initial Values
infl = zeros(100,1);
y    = zeros(100,1);
r    = zeros(100,1);


infl(1,1) = 1;
y(1,1)    = 0;

for t = 2:time

	r(t-1) = F(1,1)*infl(t-1,1) + F(1,2)*y(t-1,1);

	infl(t,1) = infl(t-1,1) + 0.1*y(t-1,1);

	y(t,1) = 0.5*y(t-1,1) - r(t-1,1);

end

%plot stuff

figure
plot(infl)
xlabel('Time')
ylabel('Inflation')

figure
plot(y)
xlabel('Time')
ylabel('Output')

figure
plot(r)
xlabel('Time')
ylabel('Interest Rate')

