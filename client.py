import app
import time
import mail
import main


class Client:

    def __init__(self):
        self.prev_content = app.collect_content()
        time.sleep(300)
        self.content = app.collect_content()
        self.html_content = app.return_table()

        if self.content != self.prev_content:
            self.update()
        else:
            self.no_update()

    def update(self):

        change_dic = {0: "Corona confirmed number(India)", 1: "Corona confirmed number(Foreign)",
                      2: "Corona cured number", 3: "Corona death number"}

        changed_fields = Client.difference(self.prev_content, self.content)
        changed_states = []
        changed_message = []

        for i in range(len(changed_fields) // 2):
            changed_states.append(changed_fields[i][0])

            for j in range(len(changed_fields[i])):
                if changed_fields[i][j] != changed_fields[i + len(changed_fields) // 2][j]:
                    changed_message.append(
                        f'In {changed_states[i]}, {change_dic[j - 1]} is changed from {changed_fields[i + 1][j]} to {changed_fields[i][j]}.')
        
        mail.create_mail(self.html_content, changed_message, main.name_email()[0],main.name_email()[1])
        self.__init__()

    def no_update(self):
        print("No updates-> No mail sent")
        self.__init__()

    def difference(list1, list2):
        list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
        return list_dif
