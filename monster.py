from bs4 import BeautifulSoup
import requests
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="03041999", db="jobs")
cursor = db.cursor()


# class for Monster.com
class Monster:
    c = 0

    @staticmethod
    def monster(url1):

        # global c
        # print(monster_final.c)

        r = requests.get(url1)

        data = r.text
        url = []
        title = []
        details = []
        company = []
        descrpition = []
        exp = []
        loc = []
        skills = []
        list1 = []
        soup = BeautifulSoup(data, "html.parser")

        for link in soup.find_all('a', {"class": "title_in"}):
            url.append(link.get('href'))
            title.append(link.get('title'))

        for link in soup.find_all('div', {"class": "jtxt"}):
            details.append(link.get_text())

        z = 3
        for y in range(len(details)):

            if y == z:
                # print(details[y],y)
                if 'Summary' not in str(details[y]):
                    # print("--------------------If ke andar")
                    details.insert(y, '')
                    # print(details[y])
                    z += 6
                else:

                    # print(details[y], y)
                    # print("Kuch nhi-------------------------------------------------")
                    z += 6
        # print("After checking:" ,details)

        k = 1
        j = 1
        while j < (len(details)):
            if k == 1:
                company.append(details[j])
                # print(company)
                k += 1
            elif k == 2:
                skills.append(details[j])
                # print(skills)
                k += 1
            elif k == 3:
                descrpition.append(details[j])
                # print(descrpition)
                k += 1
            elif k == 4:
                loc.append(details[j])
                # print(loc)
                k += 1
            elif k == 5:
                exp.append(details[j])
                # print(exp)
                k += 1
            else:
                k = 1
                # print()
            j += 1

        print()
        print(title[Monster.c])
        print(company[Monster.c])
        print("Description:" + descrpition[Monster.c][8:])
        print("Skills Required:" + skills[Monster.c][10:])
        print("Location:" + loc[Monster.c])
        print("Work Experience:" + exp[Monster.c])
        print("For More Details, " + url[Monster.c])


        query = "insert into job_details(job_name,company,description,skills,experience,location,url)" \
                "values(%s,%s,%s,%s,%s,%s,%s)"
        args = (title[Monster.c],
                company[Monster.c],
                descrpition[Monster.c][8:],
                skills[Monster.c][10:],
                exp[Monster.c],
                loc[Monster.c],
                url[Monster.c]
                )

        cursor.execute(query, args)
        db.commit()
        Monster.c += 1
    '''
        for i in range(len(title)):
            print(title[i])
            print()


                for link in soup.find_all('div',{"class":"jtxt jico ico1"}):
                    loc.append(link.get_text())


                for link in soup.find_all('div',{"class":"jtxt jico ico2"}):
                    exp.append(link.get_text())

      '''

    '''
    for i in range(len(title)):
        print(title[i])
        j=i*6+1
        while j<=(i*6+5):
            print(str(details[j]))
            j+=1
        print(url[i])
        print()



    for j in range(len(title)):
        print(title[j])
        print(company[j])
        print(descrpition[j])
        print(skills[j])
        print("Location:" +loc[j])
        print("Work Experience:" +exp[j])
        print("For More Details:" +url[j])
        print()
        '''


# string = input("Enter Job")
# words=string.split(" ")
# i=0
# final='http://www.monsterindia.com/'
# while i!=len(words):
#     final+=words[i]+"-"
#     i+=1
# final+="jobs.html"
# print(final)
#
# # print(monster_final.c)
# obj=monster_final()
# obj.monster(final)
# monster_final.c+=1
# obj1=monster_final()
# obj1.monster(final)
# print(monster_final.c)
