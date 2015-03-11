% This is the function to compute loss function in 
% gradient descent algorithm

function J = cost_f(X,y,theta)
	training    = length(y); % No of training samples
	prediction = X*theta;
	sq_err      = (prediction - transpose(y)).^2;
	J = (1/(2*training)) * nansum(sq_err);
end