x=[-5:.1:5];y=[-5:.1:5];
[X,Y]=meshgrid(x,y);
Z=X.^2+Y.^2;
surf(Z);
