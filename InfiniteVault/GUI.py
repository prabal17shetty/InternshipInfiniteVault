from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import sys
import os
import pyodbc,subprocess
import shutil,re,listfiles,share
import main,startup,login,authentication


class share(share.Ui_MainWindow,QtWidgets.QMainWindow):
   def __init__(self):
       super(share, self).__init__()
       self.setupUi(self)
       self.share_button.clicked.connect(self.share)
       self.listWidget.currentItemChanged.connect(self.gettext)
       self.user=""
   def gettext(self):
       for index in range(self.listWidget.count()):
           self.user = self.listWidget.item(index).text()



   def view_known_user(self,user_id):

       conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                             'Server=LEGIONY730;'
                             'Database=UserDetails;'
                             'Trusted_Connection=yes;')
       cursor = conn.cursor()
       cursor.execute("select known_user_id from known_user_id_list where user_id='%s'"% (user_id ))
       user_list=[]
       for i in cursor:
           user_list.append(i[0])
       self.listWidget.addItems([str(i) for i in user_list])
       conn.commit()
   def share(self):

       if self.user:
           user_id=self.user
       else:
         user_id= self.receiver_use_id.text()
       index = fb.treeView.currentIndex()
       file_path = fb.model.filePath(index)
       conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                             'Server=LEGIONY730;'
                             'Database=UserDetails;'
                             'Trusted_Connection=yes;')
       cursor = conn.cursor()
       cursor.execute("if exists(select * from %s where %s='%s')select'true' els select 'false';" % ("known_user_id_list", "user_id", auth.directory_name))
       for i in cursor:
           status = i[0]
       conn.commit()
       if status == "false":
           cursor.execute("insert into %s(%s,%s)values('%s','%s')" % (
           "known_user_id_list", "user_id", "known_user_id", auth.directory_name,user_id))

       if user_id and file_path:
           temp_column=["receiver_user_id","file_path","senders_user_id"]
           temp_values=[user_id,file_path,auth.directory_name]
           columns = ', '.join(str(x) for x in temp_column)
           values = ', '.join("'"+str(x)+"'" for x in temp_values)
           insert_query = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("temp_store_files", columns, values)
           cursor.execute(insert_query)
           conn.commit()
       fb.populate(auth.directory_name)
       share.close()



class listfiles(listfiles.Ui_MainWindow,QtWidgets.QMainWindow):
   def __init__(self):
       super(listfiles, self).__init__()
       self.setupUi(self)
       self.show_result_btn.clicked.connect(self.view_result)
       self.listWidget.currentItemChanged.connect(self.opens)
       self.fil_names = []
       self.count=0

   def view_result(self):
       if self.count == 0:
           self.count = 1
           self.listWidget.addItems([str(i) for i in self.fil_names])

   def opens(self):


         for index in range(self.listWidget.count()):
             value=self.listWidget.item(index).text()
             file_path=re.findall("^F.*(D.*)",value)

         os.startfile(file_path[0 ])

class authenticate(authentication.Ui_MainWindow,QtWidgets.QMainWindow):
   def __init__(self):
       super(authenticate, self).__init__()
       self.setupUi(self)
       self.loginbutton.clicked.connect(self.login)

       self.googleloginbutton.clicked.connect(self.googlelogin)
   def login(self):
       conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                             'Server=LEGIONY730;'
                             'Database=UserDetails;'
                             'Trusted_Connection=yes;')

       self.userid = self.username_lineedit.text()
       if self.userid:
           self.directory_name = self.userid

       self.passwrd = self.password_lineedit.text()
       cursor = conn.cursor()
       cursor.execute('SELECT * FROM LoginDetails')
       for row in cursor:
           if row[0] == self.userid and row[1] == self.passwrd:

               if not os.path.isdir("D:/InternshipProject/" + self.directory_name):
                   os.mkdir("D:/InternshipProject/" + self.directory_name)
               auth.close()
               if not os.path.isdir("D:/InternshipProject/" +self.directory_name+"/"+self.directory_name):
                   os.mkdir("D:/InternshipProject/" +self.directory_name+"/"+self.directory_name)
               fb.populate(self.directory_name)
               fb.show()

   def googlelogin(self):

        auth.close()
        fb.show()

        temp = login.main(fb,auth)



        if temp:
            self.directory_name=temp


class start_up(startup.Ui_MainWindow,QtWidgets.QMainWindow):
   def __init__(self):
       super(start_up, self).__init__()
       self.setupUi(self)
       self.nextbutton.clicked.connect(self.nextpage)


   def nextpage(self):

        start.close()

        auth.show()


class file(main.Ui_MainWindow,QtWidgets.QMainWindow):
   def __init__(self):
       super(file, self).__init__()
       self.setupUi(self)
       self.exitbutton.clicked.connect(self.prints)
       self.createbutton.clicked.connect(self.create_folder)
       self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
       self.treeView.customContextMenuRequested.connect(self.context_menu)
       self.deletebutton.clicked.connect(self.delete_folder)
       self.logoutbutton.clicked.connect(self.logout)
       self.browsebutton.clicked.connect(self.browse)
       self.searchbutton.clicked.connect(self.search)


   def update_combobox(self,DirectoryName):
       self.typeselectcombobox.close()
       self.typeselectcombobox = QtWidgets.QComboBox(self.frame)
       self.typeselectcombobox.setGeometry(QtCore.QRect(740, 340, 191, 22))
       self.typeselectcombobox.setObjectName("comboBox")
       self.conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                             'Server=LEGIONY730;'
                             'Database=UserDetails;'
                             'Trusted_Connection=yes;')
       items = [" "]
       self.AvailableFileTypes = []
       self.cursor = self.conn.cursor()
       self.cursor.execute("select file_type from file_types where directory_name='"+DirectoryName+"';")
       for i in self.cursor:
           items.append(i[0])
           self.AvailableFileTypes.append(i[0])
       self.conn.commit()

       self.typeselectcombobox.addItems(items)
       self.typeselectcombobox.show()

   def search(self):
       filename = self.searchlineedit.text()
       fil_ext = self.typeselectcombobox.currentText()
       for i in self.AvailableFileTypes:

           try:
               self.cursor.execute(
                   "select FileName,file_location from %s where FileName='%s' or FileTypeExtension='%s';" % (
                   i + "_file_metadata", filename + "." + i, fil_ext))
               for i in self.cursor:
                   listfiles.fil_names.append("File Name:  " + i[0] + "       located path: " + i[1].replace('_', '/'))
                   self.conn.commit()
           except:
               pass

       listfiles.show()


   def browse(self):
       index = self.treeView.currentIndex()
       file_path = str(self.model.filePath(index))
       url = QtWidgets.QFileDialog.getOpenFileUrl(self)
       file_loc = (re.findall("///(.*)[']", str(url[0])))

       temp = file_loc[0][::-1]
       temp1 = ""
       for i in temp:
           if i == "/":
               break
           else:
               temp1 = (temp1 + i)
       file_name= temp1[::-1]
       if file_path == "":
          shutil.copy(file_loc[0], "D:/InternshipProject/" + auth.directory_name)
          fb.populate(auth.directory_name)
       else:
          shutil.copy(file_loc[0], file_path)
          fb.populate(auth.directory_name)


       input_file = file_loc[0]
       exe = "C:/Users/Prabal Shetty/PycharmProjects/InternshipP1/exiftool.exe"
       process = subprocess.Popen([exe, input_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
       list_dict = []
       for output in process.stdout:
           line = output.strip().split(":")
           info = {line[0].strip(): line[1].strip()}
           list_dict.append(info)
       meta_data = {}
       for dictionary in list_dict:
           for key, val in dictionary.items():
               meta_data[key.replace(' ', '')] = val

       if file_path == "":
           meta_data["file_location"] = "D:/InternshipProject/"+auth.directory_name +"/" + file_name
           meta_data["user_id"] = auth.directory_name
       else:
           meta_data["file_location"] = file_path + "/" + file_name
           meta_data["user_id"] = auth.directory_name


       conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                             'Server=LEGIONY730;'
                             'Database=UserDetails;'
                             'Trusted_Connection=yes;')
       cursor = conn.cursor()
       for key, val in meta_data.items():
           if key == "FileTypeExtension":

               columns = ', '.join("" + str(x).replace('/', '_') + "" for x in meta_data.keys())
               values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in meta_data.values())
               table_columns = ', '.join("" + str(x + " " + "varchar(MAX)").replace('/', '_') + "" for x in meta_data.keys())
               create_query = "CREATE TABLE %s ( %s );" % (val + "_file_metadata", table_columns)
               insert_query = "INSERT INTO %s ( %s ) VALUES ( %s );" % (val + "_file_metadata", columns, values)

               temp_filetype_columns = ['directory_name', 'file_type']
               temp_filetype_value = [auth.directory_name, meta_data["FileTypeExtension"]]
               filetype_columns = ', '.join(str(x) for x in temp_filetype_columns)
               filetype_value = ', '.join("'" + str(x) + "'" for x in temp_filetype_value)
               file_type_insert_query = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("file_types", filetype_columns, filetype_value)




               try:
                   cursor.execute(create_query)
                   conn.commit()
                   cursor.execute(insert_query)
                   conn.commit()

                   query = "IF exists (SELECT * FROM %s where user_id='%s' and FileTypeExtension='%s') select 'true' ELSE select 'false';" % (val + "_file_metadata", auth.directory_name, meta_data["FileTypeExtension"])
                   cursor.execute(query)
                   temp = str(cursor.fetchall()[0])
                   conn.commit()


                   if re.findall(".*'(.*)'.*", temp)[0] == "true":
                       try:

                           cursor.execute(
                               "if exists(select * from file_types where file_type='%s'and directory_name='%s') select 'true' else select 'false'" % (meta_data["FileTypeExtension"], auth.directory_name))
                           conn.commit()
                           status=str(cursor.fetchall()[0])


                           if re.findall(".*'(.*)'.*", status)[0] == "false":

                               cursor.execute(file_type_insert_query)
                               conn.commit()

                       except:
                           pass

                   else:
                       pass


               except:
                   cursor.execute(insert_query)
                   conn.commit()


                   query = "IF exists (SELECT * FROM %s where user_id='%s' and FileTypeExtension='%s') select 'true' ELSE select 'false';" % (val + "_file_metadata", auth.directory_name, meta_data["FileTypeExtension"])
                   cursor.execute(query)
                   temp = str(cursor.fetchall()[0])
                   conn.commit()


                   if re.findall(".*'(.*)'.*", temp)[0] == "true":
                       try:


                           cursor.execute(
                               "if exists(select * from file_types where file_type='%s'and directory_name='%s') select 'true' else select 'false'" % (
                               meta_data["FileTypeExtension"], auth.directory_name))
                           conn.commit()

                           status = str(cursor.fetchall()[0])
                           if re.findall(".*'(.*)'.*", status)[0] == "false":

                               cursor.execute(file_type_insert_query)
                               conn.commit()
                       except:
                           pass

                   else:
                       pass
       self.update_combobox(auth.directory_name)

   def logout(self):
       if os.path.exists("C:/Users/Prabal Shetty/PycharmProjects/InternshipP1/token.pickle"):
            os.remove("C:/Users/Prabal Shetty/PycharmProjects/InternshipP1/token.pickle")
       fb.close()
       auth.show()


   def populate(self,directory_name):
       self.update_combobox(directory_name)
       self.path = "D:/InternshipProject/"+ directory_name
       self.model = QtWidgets.QFileSystemModel()
       self.model.setRootPath((QtCore.QDir.rootPath()))
       self.treeView.setModel(self.model)
       self.treeView.setRootIndex(self.model.index(self.path))

   def context_menu(self):
       menu = QtWidgets.QMenu()
       open = menu.addAction("Open")
       share = menu.addAction("Share")
       share.triggered.connect(self.share)
       open.triggered.connect(self.open_file)
       cursor = QtGui.QCursor()
       menu.exec_(cursor.pos())

   def open_file(self):
       index = self.treeView.currentIndex()
       file_path = self.model.filePath(index)
       os.startfile(file_path)

   def share(self):

       print(auth.directory_name)
       share.view_known_user(auth.directory_name)
       share.show()

   def create_folder(self):
       try:
            self.fname=self.foldername.text()
            index = self.treeView.currentIndex()
            file_path = self.model.filePath(index)
            if file_path =="":

                 os.mkdir("D://InternshipProject" +"//"+ auth.directory_name + "//"+self.fname)
                 print("Folder Created!!")
                 self.print_fname()
                 fb.populate(auth.directory_name)

            else:

                os.mkdir(file_path+"//" + self.fname)
                print("Folder Created!")
                self.print_fname()
                fb.populate(auth.directory_name)



       except:
              self.popup("File/Folder already exists! OR enter a new file name")
       fb.populate(auth.directory_name)

   def delete_folder(self):
       conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                             'Server=LEGIONY730;'
                             'Database=UserDetails;'
                             'Trusted_Connection=yes;')
       cursor = conn.cursor()
       try:
           index = self.treeView.currentIndex()
           file_path = self.model.filePath(index)
           if file_path=="D:/InternshipProject"+auth.directory_name:
               try:
                   choice = QtWidgets.QMessageBox.question(self, "Alert!","Confirm Delete", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                   if choice == QtWidgets.QMessageBox.Yes:
                       os.removedirs("D:/InternshipProject/"+auth.directory_name+"/"+self.model.fileName(index))

                       table_name = os.path.splitext("D:/InternshipProject/" + auth.directory_name + "/" + self.model.fileName(index))[1][1:] + "_file_metadata"
                       f_l = "D:/InternshipProject/" + auth.directory_name + "/" + self.model.fileName(index)
                       cursor.execute("select %s from %s where file_location='%s';" % ("FileTypeExtension", table_name, f_l.replace('/', '_')))
                       fileextension = ""
                       for i in cursor:
                           fileextension = i[0]
                       conn.commit()
                       query = "IF exists (SELECT * FROM %s where user_id='%s' and FileTypeExtension='%s') select 'true' ELSE select 'false';" % (fileextension + "_file_metadata", auth.directory_name, fileextension)
                       file_type_delete_query = "delete from %s where  file_type='%s' and directory_name='%s';" % ("file_types", fileextension, auth.directory_name)
                       cursor.execute("delete from %s where file_location='%s';" % (table_name, f_l.replace('/', '_')))
                       conn.commit()
                       cursor.execute(query)
                       temp = str(cursor.fetchall()[0])
                       check = re.findall(".*'(.*)'.*", temp)[0]
                       conn.commit()
                       if check == "false":
                           try:
                               cursor.execute(file_type_delete_query)
                               conn.commit()
                           except:
                               pass


                       print("Folder Deleted!")
                       QtWidgets.QMessageBox.close()
                   elif choice == QtWidgets.QMessageBox.No:
                       QtWidgets.QMessageBox.close()
               except Exception as e:
                   self.popup(e)
           else:
               if file_path == "":
                   self.popup("Select the folder to be deleted")
               else:
                   choice = QtWidgets.QMessageBox.question(self, "Alert!", "Confirm Delete",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                   if choice == QtWidgets.QMessageBox.Yes:
                       if file_path=="D:/InternshipProject/" +auth.directory_name+"/"+auth.directory_name:
                           self.popup("Delete action denied for default user folder!")
                       else:
                         shutil.rmtree(file_path)
                         os.rmdir(file_path)

                         table_name = os.path.splitext(file_path)[1][1:] + "_file_metadata"
                         cursor.execute("select %s from %s where file_location='%s';" % ("FileTypeExtension", table_name, file_path.replace('/', '_')))
                         fileextension = ""
                         for i in cursor:
                             fileextension = i[0]
                         conn.commit()
                         query = "IF exists (SELECT * FROM %s where user_id='%s' and FileTypeExtension='%s') select 'true' ELSE select 'false';" % (fileextension + "_file_metadata", auth.directory_name, fileextension)
                         file_type_delete_query = "delete from %s where  file_type='%s' and directory_name='%s';" % ("file_types", fileextension, auth.directory_name)
                         cursor.execute("delete from %s where file_location='%s';" % (table_name, file_path.replace('/', '_')))
                         conn.commit()
                         cursor.execute(query)
                         temp = str(cursor.fetchall()[0])
                         check = re.findall(".*'(.*)'.*", temp)[0]
                         conn.commit()
                         if check == "false":
                             try:
                                 cursor.execute(file_type_delete_query)
                                 conn.commit()
                             except:
                                 pass

                         QtWidgets.QMessageBox.close()
                         print("Folder Deleted!")
                         fb.populate(auth.directory_name)




                   elif choice == QtWidgets.QMessageBox.No:
                       QtWidgets.QMessageBox.close()
       except:
           try:
               file_path = self.model.filePath(index)
               os.remove(file_path)
               table_name = os.path.splitext(file_path)[1][1:] + "_file_metadata"
               cursor.execute("select %s from %s where file_location='%s';" % ("FileTypeExtension", table_name, file_path.replace('/', '_')))
               fileextension = ""
               for i in cursor:
                   fileextension = i[0]
               conn.commit()
               query = "IF exists(SELECT * FROM %s where user_id='%s' and FileTypeExtension='%s') select 'true' ELSE select 'false';" % (fileextension + "_file_metadata",auth.directory_name, fileextension)
               file_type_delete_query = "delete from %s where file_type='%s' and directory_name='%s';" % ("file_types", fileextension, auth.directory_name)
               cursor.execute("delete from %s where file_location='%s';" % (table_name, file_path.replace('/', '_')))
               conn.commit()
               cursor.execute(query)
               temp = str(cursor.fetchall()[0])
               check = re.findall(".*'(.*)'.*", temp)[0]
               conn.commit()
               if check == "false":
                   try:
                       cursor.execute(file_type_delete_query)
                       conn.commit()
                   except:
                       pass



           except Exception as e:
               self.popup(e)
       fb.populate(auth.directory_name)

   def prints(self):
       print("You just closed the directory tree view!")
       sys.exit()

   def print_fname(self):
       self.fname=self.foldername.text()
       print("Folder is in "+self.path +" and the name of the folder is "+self.fname)

   def popup(self, e):
       try:
           choice = QtWidgets.QMessageBox.question(self, "Alert!", e, QtWidgets.QMessageBox.Ok)
           if choice == QtWidgets.QMessageBox.Ok:
               QtWidgets.QMessageBox.close()
       except:
           pass


if __name__=='__main__':

   app = QtWidgets.QApplication(sys.argv)
   listfiles=listfiles()
   fb = file()
   share=share()
   start=start_up()
   auth = authenticate()
   start.show()
   sys.exit(app.exec_())








