import strength
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig=plt.figure()

ax=fig.add_subplot(1,1,1)
ys=[]
xs=[]

def animate(f,xs,ys):
    stren = -(strength.get_wifi_signal_strength())
    xs.append(datetime.datetime.now().strftime('%M:%S'))
    ys.append(stren)
    
    plt.cla()
    ax.plot(xs,ys)    
    
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    
    plt.title('wifi strength over Time')
    plt.ylabel('strength less negative is better')
    plt.xlabel('time')
ani=animation.FuncAnimation(fig,animate,fargs=(xs,ys),interval=1000,blit=True)
plt.tight_layout()

plt.show()