#for text copied
with open('E:/VS studio/Python/to learn py/7File Handling/test.txt','r') as rf:
  with open('E:/VS studio/Python/to learn py/7File Handling/copied.txt','w') as wf:
    for line in rf:
      wf.write(line)

#for picture copy- to be opened in binary mode
with open('E:/VS studio/Python/to learn py/7File Handling/pic.png','rb') as rf:
  with open('E:/VS studio/Python/to learn py/7File Handling/pic_copied.png','wb') as wf:
    for line in rf:
      wf.write(line)

#copying images using sizes(chunk)
with open('E:/VS studio/Python/to learn py/7File Handling/pic.png','rb') as rf:
  with open('E:/VS studio/Python/to learn py/7File Handling/pic_copied1.png','wb') as wf:
    chunksize=4000
    readchunk=rf.read(chunksize)
    while len(readchunk) >0 :
      wf.write(readchunk)
      readchunk=rf.read(chunksize)