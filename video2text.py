from youtube_transcript_api import YouTubeTranscriptApi as yta
import re,sys
from datetime import datetime
url=input(' Enter url... \n')
idIndexVal=url.find("?v=")
if idIndexVal==-1:
    print(" Invalid Url. Provide a valid URL ".center(60,"="))
    sys.exit()
vid_id=url[idIndexVal+3:]
# https://www.youtube.com/watch?v=hLoatpfE7VM
# vid_id='xXkIpZutTsI&t=45s'
# extract text from video
lan_org=[]
lan_target=[]
availableLangs=[]
availableTranslts=[]
#see all available transcript languages
transcript_list = yta.list_transcripts(vid_id) 
if len(transcript_list._manually_created_transcripts)>0:
    print('\nManually created transcript(s) found\n')
else:
    print('\nA manually created transcipt is not found\n')    
print("Transcripts available in : ")
for tritem in transcript_list:
    if tritem.language_code not in availableLangs:
        availableLangs.append(tritem.language_code) 
for lang in availableLangs:
    print(lang+'\n')        
nlc=input("Type native language code (2 characters e.g. en,tr,de): ")
if nlc not in availableLangs:
    print(nlc+ ' is not a defined language')
    input()
    sys.exit()

tlc=input("Type target language code (2 characters e.g. en,tr,de): ")
data=yta.get_transcript (vid_id,languages=[nlc])
   
transcript=''

tempStr=''
for value in data:
    for key,val in value.items():
        if key=='text':
            if "." in val :
                val=val.replace('\n',' ')
                tempStr+=' '+val
                lan_org.append(' '+tempStr+'\n')
                tempStr=''
            else :
                val=val.replace('\n',' ')
                tempStr+=' '+val

            # lan_org.append(' '+val+'\n')
           
# write transcript into a file
if len(lan_org)>0:
    tempStr=''
     
now=datetime.now()
file=open("original_text {lngOrgn} {time}.doc".format(time=now.strftime("%H_%M_%S"),lngOrgn=nlc),"w")
if len(lan_org)==0:
    lan_org.append(tempStr) 
    
file.writelines(lan_org)   
file.close()
print('Original script is saved..')

# get translated subtitle
tempStr=''
transcriptTranslated = transcript_list.find_transcript([nlc])
translated_transcript = transcriptTranslated.translate(tlc)
data_translated=translated_transcript.fetch()
for value in data_translated:
    for key,val in value.items():
        if key=='text' :
            if "." in val :
                val=val.replace('\n',' ')
                tempStr+=' '+val
                lan_target.append(' '+tempStr+'\n')
                tempStr=''
            else:
                val=val.replace('\n',' ')
                tempStr+=' '+val
          
if len(lan_target)==0:
    lan_target.append(tempStr)             

file2=open("translated_text {lngTrgt} {time}.doc".format(time=now.strftime("%H_%M_%S"),lngTrgt=tlc),"w")
file2.writelines(lan_target)
file2.close()
print('Translation Done..\n')


minIndex=min(len(lan_target),len(lan_org))

fileCombined=open("combined_text {cmbndLangs} {time}.doc".format(time=now.strftime("%H_%M_%S"),cmbndLangs=nlc+'&'+tlc),"w")
for k in range(minIndex):
    curStr=lan_org[k]+'\n'+lan_target[k]+'\n'
    fileCombined.writelines(curStr)

fileCombined.close()   