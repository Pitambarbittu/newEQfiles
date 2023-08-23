import requests

myToken = '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'
myUrl = 'https://api.github.com/'
head = {'Authorization': 'token {}'.format(myToken)} 
response = requests.get(myUrl, headers=head)

#My-Token:    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


# organisational requests

def morgpro(org):
    url= myUrl +"orgs/" + org + "/projects"
    print(url)
    res=requests.get(url,auth=(myToken,''))
    print(res)
morgpro("pitambar-orgs")
# response[200]



def morgs(org):
    url = myUrl + "orgs/" + org + "/projects"
    print(url)
    todo = {"org":org,
            "name": "project1",
            "body": "this is project1"}
    res = requests.post(url, json=todo,headers=head)
    print(res)
    
morgs("pitambar-orgs")    
# #<Response [410]>:gone

#-----------------------------------------------------------------------------------------------------
def mproid(project_id):
    url=myUrl +"projects/"+ project_id
    print(url)
    res=requests.get(url,auth=(myToken,''))
    print(res)
    return res.json()
mproid("2")
#[403]:forbidden

#-------------------------------------------------------------------------------------------------------
def mprojson(project_id):
    url=myUrl +"projects/"+ project_id
    print(url)
    todo={"name":"project1",
          "body":"Project1 body" }
  
    res = requests.patch(url, auth=(myToken, ''), json=todo,headers=head)
    print(res)
mprojson("1")
#[403]:forbidden

#--------------------------------------------------------------------------------------------------------
def mproid(project_id):
    url=myUrl +"projects/"+ project_id
    print(url)
    res = requests.delete(url, auth=(myToken, ''),headers=head)

    return print(res)
    
mproid("1")
# # <Response [403]>

#---------------------------------------------------------------------------------------------------------
def mowner(owner,repo):
    url=myUrl+"repos/"+owner +"/"+repo+"/projects"
    print(url)
    res=requests.get(url,auth=(myToken,''))
    print(res)
    return res.json()
mowner("Pitambarbittu","My-Portfolio")
# #<Response [200]>
#---------------------------------------------------------------------------------------------------------
def mportfolio(owner,repo):
    url=myUrl+"repos/"+owner +"/"+repo+"/projects"
    print(url)
    todo = {"name":"myportfolio",
          "body":"myProject body" } 
    res = requests.post(url, auth=(myToken, ''), json=todo,headers=head)          
  #  res=requests.post(url, auth=(myToken, ''), json=todo)
    print(res)
    print("hello")
    
mportfolio("Pitambarbittu","My-Portfolio")
# #<Response [410]>:gone
#----------------------------------------------------------------------------------------------------------

def mtodo():
    url=myUrl+"user/projects"
    print(url)
    todo = {"name":"myproject1",
          "body":"myProject1 body" } 
    res=res = requests.post(url, auth=(myToken, ''), json=todo,headers=head)
    print(res)
    
mtodo()
# #res[410]:not such privileges 
#---------------------------------------------------------------------------------------------------------

def muser(username):
    url=myUrl+"users/"+username+"/projects"
    print(url)
    res=requests.get(url,auth=(myToken,''))
    print(res)
   
muser("Pitambarbittu")
# #response[200]
#---------------------------------------------------------------------------------------------------------
