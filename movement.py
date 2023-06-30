# 合併動作在這裡處理
def merge(objects,selected_id,mode):
    selected_id[0],selected_id[1]=selected_id[1],selected_id[0]
    for t,i in enumerate(objects):
        if i.id==selected_id[0]:
            i.display=False
            a=i
        if i.id==selected_id[1]:
            i.display=False
            b=i
            pop_item=t
    if mode==1:
        cost=a.weight*b.weight
    elif mode==2:
        cost=a.weight+b.weight
    elif mode==3:
        cost=min([a.weight,b.weight])
    elif mode==4:
        cost=max([a.weight,b.weight])
    elif mode==5:
        cost=abs(a.weight-b.weight)
    a.weight+=b.weight
    a.display=True
    a.selected=False
    b.display=True
    b.selected=False
    objects.pop(pop_item)
    
    return cost