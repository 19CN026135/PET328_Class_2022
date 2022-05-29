no_dolo=float(input('Enter number of dolomite cores:'))
no_shale=float(input('Enter number of shale cores:'))
Ts= no_dolo+no_shale  #this is to calculate total amount of cores
P_D=no_dolo/Ts
P_S=no_shale/Ts

import scipy.stats

loc_D=float(input('Enter the mean of dolomite:'))
loc_S=float(input('Enter the mean of shale:'))
scale_D=float(input('Enter the standard deviation of dolomite:'))
scale_S=float(input('Enter the standard deviation of shale:'))
Ps_D=1-scipy.stats.norm(loc_D,scale_D).cdf(60)
Ps_S=1-scipy.stats.norm(loc_S,scale_S).cdf(60)

Pg_D=((P_D*Ps_D)/((P_D*Ps_D)+(P_S*Ps_S)))
if Pg_D>=0.5:
	print('The interval is dolomite')

else:
	print('The interval is shale')
	
	