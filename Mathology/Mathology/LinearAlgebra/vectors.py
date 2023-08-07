import re
from Mathology.Trigonometry.trigonometry import Trig

class Vectors(Trig):
    
    def __init__(self):
        pass

    def coordinatesToVector(self,x=0,y=0,z=0):
        return ('{}î + {}ĵ + {}k̂'.format(x,y,z))
    
    def magnitude(self,inputvector="0i+0j+0k"):
        final=re.split(r'\+|-',self.scaleVector(inputvector))
        magnitude=0
        for i in final:
            magnitude+=(eval(i[:len(i)-1]))**2
        return magnitude**0.5
    
    def scaleVector(self,inputvector="0i+0j+0k",constant=1):
        inputvector.replace(" ","")
        v=""
        for i in inputvector:
            if i in ("+","-"):
                v+=" "+i+" "
            else:
                v+=i
        s=v.split(" ")
        final=[]
        i=1
        while i<len(s)+1:
            if s[i-1]=="-":
                final.append(s[i-1] + s[i])
                i += 1
            else:
                final.append(s[i-1])
            i += 1
            
        for i in final[:]:
            if i in ("-+","+-","--","++","=","+","-",''):
                final.remove(i)
        
        result=""
        i_list=[]
        j_list=[]
        k_list=[]
       
        
        for i in range(len(final)):
            if len(final[i])==1:
                final[i]="1"+final[i]
            elif len(final[i])==2 and final[i][0]=="-" and final[i][1].isalpha():
                final[i]="-"+"1"+final[i][1]
            final[i]=final[i][:len(final[i])-1].replace(final[i][:len(final[i])-1],str(constant*eval(final[i][:len(final[i])-1])))+final[i][-1]
            if final[i][-1]=="i":
                if final[i][0]=="-" and final[i][1].isalpha():
                    i_list.append(-1)
                elif final[i][0].isalpha():
                    i_list.append(1)
                else:
                    i_list.append(eval(final[i][:len(final[i])-1]))
            elif final[i][-1]=="j":
                if final[i][0]=="-" and final[i][1].isalpha():
                    j_list.append(-1)
                elif final[i][0].isalpha():
                    j_list.append(1)
                else:
                    j_list.append(eval(final[i][:len(final[i])-1]))
            elif final[i][-1]=="k":
                if final[i][0]=="-" and final[i][1].isalpha():
                    k_list.append(-1)
                elif final[i][0].isalpha():
                    k_list.append(1)
                else:
                    k_list.append(eval(final[i][:len(final[i])-1]))

        i_list_sum=sum(i_list)
        j_list_sum=sum(j_list)
        k_list_sum=sum(k_list)

        final.clear()
        final.append(str(i_list_sum)+"i")
        final.append(str(j_list_sum)+"j")
        final.append(str(k_list_sum)+"k")

        if len(final)==1:
            result+=final[0]
            return result

        for i in range(1,len(final)):
            if i!=len(final)-1:
                if final[i-1][0]=="-" and final[i][0]=="-":
                    result+=final[i-1]+final[i]
                elif final[i-1][0]=="-" and final[i][0].isdigit():
                    result+=final[i-1]+"+"+final[i]
                elif final[i-1][0].isdigit() and final[i][0].isdigit():
                    result+=final[i-1]+"+"+final[i]
                elif final[i-1][0].isdigit() and final[i][0]=="-":
                    result+=final[i-1]+final[i]
            else:
                if len(final)==2:
                    if final[i-1][0]=="-" and final[i][0]=="-":
                        result+=final[i-1]+final[i]
                    elif final[i-1][0]=="-" and final[i][0].isdigit():
                        result+=final[i-1]+"+"+final[i]
                    elif final[i-1][0].isdigit() and final[i][0].isdigit():
                        result+=final[i-1]+"+"+final[i]
                    elif final[i-1][0].isdigit() and final[i][0]=="-":
                        result+=final[i-1]+final[i]
    
                else:
                    if final[i][0]=="-":
                        result+=final[i]
                    else:
                        result+="+"+final[i]
        return result

    def addition(self,*vectors):
        if type(vectors[0])==tuple or type(vectors[0])==list:
            k=[]
            for i in vectors:
                for j in i:
                    k.append(j)
            vectors=k.copy()
        
        if len(vectors)>1:
            vector_string=""
            result_vectors=[]
            result_i=[]
            result_j=[]
            result_k=[]
            for vector in vectors:
                vector.replace(" ","")
                v=""
                for i in vector:
                    if i in ("+","-"):
                        v+=" "+i+" "
                    else:
                        v+=i
                s=v.split(" ")
                final=[]
                i=1
                while i<len(s)+1:
                    if s[i-1]=="-":
                        final.append(s[i-1] + s[i])
                        i += 1
                    else:
                        final.append(s[i-1])
                    i += 1
                    
                for i in final[:]:
                    if i in ("-+","+-","--","++","=","+","-",''):
                        final.remove(i)
        
                i_list=[]
                j_list=[]
                k_list=[]
                

                for i in range(len(final)):
                    if len(final[i])==1:
                        final[i]="1"+final[i]

                    elif len(final[i])==2 and final[i][0]=="-" and final[i][1].isalpha():
                        final[i]="-"+"1"+final[i][1]

                    if final[i][-1]=="i":
                        if final[i][0]=="-" and final[i][1].isalpha():
                            i_list.append(-1)
                        elif final[i][0].isalpha():
                            i_list.append(1)
                        else:
                            i_list.append(eval(final[i][:len(final[i])-1]))

                    elif final[i][-1]=="j":
                        if final[i][0]=="-" and final[i][1].isalpha():
                            j_list.append(-1)
                        elif final[i][0].isalpha():
                            j_list.append(1)
                        else:
                            j_list.append(eval(final[i][:len(final[i])-1]))

                    elif final[i][-1]=="k":
                        if final[i][0]=="-" and final[i][1].isalpha():
                            k_list.append(-1)
                        elif final[i][0].isalpha():
                            k_list.append(1)
                        else:
                            k_list.append(eval(final[i][:len(final[i])-1]))
                
                    

                i_list_sum=sum(i_list)
                j_list_sum=sum(j_list)
                k_list_sum=sum(k_list)
                
                final.clear()
                final.append(str(i_list_sum)+"i")
                final.append(str(j_list_sum)+"j")
                final.append(str(k_list_sum)+"k")


                final_vector=""

                for i in range(1,len(final)):
                    if i!=len(final)-1:
                        if final[i-1][0]=="-" and final[i][0]=="-":
                            final_vector+=final[i-1]+final[i]
                        elif final[i-1][0]=="-" and final[i][0].isdigit():
                            final_vector+=final[i-1]+"+"+final[i]
                        elif final[i-1][0].isdigit() and final[i][0].isdigit():
                            final_vector+=final[i-1]+"+"+final[i]
                        elif final[i-1][0].isdigit() and final[i][0]=="-":
                            final_vector+=final[i-1]+final[i]
                    else:
                        if len(final)==2:
                            if final[i-1][0]=="-" and final[i][0]=="-":
                                final_vector+=final[i-1]+final[i]
                            elif final[i-1][0]=="-" and final[i][0].isdigit():
                                final_vector+=final[i-1]+"+"+final[i]
                            elif final[i-1][0].isdigit() and final[i][0].isdigit():
                                final_vector+=final[i-1]+"+"+final[i]
                            elif final[i-1][0].isdigit() and final[i][0]=="-":
                                final_vector+=final[i-1]+final[i]
            
                        else:
                            if final[i][0]=="-":
                                final_vector+=final[i]
                            else:
                                final_vector+="+"+final[i]
                
              
                result_vectors.append(final_vector)
                
            
            if len(result_vectors)==2:
                vector_string+=result_vectors[0]
                if result_vectors[1][0]!="-":
                    vector_string+="+"
                vector_string+=result_vectors[1]

            else:
                for vector in range(1,len(result_vectors)):
                    
                    for component in result_vectors[vector-1]:
                        vector_string+=component

                    if result_vectors[vector][0]!="-":
                        vector_string+="+"
                vector_string+=result_vectors[vector]


            
            
            vector_string.replace(" ","")
            v=""
            for i in vector_string:
                if i in ("+","-"):
                    v+=" "+i+" "
                else:
                    v+=i
            s=v.split(" ")
            final=[]
            i=1
            
            while i<len(s)+1:
                if s[i-1]=="-":
                    final.append(s[i-1] + s[i])
                    i += 1
                else:
                    final.append(s[i-1])
                i += 1
           
                
            for i in final[:]:
                if i in ("-+","+-","--","++","=","+","-",''):
                    final.remove(i)

    
            for i in range(len(final)):
                if len(final[i])==1:
                    final[i]="1"+final[i]

                elif len(final[i])==2 and final[i][0]=="-" and final[i][1].isalpha():
                    final[i]="-"+"1"+final[i][1]

                if final[i][-1]=="i":
                    if final[i][0]=="-" and final[i][1].isalpha():
                        result_i.append(-1)
                    elif final[i][0].isalpha():
                        result_i.append(1)
                    else:
                        result_i.append(eval(final[i][:len(final[i])-1]))

                elif final[i][-1]=="j":
                    if final[i][0]=="-" and final[i][1].isalpha():
                        result_j.append(-1)
                    elif final[i][0].isalpha():
                        result_j.append(1)
                    else:
                        result_j.append(eval(final[i][:len(final[i])-1]))

                elif final[i][-1]=="k":
                    if final[i][0]=="-" and final[i][1].isalpha():
                        result_k.append(-1)
                    elif final[i][0].isalpha():
                        result_k.append(1)
                    else:
                        result_k.append(eval(final[i][:len(final[i])-1]))

            
          

            result_i_sum=sum(result_i)
            result_j_sum=sum(result_j)
            result_k_sum=sum(result_k)
           

            final.clear()
            final.append(str(result_i_sum)+"i")
            final.append(str(result_j_sum)+"j")
            final.append(str(result_k_sum)+"k")
            

            result=""

            for i in range(len(final)):
                if i!=0:
                    if final[i][0]=="-":
                        result+=final[i]
                    else:
                        result+="+"+final[i]
                else:
                    result+=final[i]

            return result
                
        else:
            vector=vectors[0]
            vector.replace(" ","")
            v=""
            for i in vector:
                if i in ("+","-"):
                    v+=" "+i+" "
                else:
                    v+=i
            s=v.split(" ")
            final=[]
            i=1
            while i<len(s)+1:
                if s[i-1]=="-":
                    final.append(s[i-1] + s[i])
                    i += 1
                else:
                    final.append(s[i-1])
                i += 1
                
            for i in final[:]:
                if i in ("-+","+-","--","++","=","+","-",''):
                    final.remove(i)
    
            i_list=[]
            j_list=[]
            k_list=[]
            

            for i in range(len(final)):
                if len(final[i])==1:
                    final[i]="1"+final[i]

                elif len(final[i])==2 and final[i][0]=="-" and final[i][1].isalpha():
                    final[i]="-"+"1"+final[i][1]

                if final[i][-1]=="i":
                    if final[i][0]=="-" and final[i][1].isalpha():
                        i_list.append(-1)
                    elif final[i][0].isalpha():
                        i_list.append(1)
                    else:
                        i_list.append(eval(final[i][:len(final[i])-1]))

                elif final[i][-1]=="j":
                    if final[i][0]=="-" and final[i][1].isalpha():
                        j_list.append(-1)
                    elif final[i][0].isalpha():
                        j_list.append(1)
                    else:
                        j_list.append(eval(final[i][:len(final[i])-1]))

                elif final[i][-1]=="k":
                    if final[i][0]=="-" and final[i][1].isalpha():
                        k_list.append(-1)
                    elif final[i][0].isalpha():
                        k_list.append(1)
                    else:
                        k_list.append(eval(final[i][:len(final[i])-1]))
            
                

            i_list_sum=sum(i_list)
            j_list_sum=sum(j_list)
            k_list_sum=sum(k_list)
            
            final.clear()
            final.append(str(i_list_sum)+"i")
            final.append(str(j_list_sum)+"j")
            final.append(str(k_list_sum)+"k")

            final_vector=""

            for i in range(1,len(final)):
                if i!=len(final)-1:
                    if final[i-1][0]=="-" and final[i][0]=="-":
                        final_vector+=final[i-1]+final[i]
                    elif final[i-1][0]=="-" and final[i][0].isdigit():
                        final_vector+=final[i-1]+"+"+final[i]
                    elif final[i-1][0].isdigit() and final[i][0].isdigit():
                        final_vector+=final[i-1]+"+"+final[i]
                    elif final[i-1][0].isdigit() and final[i][0]=="-":
                        final_vector+=final[i-1]+final[i]
                else:
                    if len(final)==2:
                        if final[i-1][0]=="-" and final[i][0]=="-":
                            final_vector+=final[i-1]+final[i]
                        elif final[i-1][0]=="-" and final[i][0].isdigit():
                            final_vector+=final[i-1]+"+"+final[i]
                        elif final[i-1][0].isdigit() and final[i][0].isdigit():
                            final_vector+=final[i-1]+"+"+final[i]
                        elif final[i-1][0].isdigit() and final[i][0]=="-":
                            final_vector+=final[i-1]+final[i]
        
                    else:
                        if final[i][0]=="-":
                            final_vector+=final[i]
                        else:
                            final_vector+="+"+final[i]
        return final_vector
    
    def subtraction(self,*vectors):
        if type(vectors[0])==tuple or type(vectors[0])==list:
            k=[]
            for i in vectors:
                for j in i:
                    k.append(j)
            vectors=k.copy()
        topass=[]
        for i in range(len(vectors)):
            if i==0:
                topass.append(vectors[i])
            else:
                topass.append(self.scaleVector(vectors[i],-1))
       
        return self.addition(topass)
    
    def scalarProduct(self,vector1="0i+0j+0k",vector2="0i+0j+0k"):  
        vector1 = self.addition(vector1)
        vector2 = self.addition(vector2)

        i_list=[]
        j_list=[]
        k_list=[]
        
        i_index_1 = vector1.index('i')
        j_index_1 = vector1.index('j')
        k_index_1 = vector1.index('k')
        i_list.append(eval(vector1[:i_index_1]))
        j_list.append(eval(vector1[i_index_1+1:j_index_1]))
        k_list.append(eval(vector1[j_index_1+1:k_index_1]))

        i_index_2 = vector2.index('i')
        j_index_2 = vector2.index('j')
        k_index_2 = vector2.index('k')
        i_list.append(eval(vector2[:i_index_2]))
        j_list.append(eval(vector2[i_index_2+1:j_index_2]))
        k_list.append(eval(vector2[j_index_2+1:k_index_2]))                
        
        i_list_product=1
        j_list_product=1
        k_list_product=1

        for i in i_list:
            i_list_product *= i

        for j in j_list:
            j_list_product *= j
        
        for k in k_list:
            k_list_product *= k
        
        result = i_list_product + j_list_product + k_list_product
        return result

    def angleBwVectors(self,vector1="0i+0j+0k",vector2="0i+0j+0k"):
        if self.magnitude(vector1)==0.0 or self.magnitude(vector2)==0.0:
            print("Error: Angle between vectors is not defined as either or both vectors have magnitude zero!")
            return "\033[F"
        return str(self.radiansToDegrees(self.arccos(self.scalarProduct(vector1,vector2)/(self.magnitude(vector1) * self.magnitude(vector2))))) + "°"

    def projectVectors(self,vector1="0i+0j+0k",vector2="0i+0j+0k"):
        """
        Projects Vector 1 onto Vector 2
        """
        if self.magnitude(vector1)==0.0 or self.magnitude(vector2)==0.0:
            print("Error: Projection is not defined as either or both vectors have magnitude zero!")
            return "\033[F"
        return self.scalarProduct(vector1,vector1)/self.magnitude(vector2)