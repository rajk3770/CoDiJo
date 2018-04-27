from bs4 import BeautifulSoup
import requests
import regex as re
from nltk import tokenize
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="03041999", db="jobs")
cursor = db.cursor()


# class for Shine.com
class Shine:

    i = 2

    @staticmethod
    def clean(html_string):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', str(html_string)).strip()
        return cleantext

    def shine_job(self, url):

        url_list = []
        url = 'https://www.shine.com/job-search/'+url.replace(' ', '-')+'-jobs'
        shine = requests.get(url)
        soup2 = BeautifulSoup(shine.text, 'html.parser')
        job_name = soup2.find_all('strong')
        company_name = soup2.find_all("li", {"class": "snp_cnm cls_cmpname cls_jobcompany"})
        exp = soup2.find_all("span", {"class": "snp_yoe cls_jobexperience"})
        location = soup2.find_all("em", {"class": "snp_loc cls_joblocation"})
        for tag in soup2.find_all("a", {"class": "cls_searchresult_a"}):
            url_list.append(tag.get('href'))

        """shine_desc = soup2.find_all("li", {"class": "srcresult"})"""

        desc = requests.get('https://www.shine.com' + url_list[Shine.i])
        desc = BeautifulSoup(desc.text, 'html.parser')
        description = desc.find_all("span", {"itemprop": "description"})
        skills = soup2.find_all("i", {"class": "sk jsrp cls_jobskill"})
        print("job: " + self.clean(job_name[Shine.i + 3]))
        print("company: " + self.clean(company_name[Shine.i]))
        description = tokenize.sent_tokenize(str(description))
        description_cleaned = str(self.clean(description))
        list_desc = []
        length = len(description_cleaned)
        i, j = 0, 0
        description_cleaned = description_cleaned.replace("\\xa0", " ")
        description_list = ""
        # print(description)
        # print(description_cleaned)
        try:
            for k in range(2):
                while i < length - 1:
                    if description_cleaned[i] == "\\":
                        if description_cleaned[i + 1] == "n":
                            list_desc.append(description_cleaned[j:i])
                            j = i
                    # elif description_cleaned == ".":
                    #     list_desc.append(description_cleaned[0:i])

                    i = i+1
            print(list_desc[0].strip("[").strip("\'").strip('['), list_desc[1].replace('\\n', '.'))
            description_list += list_desc[0].strip("[").strip("\'").strip('['), list_desc[1].replace('\\n', '.')

        except Exception:
            pass

        try:
            i = 0
            while i < length-1:
                if description_cleaned[i] == ".":
                    list_desc.append(description_cleaned[0:i])
                    break
                i = i+1

            print(list_desc[0].strip("[").strip("\'").strip('['))
            description_list += list_desc[0].strip("[").strip("\'").strip('[')

        except Exception:
            pass

        cleantext = self.clean(skills[Shine.i])
        print('skills:'+cleantext.replace(' ', '').replace('\n', ' '))
        print("Experience:"+self.clean(exp[Shine.i]))
        print(self.clean(location[Shine.i]))
        print("For more details: https://www.shine.com"+url_list[Shine.i])

        print(Shine.i)
        print("\n")
        query = "insert into job_details(job_name,company,description,skills,experience,location,url)" \
                "values(%s,%s,%s,%s,%s,%s,%s)"
        args = (str(self.clean(job_name[Shine.i + 3])),
                str(self.clean(company_name[Shine.i])),
                str(description_list),
                str(cleantext.replace(' ', '').replace('\n', ' ')),
                str(self.clean(exp[Shine.i])),
                str(self.clean(location[Shine.i])),
                str("https://www.shine.com/" +url_list[Shine.i])
                )

        cursor.execute(query, args)
        db.commit()
        Shine.i += 1


# url = input("Enter keyword")
# s = Shine()
# s.shine_job(url)
