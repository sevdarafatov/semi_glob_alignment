#Sevda Rafatov
#CENG465 Assignment1

#Dynamic program for semi-global alignment
#I have used first 250000 nucleotides of short read sequence

import sys
def align():
                print ("Enter the short read sequence. Enter ctrl+d at the end")
                a=sys.stdin.read()
                a=a.replace("\n","")
                print ("Enter the refence sequence. Enter ctrl+d at the end")
                b=sys.stdin.read()
                b=b.replace("\n","")
                al=len(a)
                print ("length of the first sequence is: ",al)
                bl=len(b)
                print ("length of second sequence is: ",bl)
                m=[[0 for i in range((al+5)*2)] for j in range((bl+5)*2)]
                m[0][0]=0
                d='DiG'
                u='UpP'
                s='SiD'
                ds='D&S'
                du='D&U'
                su='S&U'
                dsu='ALL'
                f=0
                a1='A'
                na="\t"
                nb=[["" for i in range((al+5)*2)] for j in range((bl+5)*2)]
                t=[["" for i in range((al+5)*2)] for j in range((bl+5)*2)]
                tab="\t"
                ma=int(input("Enter the score for match"))
                mm=int(input("Enter the score for mismatch"))
                gp=int(input("Enter the score for linear gap penalty"))
                sc=[0,0,0]
                c=0
                m[1][1]=0
                t[1][1]="   "
                f=0
                for i in range(2,al+2):
                        f=f-gp
                        m[i][1]=f
                        t[i][1]=t[i][1]+s
                        na=na+a[i-2]+"\t"+"\t"
                f=0
                for j in range(2,bl+2):
                        f=f-gp
                        m[1][j]=f
                        t[1][j]=t[1][j]+u
                        nb[0][j-1]=nb[0][j-1]+b[j-2]
                for j in range(bl):
                    for i in range(al):
                        if(b[j]==a[i]):
                            #print "this are the caharacter mismatch",b[j],a[i]
                            sc[0]=ma+m[i+2-1][j+2-1]
                            #print "cell",m[i+2-1][j+2-1]
                            #sc[1]=m[i+2-1][j+2]-gp
                            #print "cell",m[i+2-1][j+2]
                            #sc[2]=m[i+2][j+2-1]-gp
                            #print "cell",m[i+2][j+2-1]
                            #sc[2]=c+m[i+2-1][j+2]
                            #print "cell",m[i+2-1][j+2]
                            #sc[2]=c+m[i+2][j+2-1]
                            #print "cell",m[i+2][j+2-1]
                            #print "this are the score for match",sc
                        else:
                            #print "this are the caharacter mismatch",b[j],a[i]
                            #sc[0]=c+m[i+2-1][j+2-1]
                            #print "cell",m[i+2-1][j+2-1]
                            sc[0]=m[i+2-1][j+2-1]-mm
                            #print "cell",m[i+2-1][j+2-1]
                        sc[1]=m[i+2-1][j+2]-gp
                        #print "cell",m[i+2-1][j+2]
                        sc[2]=m[i+2][j+2-1]-gp
                        #print "cell",m[i+2][j+2-1]
                        #print "this are the score for match",sc
                        #print max(sc)
                        m[i+2][j+2]=max(sc)
                        if(m[i+2][j+2]==sc[0] and m[i+2][j+2]==sc[1] and m[i+2][j+2]==sc[2]):
                            t[i+2][j+2]=t[i+2][j+2]+dsu
                        elif(m[i+2][j+2]==sc[0] and m[i+2][j+2]==sc[1]):
                            t[i+2][j+2]=t[i+2][j+2]+ds
                        elif(m[i+2][j+2]==sc[0] and m[i+2][j+2]==sc[2]):
                            t[i+2][j+2]=t[i+2][j+2]+du
                        elif(m[i+2][j+2]==sc[1] and m[i+2][j+2]==sc[2]):
                            t[i+2][j+2]=t[i+2][j+2]+su
                        elif(m[i+2][j+2]==sc[1]):
                            t[i+2][j+2]=t[i+2][j+2]+s
                        elif(m[i+2][j+2]==sc[2]):
                            t[i+2][j+2]=t[i+2][j+2]+u
                        else:
                            t[i+2][j+2]=t[i+2][j+2]+d
                #print ("After applying scores the matrix is")
                #print ("###################################")
                #print ("Short form of tracing cell")
                #print ("A=SCORE COME FROM ALL THREE CELL")
                #print ("D=SCORE COME FROM DIAGONAL CELL")
                #print ("S=SCORE COME FROM LEFT CELL")
                #print ("U=SCORE COME FROM UPPER CELL")
                #print ("DS=SCORE COME FROM DIAGONAL AND SIDE CELL")
                #print ("DU=SCORE COME FROM DIAGONAL AND UPPER CELL")
                #print ("SU=SCORE COME FROM SIDE AND UPPER CELL")
                            

                #print( "\t",na)
                #l=1
                #for j in range(1,bl+2):
                    #for i in range(1,al+2):print nb[i-1][j-1],'%2d'%m[i][j],t[i][j],"\t",
                    #print "\n"
                a1=""
                b1=""
                mid=""
                i=al
                j=bl
                iden=0
                mism=0
                while(i>0 and j>0):
                    #print "This is the value where tracing start",t[i+1][j+1],m[i+1][j+1]
                    if(t[i+1][j+1]==dsu or t[i+1][j+1]==du or t[i+1][j+1]==ds or t[i+1][j+1]==d):
                        if(a[i-1]==b[j-1]):
                            a1=a1+a[i-1]
                            #print "this is value of a1",a1
                            b1=b1+b[j-1]
                            #print "This is value of b1",b1
                            mid=mid+'|'
                            #print "This is value of mid",mid
                            i=i-1
                            #print "This is value of i",i
                            j=j-1
                            #print "This is value of j",j
                            iden=iden+1
                        else:
                            a1=a1+a[i-1]
                            #print "this is value of a1",a1
                            b1=b1+b[j-1]
                            #print "This is value of b1",b1
                            mid=mid+' '
                            #print "This is value of mid",mid
                            i=i-1
                            #print "This is value of i",i
                            j=j-1
                            #print "This is value of j",j
                            mism=mism+1
                    elif(t[i+1][j+1]==s or t[i+1][j+1]==su):
                        a1=a1+a[i-1]
                        #print "this is value of a1",a1
                        mid=mid+" "
                        #print "This is value of mid",mid
                        b1=b1+"-"
                        #print "This is value of b1",b1
                        i=i-1
                        #print "This is value of i",i
                        #print "This is value of j",j
                    else:
                        a1=a1+"-"
                        #print "this is value of a1",a1
                        mid=mid+" "
                        #print "This is value of mid",mid
                        b1=b1+b[j-1]
                        #print "This is value of b1",b1
                        #print "This is the value of i",i
                        j=j-1
                        #print "This is value of j",j
                print ("The semi-global alignment is")
                a1=a1[::-1]
                b1=b1[::-1]
                mid=mid[::-1]
                k=0
                x,y=divmod(len(mid),80)
                print ("Score is :",m[al+1][bl+1])
                while(x!=0):
                        i=0
                        for i in range(80):print (a1[i+k],end=" ")
                        print ('\n')
                        for i in range(80):print (mid[i+k],end=" ")
                        print ("\n")
                        for i in range(80):print (b1[i+k],end=" ")
                        print ("\n")
                        k=k+80
                        #print ("\n")
                        print("_______________________________________________________________________________________________________________________________________________________\n")
                        x=x-1
                for i in range(y):print (a1[i+(x*80)],end=" ")
                print ("\n")
                for i in range(y):print (mid[i+(x*80)],end=" ")
                print ("\n")
                for i in range (y):print (b1[i+(x*80)],end=" ")
                print ("\n")
                print("______________________________________________________________________________________________________________________________________________\n")
           
                    
