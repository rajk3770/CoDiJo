from bs4 import BeautifulSoup
import requests
import nltk
# from nltk import tokenize
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="password", db="jobs")
cursor = db.cursor()


# class for indeed.com
class Indeed:
    c = 0

    def get_desp(self, url):
        r = requests.get(url)

        data = r.text

        soup = BeautifulSoup(data, "html.parser")
        list4 = []
        list5 = []
        for link in soup.findAll('span', {'id': 'job_summary'}):
            list4 = nltk.sent_tokenize(link.get_text())
            # print(list4)
        # print(soup.find)
        # print(str(list4[0]).find('\n'))
        if str(list4[0]).find('\n') != -1:
            # print(list4[0])
            print("Description: ", list4[0][0:str(list4[0]).find('\n')])
            return list4[0][0:str(list4[0]).find('\n')]
        else:
            print("Description: ", list4[0][0:str(list4[0]).find('.')])
            return list4[0][0:str(list4[0]).find('.')]
        # print('Description over')

    def get_exp(self, url):
        # print('Inside Description')
        r = requests.get(url)
        skills = ""
        data = r.text

        soup = BeautifulSoup(data, "html.parser")
        list4 = []
        list5 = []
        for link in soup.findAll('span', {'id': 'job_summary'}):
            list4 = nltk.sent_tokenize(link.get_text())
            # print("Without any change" ,link.get_text())
        # print(list4)
        c = 0
        for j in list4:
            list5 = nltk.word_tokenize(j)
            # print(list5)
            for k in list5:
                if 'years' in k:
                    start, end = self.get_indexes(j)
                    # print('Came till here')
                    # print(start,end)
                    # print()
                    # print('-------------------------------------')
                    if start != 0:
                        print("Work Experience:", j[start + 1:end])
                        skills += j[start + 1:end]
                    else:
                        # print("I was here")
                        print("Work Experience:", j[start:end])
                        skills += j[start:end]
                    # print('-------------------------------------')
                    # print()
                    c = 1
                    break
            if c == 1:
                break
        return skills
        # print("Out of loop")

    '''
    def get_indexes(s):
        j,t=0,0
        for k in range(s.find('years')):
            if (s[k] == '\n'):
                j = k
        #print("hello:",s[j:s.find('years')])
        print("j=",j)
        z=s.find('years')
        #print(j)
        while z<(len(s)):
            #print(len(s),z)
            if(s[z]=='\n'):
                t=z
                break
            z+=1
        if(t==len(s)):
            t=0
            z=s.find('years')
            while(z<(len(s))):

                if (s[z]=='.'):
                    #print("Idhar:",s[z])
                    t = z
                    break
            z+=1

        print("t=",t)
        return j+1,t


    def check_this(s,x,start):

    '''

    def get_indexes(self, s):
        newline_before = self.find_last(s, 0, s.find('years'), '\n')
        dot_before = self.find_last(s, 0, s.find('years'), '.')
        newline_after = self.find_first(s, s.find('years'), len(s), '\n')
        dot_after = self.find_first(s, s.find('years'), len(s), '.')
        if dot_before > newline_before:
            start = dot_before
        elif newline_before > dot_before:
            start = newline_before
        else:
            start = 0

        if dot_after < newline_after:
            end = dot_after
        elif newline_after < dot_after:
            end = newline_after
        else:
            end = len(s)
        return start, end

    def find_last(self, s, start, end, x):

        t = 0
        while start < end:
            if s[start] == x:
                t = start
            start += 1
        return t

    def find_first(self, s, start, end, x):
        t = 0
        # print("Start=",start)
        # print("End=",end)
        while start < end:
            if s[start] == x:
                t = start
                break
            start += 1
        if t == 0:
            t = len(s)
        # print(t)
        # print("t=",s[t:])
        return t

    def main(self, url):
        r = requests.get(url)

        data = r.text

        soup = BeautifulSoup(data, "html.parser")
        '''list1 = []
        list1 = soup.findAll(attrs={"class": "summary"})

        k = 0
        list2 = []
        for i in list1:
            list1[k] = i.get_text().strip()
            k += 1
        print(list1)
        print(list2)
        k = 0
         + list1[k] + "\n" 
        '''

        url2 = []
        title = []
        company = []
        loc = []

        for link in soup.find_all('a'):
            if link.get('data-tn-element') == 'jobTitle':
                url1 = "https://www.indeed.co.in/" + link.get('href')
                title.append(link.get('title'))
                # self.get_desp(url1)
                # self.get_exp(url1)
                url2.append(url1)
                # print()

        for link in soup.find_all('span', {'class': 'company'}):
            company.append(link.get_text())
        for link in soup.find_all('span', {'class': 'location'}):
            loc.append(link.get_text())

        # print(company)
        # print(loc)
        print()
        print(title[Indeed.c])
        print(str(company[Indeed.c]).strip())
        desp = self.get_desp(url2[Indeed.c])
        print("Location:", loc[Indeed.c])
        exp = self.get_exp(url2[Indeed.c])
        print("For more Details ", url2[Indeed.c])

        query = "insert into job_details(job_name,company,description,skills,experience,location,url)" \
                "values(%s,%s,%s,%s,%s,%s,%s)"
        args = (title[Indeed.c],
                str(company[Indeed.c]).strip(),
                desp,
                "null",
                exp,
                str(loc[Indeed.c]),
                str(url2[Indeed.c])
                )

        cursor.execute(query, args)
        db.commit()
        Indeed.c += 1






# url = input("Enter website")
# get_exp('https://www.indeed.co.in/viewjob?cmp=sumayya.essack%40eflglobal.com&t=Senior+Data+Scientist&jk=fc0f667b3f5341c6&sjdu=QwrRXKrqZ3CNX5W-O9jEvb3jah1zuiM8AKGmwjJO4JwepeX_GpCCu9IQJP_iqumzDcwKRGvgnd7y9g1eTwIGWF28py_5B5u5GdPx13wcuT4&tk=1c9qtpapd9u0q9p8&pub=4a1b367933fd867b19b072952f68dceb&vjs=3')
# get_title('https://www.indeed.co.in/viewjob?jk=6a61ab2ec1072b08&tk=1c9qtpapd9u0q9p8&from=serp&vjs=3')
# get_exp('https://www.indeed.co.in/viewjob?jk=6a61ab2ec1072b08&tk=1c9qtpapd9u0q9p8&from=serp&vjs=3')


# string=input("Enter Job")
# words=string.split(" ")
# i=0
# final='https://www.indeed.co.in/jobs?q='
# while i!=len(words):
#     if(i+1!=len(words)):
#         final+=words[i]+"+"
#     else:
#         final+=words[i]
#     i+=1
# final+="&l="
# print(final)
# obj=Indeed()
# obj.main(final)
# obj1=Indeed()
# obj1.main(final)
# print("End")
