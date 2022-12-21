import os
import shutil

def get_topics(path_dir):
    topics=[]
    for file in os.listdir(path_dir):
        if file.endswith('.pdf'):
            topics.append(file.split("_")[-1])
    topics=list(set([(i.lower()).split('.')[0] for i in topics]))
    return topics

def create_folders(path_dir,topics):
    try:
        os.mkdir('Dataset')
    except:
        pass

    for i in topics: 
        try:
            os.mkdir('Dataset\\'+i)
        except:
            pass
        
def move_to_folders(path_dir):
    for file in os.listdir(path_dir):
        if file.endswith('.pdf'):
            key=((file.split('_')[-1]).split('.')[0]).lower()
            shutil.copy(path_dir+'/'+file,'.//Dataset//'+key+'//'+file)
            os.remove(path_dir+'/'+file)
            

if __name__=='__main__':
    path_dir=input('Enter the path where all documents are present: ')
    topics=get_topics(path_dir)
    print(topics)
    create_folders(path_dir,topics)
    move_to_folders(path_dir)