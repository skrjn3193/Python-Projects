from tkinter import *
tk=Tk()
tk.title("EVM")
tk.geometry("500x500")

b,c,a,s=[],[],[],[]
def BJP():
    v=0
    v+=1
    b.append(v)
def CONGRESS():
    v=0
    v+=1
    c.append(v)
def AAP():
    v=0
    v+=1
    a.append(v)
def SP():
    v=0
    v+=1
    s.append(v)


def Result():
    bjp_vote=len(b)
    congress_vote=len(c)
    aap_vote=len(a)
    sp_vote=len(s)

    total_vote=bjp_vote+congress_vote+aap_vote+sp_vote

    bjp_result=bjp_vote/total_vote*100
    congress_result=congress_vote/total_vote*100
    aap_result=aap_vote/total_vote*100
    sp_result=sp_vote/total_vote*100
    
    lbl5=Label(tk,text=round(bjp_result,2),font="Helvetica 20 bold italic").grid(row=1,column=5)
    lbl6=Label(tk,text=round(congress_result,2),font="Helvetica 20 bold italic").grid(row=2,column=5)
    lbl7=Label(tk,text=round(aap_result,2),font="Helvetica 20 bold italic").grid(row=3,column=5)
    lbl8=Label(tk,text=round(sp_result,2),font="Helvetica 20 bold italic").grid(row=4,column=5)
    

lbl1=Label(tk,text="BJP",font="Helvetica 20 bold italic").grid(row=1,column=1)
lbl2=Label(tk,text="CONGRESS",font="Helvetica 20 bold italic").grid(row=2,column=1)
lbl3=Label(tk,text="AAP",font="Helvetica 20 bold italic").grid(row=3,column=1)
lbl4=Label(tk,text="SP",font="Helvetica 20 bold italic").grid(row=4,column=1)
#lbl1.grid(row=1,column=1)

btn1=Button(tk,text="Vote",command=BJP).grid(row=1,column=3)
btn2=Button(tk,text="Vote",command=CONGRESS).grid(row=2,column=3)
btn3=Button(tk,text="Vote",command=AAP).grid(row=3,column=3)
btn4=Button(tk,text="Vote",command=SP).grid(row=4,column=3)

btn5=Button(tk,text="Result",command=Result).grid(row=4,column=7)

                                            
