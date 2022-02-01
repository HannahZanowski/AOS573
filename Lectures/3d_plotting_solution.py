#Surface example
#Set up the data
x=np.arange(-10.1,10.1,0.5)
y=x

x,y=np.meshgrid(x,y)
z=x*y*(x**2-y**2)/(x**2+y**2)

#set up axis
fig,ax=plt.subplots(subplot_kw={'projection':'3d'},figsize=(6,6))

#make the surface plot
ax.plot_surface(x, y, z,cmap=plt.cm.magma)

#add labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
