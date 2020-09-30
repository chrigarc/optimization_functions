x=[-5:.1:5];y=[-5:.1:5];
[X,Y]=meshgrid(x,y);
Z = (X.^2 - 10*cos(2*pi*X) + 10) + (Y.^2 - 10*cos(2*pi*Y) + 10);
surf(Z);
