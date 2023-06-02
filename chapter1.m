
a11 = quaternion(1,0,0,0);
a12 = quaternion(0,1,0,0);
a21 = quaternion(0,0,1,0);
a22 = quaternion(0,0,0,1);

X1 = quaternion(1,1,1,0);
X2 = quaternion(0,1,1,1);

Y1 = quaternion(1,1,0,0); 
Y2 = quaternion(1,0,0,1);

a = quaternion(1,0,1,0);
b = quaternion(1,1,0,0);

% expression 1 (Left)

top1 = a * X1 + b * Y1;
bottom1 = a * X2 + b * Y2; 
a11 * top1 + a12 * bottom1
a21 * top1 + a22 * bottom1

% expression 2 (Right)
a * (a11 * X1 + a12 * X2) + b * (a11 * Y1 + a12 * Y2)
a * (a21 * X1 + a22 * X2) + b * (a21 * Y1 + a22 * Y2)