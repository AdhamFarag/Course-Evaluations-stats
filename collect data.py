import pdfplumber
import re
import csv
import os


def listToString(s):  

     # initialize an empty string 
     str1 = ""  

     # traverse in the string   
     for ele in s:  
          str1 += ele   

     # return string   
     return str1  

with open('data.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(["Course","Campus","Term","Section","Invited","Responded","Mean1","Mean2","Mean3","Mean4","Mean5","Mean6","Median1","Median2","Median3","Median4","Median5","Median6","Mode1","Mode2","Mode3","Mode4","Mode5","Mode6","StdDev1","StdDev2","StdDev3","StdDev4","StdDev5","StdDev6"])
counter = 0
for filename in os.listdir("."):
     counter+=1
     try:
          Path = ""+ filename
          Pdf = pdfplumber.open(Path)
          contents = ""
          for page in Pdf.pages:
               contents += page.extract_text()
          contents = contents.splitlines()
          '''
          this part of the code uses regex to find patters in the pdf that is now read into the file as a list of sentences
          '''
          
          r = re.compile("Responded *")
          responded_number = list(filter(r.match, contents))
          responded_number = float(''.join(responded_number) .split(" ")[1])
          
          
          r = re.compile("Invited *")
          invited_number = list(filter(r.match, contents))
          invited_number= float(''.join(invited_number) .split(" ")[1])
          
          
          r = re.compile("Course Name*");
          course_info = list(filter(r.match, contents))
          
          course_code=""
          LEC=""
          campus=""
          Term = ""
          
          r = re.compile("(Fall|Winter|Summer)\W*\w*(20[0-9]{2})")
          Term = r.search(Path)
          Term = Term.group(0)
          
          '''
          this part of the script is to look for the questions and give the sepcified question number and statistic values
          '''
          
          
          Questions = ["1. I found the course intellectually stimulating","2. The course provided me with a deeper understanding of the subject matter","3. The instructor","4. Course projects" ,"5. Course projects","6."]
          collected_data=[course_code,campus,Term,LEC,invited_number,responded_number]
          mean = ["N/A"] * 6
          mode=["N/A"] * 6
          median=["N/A"] * 6
          SD=["N/A"] * 6
          print("----------")
          Found = False
          Found1=False
          Found2=False
          Found3=False
          for i in range(0,len(contents)):
               if (Found2 ==False):
                    r = re.compile("[A-Z]{3}[A-Z|0-9]{1}[0-9]+H[0-9]*");
                    course_code = r.search(contents[i])
                    if course_code != None:
                         collected_data[0] = course_code.group(0)
                         if ("H3" in collected_data[0]):
                              collected_data[1] = "UTSC"
                         elif ("H1" in collected_data[0]):
                              collected_data[1] = "UTSG"
                         elif ("H5" in collected_data[0]):
                              collected_data[1] = "UTM"                  
                         Found2= True          
               if("LEC" in contents[i] and Found == False):
                    Found = True
                    r = re.compile("LEC[0-9]*");
                    LEC = r.search(contents[i])
                    collected_data[3]=LEC.group(0)      
               for m in range(0,len(Questions)):
                    if ((Questions[m] in contents[i])  and (("Statistics" in contents[i+1]) or ("Statistics" in contents[i+2]))):
                         #print(Questions[m])
                         if ((("Statistics" in contents[i+1]))):
                              try:
                                   mean[int(Questions[m][0])-1] = float((contents[i+2].split(" ")[1:][0]))
                              except Exception as e:
                                   print(e)
                              try:
                                   median[int(Questions[m][0])-1] = float((contents[i+3].split(" ")[1:][0]))
                              except Exception as e:
                                   print(e)
                              try:
                                   mode[int(Questions[m][0])-1] = listToString((contents[i+4].split(" ")[1:])) 
                              except Exception as e:
                                   print(e)   
                              try:
                                   if ((listToString((contents[i+5].split(" ")[2:])).strip('+/-')) != ''):
                                        SD[int(Questions[m][0])-1] = float((listToString((contents[i+5].split(" ")[2:])).strip('+/-')))
                                   else:
                                        SD[int(Questions[m][0])-1] = listToString((contents[i+5].split(" ")[2:])).strip('+/-') 
                              except Exception as e:
                                   print(e)                                 
                         
                         else:
                              try:
                                   mean[int(Questions[m][0])-1] = float((contents[i+3].split(" ")[1:][0]))
                              except Exception as e:
                                   print(e)                                 
                              try:
                                   median[int(Questions[m][0])-1] = float((contents[i+4].split(" ")[1:][0]))
                              except Exception as e:
                                   print(e)                                      
                              try:
                                   mode[int(Questions[m][0])-1] = listToString((contents[i+5].split(" ")[1:]))
                              except Exception as e:
                                   print(e)                                     
                              
                              try:
                                   if ((listToString((contents[i+6].split(" ")[2:])).strip('+/-')) != ''):
                                        SD[int(Questions[m][0])-1] = float((listToString((contents[i+6].split(" ")[2:])).strip('+/-')))
                                   else:
                                        SD[int(Questions[m][0])-1] = listToString((contents[i+6].split(" ")[2:])).strip('+/-')     
                              except Exception as e:
                                   print(e)                                 
     except Exception as e:
          print(e)
          print("ERROR IN THIS FILE "+Path)

     with open('data.csv', 'a', newline='') as file:
          writer = csv.writer(file)
          writer.writerow(collected_data+mean+median+mode+SD)
          print(counter)