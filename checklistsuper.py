from easygui import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
filename=eval(input("file name: "))+'.txt'
f=open(filename, 'r')
array=f.readlines()
c=68
err={}
firster=0
line_n=2
#flow_ex=internal=no_flow=port_de=rst_from=tcp_3whs=tcp_rst=handshake=0
while firster<70:
    if array[firster][0:10]=='RST Cause:':
        while array[firster+line_n]!='\n':
            err[array[firster+line_n][0:35]]=int(array[firster+line_n][35:len(array[firster+line_n])-1])
            line_n=line_n+1
    firster=firster+1

err_list=list(err.keys()) #puts all the dicts into a list

for x in range(0,len(err_list)): #makes a string for each item in the list  
    temp=err_list[x]             #using the second to last word without first letter and add _ to end
    sec_to_last =temp.split()[len(temp.split())-2]
    exec(sec_to_last[1:len(sec_to_last)]+'_=[]') 
y_counter=0
while c<len(array):
    if array[c][0:10]=='RST Cause:':
        line_n=2
        y_counter=y_counter+1
        #print(y_counter)
        while array[c+line_n]!='\n':
            temp=array[c+line_n][0:35]
            sec_to_last =temp.split()[len(temp.split())-2]
            
            eval(sec_to_last[1:len(sec_to_last)]+'_').append(str(abs(err[array[c+line_n][0:35]]-int(array[c+line_n][35:len(array[c+line_n])-1]))))
            err[array[c+line_n][0:35]]=int(array[c+line_n][35:len(array[c+line_n])-1])
            line_n=line_n+1
    c=c+1

var = multchoicebox ('message', 'title',err_list) #var is the chosen one(s)

#hdqadprdz2lb03_stats_output_5min test

#print(var)
#y_counter=range(0,y_counter)
plt.autoscale(enable=True, axis='both', tight=None)
#plt.yscale('linear')
#plt.plot(y_counter, ropped_, linewidth=.5)

#plt.xaxis.set_ticks(np.arange(start, end, 10))
legends=[]
for x in range(0,len(var)):
    temp=var[x].split()[len(var[x].split())-2]+'_'
    temp=temp[1:len(temp)]
    #print(len(eval(temp)))
    #len_x=range(0,len(eval(temp)))
    #plt.plot(len_x,eval(temp), linewidth=1.0)
    #print(len(eval(temp)))
    plt.plot(eval(temp), linewidth=.75)
    p=plt.plot(eval(temp), linewidth=.75)
    type(p) 
    type(p[0])
    patch = mpatches.Patch(color=p[0].get_color(), label=var[x])
    legends.append(patch)
    #plt.legend(handles=[patch])
plt.legend(handles=legends)


plt.show()
