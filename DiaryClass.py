import datetime, time

class Diary:
    diary_author = "Default_User"

    def __init__(self, name):
        self.diary_author = name
        self.file_name = name + '.text'        #new file name with author
        make_file = open(self.file_name, 'w+')   #make new file
        make_file.close()

    def write_diary(self):
        self.diary_date = datetime.datetime.now()
        print ("Date : ", self.diary_date)

        title = input("Title : ")
        content = input("Content : ")
        self.diary_title = title
        self.diary_content = content

    def save_diary(self):
        with open(self.file_name, 'a') as diary_write:
            diary_write.write("Date : " + str(self.diary_date))
            diary_write.write("\nBy " + self.diary_author)
            diary_write.write("\n" + self.diary_content)
            diary_write.write("\n-----------------------------------------------------------------")

    def read_diary(self):
        with open(self.file_name, 'r') as diary_read:
            read_lines = diary_read.readlines()
            for line in read_lines:
                print(line)
