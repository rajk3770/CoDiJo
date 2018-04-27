# import random
import threading
import time
from indeed import *
from monster import *
from naukri import *
from Shine import *

'''
class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter'''


class Jobs:
    is_all_alive = 1

    @staticmethod
    def search_jobs(string):
        def run(name, entered_job):
            time.sleep(10)
            # Get lock to synchronize threads
            threadLock.acquire()
            # print_time(self.name, self.counter, 3)
            # Free lock to release next thread
            '''print("Starting ", name)
            print("hello",name)
            print("hi",name)'''

            # print(threading.current_thread().getName())
            # threading.current_thread().getName().daemon(True)

            '''
            if (threading.current_thread().getName() == '1' or threading.current_thread().getName() == '3'):
                print('Here')
                b.main(make_url_for_indeed(string))
            elif (threading.current_thread().getName() == '2' or threading.current_thread().getName() == '4'):
                m.monster(make_url_for_monster(string))
            '''
            print(name)

            if name == '0' or name == '4' or name == '8' or name == '12' or name == '16':
                indeed_object = Indeed()
                indeed_object.main(make_url_for_indeed(entered_job))
                print("indeed")
            elif name == '2' or name == '6' or name == '10' or name == '14' or name == '18':
                monster_object = Monster()
                monster_object.monster(make_url_for_monster(entered_job))
                print("monster")
            elif name == '1' or name == '5' or name == '9' or name == '13' or name == '17':
                naukri_object = Naukri()
                naukri_object.naukri_job(entered_job)
                print("naukri")
            elif name == '3' or name == '7' or name == '11' or name == '15' or name == '19':
                shine_object = Shine()
                shine_object.shine_job(entered_job)
                print("shine")

            threadLock.release()

        '''
        def print_time(threadName, delay, counter):
           while counter:
              time.sleep(delay)
              print ("%s: %s" % (threadName, time.ctime(time.time())))
              counter -= 1
        '''

        def make_url_for_indeed(entered_job):
            # print('Atleast here')

            words = entered_job.split(" ")
            i = 0
            final = 'https://www.indeed.co.in/jobs?q='
            while i != len(words):
                if i + 1 != len(words):
                    final += words[i] + "+"
                else:
                    final += words[i]
                i += 1
            final += "&l="
            # print(final)
            return final

        def make_url_for_monster(entered_job):
            # string = input("Enter Job")
            words = entered_job.split(" ")
            i = 0
            final = 'http://www.monsterindia.com/'
            while i != len(words):
                final += words[i] + "-"
                i += 1
            final += "jobs.html"
            # print(final)
            return final

        '''
        def run():
            #self.lock.acquire()
            # lock = threading.RLock()

            global lock

            lock.acquire()
            print(threading.current_thread().getName())
            #threading.current_thread().getName().daemon(True)
            string = input("Enter Job")

            if(threading.current_thread().getName()=='1'):
                print('Here')
                b.main(make_url_for_indeed(string))
            elif(threading.current_thread().getName()=='2'):
                m.monster(make_url_for_monster(string))
            #self.lock.release()
            lock.release()
        '''
        threadLock = threading.Lock()
        threads = []
        # string = input("Enter Job")
        # Create new threads
        # thread1 = myThread(1, "Thread-1", 1)
        # thread2 = myThread(2, "Thread-2", 2)
        # thread3=Timer(10, )
        # thread4=Timer(10, hi)
        # thread3.start()

        # no_of_results = random.randint(15, 20)
        # for i in range(4):
        #     thread = threading.Thread(target=run, args=(i, string,))
        #     threads.append(thread)
        #
        #
        # threads[0].start()
        # threads[1].start()
        # threads[2].start()
        # threads[3].start()

        thread0 = threading.Thread(target=run, args=('0', string,))
        thread1 = threading.Thread(target=run, args=('1', string,))
        thread2 = threading.Thread(target=run, args=('2', string,))
        thread3 = threading.Thread(target=run, args=('3', string,))
        thread4 = threading.Thread(target=run, args=('4', string,))
        thread5 = threading.Thread(target=run, args=('5', string,))
        thread6 = threading.Thread(target=run, args=('6', string,))
        thread7 = threading.Thread(target=run, args=('7', string,))
        thread8 = threading.Thread(target=run, args=('8', string,))
        thread9 = threading.Thread(target=run, args=('9', string,))
        thread10 = threading.Thread(target=run, args=('10', string,))
        thread11 = threading.Thread(target=run, args=('11', string,))
        thread12 = threading.Thread(target=run, args=('12', string,))
        thread13 = threading.Thread(target=run, args=('13', string,))
        thread14 = threading.Thread(target=run, args=('14', string,))
        thread15 = threading.Thread(target=run, args=('15', string,))
        thread16 = threading.Thread(target=run, args=('16', string,))
        thread17 = threading.Thread(target=run, args=('17', string,))
        thread18 = threading.Thread(target=run, args=('18', string,))
        thread19 = threading.Thread(target=run, args=('19', string,))

        # Start Threads

        thread0.start()
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()
        thread9.start()
        thread10.start()
        thread11.start()
        thread12.start()
        thread13.start()
        thread14.start()
        thread15.start()
        thread16.start()
        thread17.start()
        thread18.start()
        thread19.start()

        thread0.join()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
        thread7.join()
        thread8.join()
        thread9.join()
        thread10.join()
        thread11.join()
        thread12.join()
        thread13.join()
        thread14.join()
        thread15.join()
        thread16.join()
        thread17.join()
        thread18.join()
        thread19.join()


        if not thread0.is_alive() and not thread1.is_alive() and not thread2.is_alive() and not thread3.is_alive() and not thread4.is_alive()  and not thread5.is_alive() and not thread6.is_alive() and not thread7.is_alive() and not thread8.is_alive() and not thread9.is_alive() and not thread10.is_alive()  and not thread5.is_alive() and not thread6.is_alive() and not thread7.is_alive() and not thread8.is_alive() and not thread9.is_alive() and not thread10.is_alive() and not thread11.is_alive() and not thread12.is_alive() and not thread13.is_alive() and not thread14.is_alive() and not thread15.is_alive() and not thread16.is_alive() and not thread17.is_alive() and not thread18.is_alive() and not thread19.is_alive():
            Jobs.is_all_alive = 0

        # Add threads to thread list
        # threads.append(thread1)
        # threads.append(thread2)

        # Wait for all threads to complete
        '''
        for t in threads:
            t.join()
        print("Exiting Main Thread")
        '''