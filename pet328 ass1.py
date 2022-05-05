import scipy.stats

dolM=float(input('Input mean of dolomite'))
shaM=float(input('Input mean of shale'))
dolS=float(input('Input standard deviation of dolomite'))
shaS=float(input('Input the standard deviation of shale'))
dolC=float(input('Input the count of dolomite'))
shaC=float(input('Input the count of shale'))


TC=dolC+shaC
pd=dolC/TC
pgd=1-scipy.stats.norm(loc=dolM, scale=dolS).cdf(60)
ps=shaC/TC
pgs=1-scipy.stats.norm(loc=shaM, scale=shaS).cdf(60)

pd_gamma=(pd*pgd)/( (pd*pgd)+(ps*pgs) )

if pd_gamma>=0.5:
    print('Dolomite interval')
else:
    print('Shale interval')
