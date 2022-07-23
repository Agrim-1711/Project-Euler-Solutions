#Problem 18
#https://projecteuler.net/problem=18
#Find the maximum total from top to bottom of the triangle below

num = ['75','95','64','17','47','82','18','35','87','10','20','04','82','47','65','19','01','23','75','03','34','88','02','77','73','07','63','67','99','65','04','28','06','16','70','92','41','41','26','56','83','40','80','70','33','41','48','72','33','47','32','37','16','94','29','53','71','44','65','25','43','91','52','97','51','14','70','11','33','28','77','73','17','78','39','68','17','57','91','71','52','38','17','14','91','43','58','50','27','29','48','63','66','04','68','89','53','67','30','73','16','69','87','40','31','04','62','98','27','23','09','70','98','73','93','38','53','60','04','23']

#print(num)
#print(len(num))

def empty():
  return None

class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

def paths(t, p = ()):
  if not t:
    return
  elif t.leftChild or t.rightChild:
    yield from paths(t.leftChild, (*p, t.data))
    yield from paths(t.rightChild, (*p, t.data))
  else:
    yield ",".join(map(str, (*p, t.data)))

for x in range(0,len(num)):
  globals()[f"node{x+1}"] = BinaryTreeNode(num[x])
  #print(eval("node"+str(x+1)))

for n in range(1,15):
  #print("nodes:",n,"Leftmost node:",(n-1)*n/2+1,"Rightmost node:",(n-1)*n/2+1+(n-1))
  for i in range(int((n-1)*n/2+1),1+int((n-1)*n/2+1+(n-1))):
    #print("row:",n,"node:",i,"left:",i+n,"right",i+n+1)
    exec("node" + str(i) + ".leftChild=node" + str(i+n))
    exec("node" + str(i) + ".rightChild=node" + str(i+n+1))

#Fetch all possible paths into a List
allpaths = list(paths(node1))
print("number of paths:",len(allpaths))
print("first path:",allpaths[0])
print("last path:",allpaths[-1])

#Iterate over all paths and find max Sum
max_length,length=0,0
for x in allpaths:
  y = x.split(",")
  length = 0
  for i in range(0,len(y)):
      length += int(y[i])
  max_length = max(max_length,length)
print("Max sum:",max_length)