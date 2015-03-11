
function [pol_coefs,serie] = fit_polyn(data,alpha_le,degree)

% =======================================================================
% Purpose of the function is to fit polynomial on the data using
% gradient descent algorithm
% Model: Y = theta1+theta2*X+theta3*X^3+...
% 
% =======================================================================
% out = polynomial coefficients
% -----------------------------------------------------------------------
% INPUT
%   matrix: Y (1 by n), data to
%   learning rate: alpha_le
%   degree: degree of polynomial
%
% OUTPUT
%   variable: pol_coefs -> polynomial coefficients
%   variable: serie -> serie computed using those coefficients
% =======================================================================
% Sarunas Girdenas, March 2015
% sg325@exeter.ac.uk


	size_data = size(data); % size of data

	coefs = zeros(degree+1,1); % container for coefficients

	polyn = zeros(degree+1,size_data(2));

	for i = 1:degree+1
		polyn(i,:) = data.^i;
	end

	% add intercept

	polyn(1,:)=ones(1,size_data(2));

	X = transpose(polyn);


	%gradient descent algorithm

	max_iter = 7000; % no of maximum iterations
	no_iter  = 0; % initialize
	Er       = 10e-20; % tolerance for error

	J_loss_hist = zeros(max_iter,1);    % empty array to store loss function values
	J_loss_new  = 0;                    % initialize loss function value
	J_loss      = cost_f(X,data,coefs); % initialize loss
	err         = zeros(length(coefs),size_data(2));
	coefs_hist  = zeros(max_iter,length(coefs)); 

	while abs(J_loss-J_loss_new) > Er

		no_iter = no_iter + 1;

		if no_iter == max_iter
			break
		end

		J_loss_hist(no_iter,1) = cost_f(X,data,coefs);

		J_loss = cost_f(X,data,coefs);

		predictions = X*coefs;

		for k = 1:length(coefs)
			err(k,:)   = (predictions - transpose(data)).*X(:,k);
			coefs(k,1) = coefs(k,1) - sum(alpha_le*(1/length(data))*err(k,:));
			coefs_hist(no_iter,k) = coefs(k,1);
		end

		J_loss_new = cost_f(X,data,coefs);
	end


	serie = X*coefs;
	pol_coefs = coefs;	

end
