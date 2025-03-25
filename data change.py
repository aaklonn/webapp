
import csv
s=[]
k=[]
l={}
with open ("josaa2024.csv" ,"r") as a:
    b=csv.reader(a)
    
    for i in b :
        s.append(i[1])

with open("josaa.csv" ,"r") as ok:
    g=csv.reader(ok)
    for x in g:
        if x[1] not in s:
            k.append(x[1])
            l=set(k)
    for gag in l:
        print(gag, end='\n')
'''
import csv
with open ("josaa.csv" , "r") as a :
    b=csv.reader(a)
    s=[]
    k=[]
    for i in b:
        
        if i[0]=='National Institute of Food Technology Entrepreneurship and ManagementThanjavur':
            s.append('National Institute of Food Technology Entrepreneurship and Management Thanjavur')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Chhattisgarh Swami Vivekanada Technical UniversityBhilai (CSVTU Bhilai)':
            s.append('Chhattisgarh Swami Vivekanada Technical University Bhilai (CSVTU Bhilai)')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Indian Institute of Information Technology(IIIT)VadodaraGujrat':
            s.append('Indian Institute of Information Technology(IIIT) Vadodara Gujrat')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='North-Eastern Hill UniversityShillong':
            s.append('North-Eastern Hill University Shillong')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='School of Planning & ArchitectureNew Delhi':
            s.append('School of Planning & Architecture New Delhi')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Shri Mata Vaishno Devi UniversityKatraJammu & Kashmir':
            s.append('Shri Mata Vaishno Devi University Katra Jammu & Kashmir')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Punjab Engineering CollegeChandigarh':
            s.append('Punjab Engineering College Chandigarh')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Indian institute of information technology RaichurKarnataka':
            s.append('Indian institute of information technology Raichur Karnataka')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='J.K. Institute of Applied Physics & Technology Department of Electronics & CommunicationUniversity of Allahabad- Allahabad':
            s.append('J.K. Institute of Applied Physics & Technology Department of Electronics & Communication University of Allahabad- Allahabad')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Ghani Khan Choudhary Institute of Engineering and Technology MaldaWest Bengal':
            s.append('Ghani Khan Choudhary Institute of Engineering and Technology Malda West Bengal')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Jawaharlal Nehru UniversityDelhi':
            s.append('Jawaharlal Nehru University Delhi')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Indian Institute of Information Technology(IIIT) UnaHimachal Pradesh':
            s.append('Indian Institute of Information Technology(IIIT) Una Himachal Pradesh')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Mizoram UniversityAizawl':
            s.append('Mizoram University Aizawl')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='School of Planning & ArchitectureBhopal':
            s.append('School of Planning & Architecture Bhopal')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Indian Institute of Information Technology (IIIT)KotaRajasthan':
            s.append('Indian Institute of Information Technology (IIIT)Kota Rajasthan')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='National Institute of Food Technology Entrepreneurship and ManagementKundli':
            s.append('National Institute of Food Technology Entrepreneurship and Management Kundli')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Institute of InfrastructureTechnology Research and Management-Ahmedabad':
            s.append('Institute of Infrastructure Technology Research and Management-Ahmedabad')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Institute of Chemical Technology Mumbai Indian Oil Odisha CampusBhubaneswar':
            s.append('Institute of Chemical Technology Mumbai Indian Oil Odisha Campus Bhubaneswar')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='School of EngineeringTezpur UniversityNapaamTezpur':
            s.append('School of Engineering Tezpur University Napaam Tezpur')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Puducherry Technological UniversityPuducherry':
            s.append('Puducherry Technological University Puducherry')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Indian Institute of Information Technology (IIIT)Sri CityChittoor':
            s.append('Indian Institute of Information Technology (IIIT) Sri City Chittoor')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Indian Institute of Handloom Technology(IIHT)Varanasi':
            s.append('Indian Institute of Handloom Technology(IIHT) Varanasi')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='School of Planning & Architecture: Vijayawada':
            s.append('School of Planning & Architecture Vijayawada')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Indian Institute of Information Technology  Manipur':
            s.append('INDIAN INSTITUTE OF INFORMATION TECHNOLOGY SENAPATI MANIPUR')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
        elif i[0]=='Institute of Technology Guru Ghasidas Vishwavidyalaya (A Central University)Bilaspur(C.G.)':
            s.append('School of Studies of Engineering and Technology Guru Ghasidas Vishwavidyalaya Bilaspur')
            s.append(i[1])
            
            s.append(i[2])
            s.append(i[3])
            s.append(i[4])  
            s.append(i[5])
            s.append(i[6])
            k.append(s)
            s=[]
            
        else:
            k.append(i)

with open("josaa1.csv" , "a") as mai:
    ji=csv.writer(mai)
    ji.writerows(k)    

'''
