from bs4 import BeautifulSoup
import requests
import regex as re
from nltk import tokenize
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="03041999", db="jobs")
cursor = db.cursor()


# class for naukri.com
class Naukri:

    i = 1

    @staticmethod
    def remove_starting_space(string):
        i = 0
        string = string.strip('[')
        for _ in range(len(string)):
            if string[i] == ' ' or string[i] == '-':
                # print("string[i]=", string[i])
                i = i+1
            else:
                break
        # print("last", string[i])
        return i

    @staticmethod
    def clean(html_string):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', str(html_string)).strip()
        return cleantext


    def naukri_job(self, url):
        try:
            url = 'https://www.naukri.com/'+url.replace(' ', '-')+'-jobs'
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            url_list = []
            job_name = soup.find_all(attrs={"class": "desig", "itemprop": "title"})
            skills = soup.find_all(attrs={"class": "skill", "itemprop": "skills"})
            # desc = soup.find_all(attrs={"class": "desc", "itemprop": "description"})
            company_name = soup.find_all(attrs={"class": "org", "itemprop": "hiringOrganization"})
            exp = soup.find_all(attrs={"class": "exp", "itemprop": "experienceRequirements"})
            location = soup.find_all(attrs={"itemprop": "jobLocation"})
            for tag in soup.find_all(attrs={"class": "content", "count": self.i+1}):
                url_list.append(tag.get('href'))

            # print("job description-"+clean(desc[2]))
            desc_url = url_list[0]
            description_page = requests.get(desc_url)
            desc_soup = BeautifulSoup(description_page.text, 'html.parser')
            description = desc_soup.find_all("ul", {"class": "listing mt10 wb", "itemprop": "description"})
            description = self.clean(description)
            description = tokenize.sent_tokenize(description)
            # description = [description[0],description[1],description[2]]

            print("job: " + self.clean(job_name[Naukri.i]))
            print("company: " + self.clean(company_name[Naukri.i]))

            description_list = ""
            if len(description) > 1:
                # print("1")
                a = description[0]
                pos = self.remove_starting_space(a)
                print(a[pos+1:len(a)].replace('  ', ' '))
                description_list = description_list + a[pos+1:len(a)].replace('  ', ' ')

            if len(description) > 2:
                # print("2")
                a = description[1]
                pos = self.remove_starting_space(a)
                print(a[pos:len(a)].strip('-'))
                description_list = description_list + a[pos:len(a)].strip('-')

            if len(description) > 3:
                # print("3")
                a = description[2]
                pos = self.remove_starting_space(a)
                print(a[pos:len(a)].strip('-'))
                description_list = description_list + a[pos:len(a)].strip('-')
            print("Description:",description_list)
            print("skills-" + self.clean(skills[Naukri.i]))
            print("location-" + self.clean(location[Naukri.i]))
            print("Work Experience-" + self.clean(exp[Naukri.i]))
            print("For More Details-" + url_list[0])

            print("\n")
            query = "insert into job_details(job_name,company,description,skills,experience,location,url)"\
                    "values(%s,%s,%s,%s,%s,%s,%s)"
            args = (self.clean(job_name[Naukri.i]),
                    self.clean(company_name[Naukri.i]),
                    description_list,
                    self.clean(skills[Naukri.i]),
                    self.clean(exp[Naukri.i]),
                    self.clean(location[Naukri.i]),

                    url_list[0]
                    )

            cursor.execute(query, args)
            db.commit()

        except Exception:
            pass
        Naukri.i += 1
# url = input("Enter keyword")
# n = Naukri()
# n.naukri_job(url)
# n.naukri_job(url)
# n.naukri_job(url)
# n.naukri_job(url)
