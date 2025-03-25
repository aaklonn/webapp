import csv
with open ("okom.csv" , "r") as a :
    b=csv.reader(a)
    s=[]
    k=[]
    for i in b:
        if i[2]!="AI":
            s.append(i[0])
            s.append(i[1])
            s.append("HS")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        else:
            s.append(i[0])
            s.append(i[1])
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
with open("okom1.csv" , "w") as mai:
    ji=csv.writer(mai)
    ji.writerows(k)             


import csv
with open ("okom.csv" , "r") as a:
    b=csv.reader(a)
    s=[]
    for x in b:
       
        s.append(x[1])
        j=set(s)
        k=list(j)
        
    for y in sorted(k):
        print(y, end='\n')
   
'''
import csv

with open("iit.csv", "r") as file:
    reader = csv.reader(file)
    colleges = {}
    for row in reader:
        college_name = row[0]
        branch = row[1]
        if college_name not in colleges:
            colleges[college_name] = [branch]
        else:
            if branch not in colleges[college_name]:
                colleges[college_name].append(branch)

print(colleges)

import csv
with open("iit.csv" , "r") as a :
    b=csv.reader(a)
    quota=[]
    for x in b:
        quota.append(x[0])
    s=set(quota)
    print(s)

import csv
with open("iit.csv" , "r") as a:
    b=csv.reader(a)
    s=[]
    
    for i in b:
        s.append(i[0])
    o=set(s)
    for x in sorted(o):
        print("<option>"+x+"</option>")

import csv
with open ("josaa2024.csv" , "r") as a :
    b=csv.reader(a)
    s=[]
    k=[]
    for i in b:
        
        if i[0]=="Assam University Silchar" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Assam")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]

        elif i[0]=="Atal Bihari Vajpayee Indian Institute of Information Technology & Management Gwalior" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Madhya Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Birla Institute of Technology Deoghar Off-Campus" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Jharkhand")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Birla Institute of Technology Mesra Ranchi" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Jharkhand")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Birla Institute of Technology Patna Off-Campus" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Bihar")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Central University of Haryana" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Haryana")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Central University of Jammu" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Jammu and Kashmir")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Central University of RajasthanRajasthan" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Rajasthan")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Central institute of Technology KokrajarAssam" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Assam")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Chhattisgarh Swami Vivekanada Technical UniversityBhilai (CSVTU Bhilai)" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Chattisgarh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Dr. B R Ambedkar National Institute of Technology Jalandhar" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Punjab")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Ghani Khan Choudhary Institute of Engineering and Technology Malda West Bengal" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("West Bengal")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Gurukula Kangri Vishwavidyalaya Haridwar" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Uttarakhand")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Carpet Technology  Bhadohi" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Uttar Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Engineering Science and Technology Shibpur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("West Bengal")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Handloom Technology Salem" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Tamil Nadu")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Handloom Technology(IIHT)Varanasi" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Uttar Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology  Manipur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Manipur")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology (IIIT) Nagpur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Maharashtra")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology (IIIT) Pune" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Maharashtra")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology (IIIT) Ranchi" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Jharkhand")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology (IIIT)KotaRajasthan" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Rajasthan")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology (IIIT)Sri CityChittoor" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Andhra Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology Agartala" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Tripura")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology Allahabad" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Uttar Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology Bhagalpur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Bihar")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology Bhopal" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Madhya Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology Design & Manufacturing Kancheepuram" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Tamil Nadu")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology Design & Manufacturing Kurnool Andhra Pradesh" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Andhra Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology Guwahati" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Assam")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology Lucknow" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Uttar Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology Surat" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Gujarat")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology Tiruchirappalli" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Tamil Nadu")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]

        elif i[0]=="Indian Institute of Information Technology Vadodara International Campus Diu (IIITVICD)" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Daman and Dui")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology(IIIT) Dharwad" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Karnataka")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology(IIIT) KalyaniWest Bengal" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("West Bengal")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology(IIIT) KilohradSonepatHaryana" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Haryana")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology(IIIT) Kottayam" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Kerala")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology(IIIT) UnaHimachal Pradesh" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Himachal Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian Institute of Information Technology(IIIT)Vadodara Gujrat" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Gujarat")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Indian institute of information technology Raichur Karnataka" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Karnataka")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Institute of Chemical Technology Mumbai Indian Oil Odisha Campus Bhubaneswar" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Odisha")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Institute of Engineering and Technology Dr. H. S. Gour University. Sagar (A Central University)" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Madhya Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Institute of Infrastructure Technology Research and Management-Ahmedabad" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Gujarat")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Institute of Technology Guru Ghasidas Vishwavidyalaya (A Central University)Bilaspur(C.G.)" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Chattisgarh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="International Institute of Information Technology Bhubaneswar" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Odisha")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="International Institute of Information Technology Naya Raipur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Chattisgarh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="J.K. Institute of Applied Physics & Technology Department of Electronics & CommunicationUniversity of Allahabad- Allahabad"  and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Uttar Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Jawaharlal Nehru UniversityDelhi" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Delhi")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Malaviya National Institute of Technology Jaipur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Rajasthan")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Maulana Azad National Institute of Technology Bhopal" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Madhya Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Mizoram UniversityAizawl" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Mizoram")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Motilal Nehru National Institute of Technology Allahabad" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Uttar Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Advanced Manufacturing Technology Ranchi" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Jharkhand")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Electronics and Information Technology Aurangabad (Maharashtra)" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Maharashtra")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Food Technology Entrepreneurship and ManagementKundli" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Haryana")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Food Technology Entrepreneurship and ManagementThanjavur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Tamil Nadu")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Agartala" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Tripura")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Andhra Pradesh" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Andhra Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Arunachal Pradesh" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Arunachal Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Calicut" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Kerala")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Delhi" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Delhi")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Durgapur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("West Bengal")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Goa" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Goa")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Hamirpur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Himachal Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Jamshedpur" and i[2]!="AI" :
            
        
            s.append(i[0])
            s.append(i[1])
            
            s.append("Jharkhand")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Karnataka Surathkal" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Karnataka")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Kurukshetra" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Haryana")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Manipur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Manipur")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Meghalaya" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Meghalaya")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Mizoram" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Mizoram")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Nagaland" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Nagaland")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Patna" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Bihar")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Puducherry" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Puducherry")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Raipur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Chattisgarh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Rourkela" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Odisha")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Sikkim" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Sikkim")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Silchar" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Assam")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Srinagar" and i[2]!="AI" and i[2]=="JK":
            s.append(i[0])
            s.append(i[1])
            
            s.append("Jammu and Kashmir")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Srinagar" and i[2]!="AI" and i[2]=="LA":
            s.append(i[0])
            s.append(i[1])
            
            s.append("Ladakh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Tiruchirappalli" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Tamil Nadu")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Uttarakhand" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Uttarakhand")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="National Institute of Technology Warangal" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Telangana")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="North Eastern Regional Institute of Science and Technology Nirjuli-791109 (Itanagar)"                      and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Arunachal Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="North-Eastern Hill UniversityShillong" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Meghalaya")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Pt. Dwarka Prasad Mishra Indian Institute of Information Technology Design & Manufacture Jabalpur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Madhya Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Puducherry Technological University Puducherry" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Puducherry")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Punjab Engineering College Chandigarh" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Chandigarh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Sant Longowal Institute of Engineering and Technology" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Punjab")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Sardar Vallabhbhai National Institute of Technology Surat" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Gujarat")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="School of EngineeringTezpur UniversityNapaamTezpur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Assam")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="School of Planning & Architecture: Vijayawada" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Andhra Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="School of Planning & ArchitectureBhopal" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Madhya Pradesh")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="School of Planning & ArchitectureNew Delhi" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Delhi")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Shri Mata Vaishno Devi UniversityKatraJammu & Kashmir" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Jammu and Kashmir")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="University of Hyderabad" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Maharashtra")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=="Visvesvaraya National Institute of Technology Nagpur" and i[2]!="AI" :
            s.append(i[0])
            s.append(i[1])
            
            s.append("Maharashtra")
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        
        elif i[0]=="Assam University Silchar" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Atal Bihari Vajpayee Indian Institute of Information Technology & Management Gwalior" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Birla Institute of Technology Deoghar Off-Campus" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Birla Institute of Technology Mesra Ranchi" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Birla Institute of Technology Patna Off-Campus" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Central University of Haryana" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Central University of Jammu" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Central University of RajasthanRajasthan" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Central institute of Technology KokrajarAssam" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Chhattisgarh Swami Vivekanada Technical UniversityBhilai (CSVTU Bhilai)" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Dr. B R Ambedkar National Institute of Technology Jalandhar" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Ghani Khan Choudhary Institute of Engineering and Technology MaldaWest Bengal" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Gurukula Kangri Vishwavidyalaya Haridwar" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Carpet Technology  Bhadohi" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Engineering Science and Technology Shibpur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Handloom Technology Salem" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Handloom Technology(IIHT)Varanasi" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology  Manipur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology (IIIT) Nagpur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology (IIIT) Pune" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology (IIIT) Ranchi" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology (IIIT)KotaRajasthan" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology (IIIT)Sri CityChittoor" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Agartala" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Allahabad" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Bhagalpur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Bhopal" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Design & Manufacturing Kancheepuram" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Design & Manufacturing Kurnool Andhra Pradesh" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Guwahati" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Lucknow" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Surat" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Tiruchirappalli" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology Vadodara International Campus Diu (IIITVICD)" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology(IIIT) Dharwad" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology(IIIT) KalyaniWest Bengal" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology(IIIT) KilohradSonepatHaryana" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology(IIIT) Kottayam" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology(IIIT) UnaHimachal Pradesh" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian Institute of Information Technology(IIIT)VadodaraGujrat" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Indian institute of information technology RaichurKarnataka" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Institute of Chemical Technology Mumbai Indian Oil Odisha CampusBhubaneswar" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Institute of Engineering and Technology Dr. H. S. Gour University. Sagar (A Central University)" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Institute of InfrastructureTechnology Research and Management-Ahmedabad" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Institute of Technology Guru Ghasidas Vishwavidyalaya (A Central University)Bilaspur(C.G.)" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="International Institute of Information Technology Bhubaneswar" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="International Institute of Information Technology Naya Raipur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="J.K. Institute of Applied Physics & Technology Department of Electronics & CommunicationUniversity of Allahabad- Allahabad"  and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Jawaharlal Nehru UniversityDelhi" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Malaviya National Institute of Technology Jaipur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Maulana Azad National Institute of Technology Bhopal" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Mizoram UniversityAizawl" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Motilal Nehru National Institute of Technology Allahabad" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Advanced Manufacturing Technology Ranchi" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Electronics and Information Technology Aurangabad (Maharashtra)" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Food Technology Entrepreneurship and ManagementKundli" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Food Technology Entrepreneurship and ManagementThanjavur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology  Agartala" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Andhra Pradesh" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Arunachal Pradesh" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Calicut" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Delhi" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Durgapur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Goa" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Hamirpur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Jamshedpur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Karnataka Surathkal" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Kurukshetra" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Manipur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Meghalaya" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Mizoram" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Nagaland" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Patna" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Puducherry" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Raipur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Rourkela" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Sikkim" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Silchar" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Srinagar" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Tiruchirappalli" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Uttarakhand" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="National Institute of Technology Warangal" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="North Eastern Regional Institute of Science and Technology Nirjuli-791109 (Itanagar)"                      and i[2]=="AI" :
            k.append(i)
        elif i[0]=="North-Eastern Hill UniversityShillong" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Pt. Dwarka Prasad Mishra Indian Institute of Information Technology Design & Manufacture Jabalpur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Puducherry Technological UniversityPuducherry" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Punjab Engineering CollegeChandigarh" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Sant Longowal Institute of Engineering and Technology" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Sardar Vallabhbhai National Institute of Technology Surat" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="School of EngineeringTezpur UniversityNapaamTezpur" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="School of Planning & Architecture: Vijayawada" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="School of Planning & ArchitectureBhopal" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="School of Planning & ArchitectureNew Delhi" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Shri Mata Vaishno Devi UniversityKatraJammu & Kashmir" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="University of Hyderabad" and i[2]=="AI" :
            k.append(i)
        elif i[0]=="Visvesvaraya National Institute of Technology Nagpur" and i[2]=="AI" :
            k.append(i)
        else:
            k.append(i)

with open("okom.csv" , "a") as mai:
    ji=csv.writer(mai)
    ji.writerows(k)    

import csv
with open("okom.csv" , "r") as a:
    b=csv.reader(a)
    s=[]
    for i in b:
        if i[2]!="AI":
            s.append(i[2])
    k=set(s)
    for x in sorted(k):
        print("<option>"+x+"</option>")
   '''     
