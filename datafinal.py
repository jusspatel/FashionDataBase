from tkinter import*
import sqlite3  
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.configure(bg="black")

conn= sqlite3.connect('address_book.db')

c= conn.cursor()

'''
c.execute("""CREATE TABLE addresses(
      first_name text,
      last_name text,
      adress text,
      city text,
      state text,
      zipcode integer
      )""")
'''
def save():
  conn= sqlite3.connect('address_book.db')
  

  c= conn.cursor()
  record_id=delete_box.get()
  c.execute("""UPDATE addresses SET
      first_name=:first,
      last_name=:last,
      adress=:address,
      city=:city,
      state=:state,
      zipcode=:zipcode
      WHERE oid=:oid""",
      {'first':f_name1.get(),
       'last':l_name1.get(),
       'address':add1.get(),
       'city':city1.get(),
       'state':state1.get(),
       'zipcode':zip1.get(),
       'oid':record_id
      


      })
  

  conn.commit()

  conn.close()
  root1.destroy()



def update():
  global root1
  root1=Tk()
  
  conn= sqlite3.connect('address_book.db')

  c= conn.cursor()
  record2= delete_box.get()
  
  c.execute("SELECT* FROM addresses WHERE oid=" + record2)
  records=c.fetchall()
  

  global f_name1
  global l_name1
  global add1
  global city1
  global state1
  global zip1
      
  #print(records)
  print_records=""
  for record in records:
      print_records += str(record[0])+", "+str(record[1])+ str(record[2])+" ,"+str(record[3])+", "+str(record[4])+", "+str(record[5])+"\n"
  f_name1= Entry(root1,width=30)
  f_name1.grid(row=0,column=1,padx=20)

  l_name1= Entry(root1,width=30)
  l_name1.grid(row=1,column=1)

  add1= Entry(root1,width=30)
  add1.grid(row=2,column=1)

  city1= Entry(root1,width=30)
  city1.grid(row=3,column=1)

  state1= Entry(root1,width=30)
  state1.grid(row=4,column=1)

  zip1= Entry(root1,width=30)
  zip1.grid(row=5,column=1)


  f_label1 = Label(root1, text="Product ID")
  f_label1.grid(row=0,column=0)

  l_label1 = Label(root1, text="Name")
  l_label1.grid(row=1,column=0)

  add_label1 = Label(root1, text="Brand")
  add_label1.grid(row=2,column=0)

  city_label1 = Label(root1, text="Gender")
  city_label1.grid(row=3,column=0)

  state_label1 = Label(root1, text="Season")
  state_label1.grid(row=4,column=0)

  zip_label1 = Label(root1, text="Price")
  zip_label1.grid(row=5,column=0)
  for record in records:
      f_name1.insert(0,record[0])
      l_name1.insert(0,record[1])
      add1.insert(0,record[2])
      city1.insert(0,record[3])
      state1.insert(0,record[4])
      zip1.insert(0,record[5])

  edit_btn=Button(root1,text="Save Records ",command=save).grid(row=6,column=0,columnspan=2,ipadx=50,pady=10)



def delete():
  
  conn= sqlite3.connect('address_book.db')

  c= conn.cursor()
  c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
  delete_box.delete(0,END)
  conn.commit()

  conn.close()


def submit():
    
  f1_name= f_name.get().strip()
  l1_name= l_name.get().strip()
  a1_name= add.get().strip()
  c1_name= city.get().strip()
  s1_name= state.get().strip()
  z1_name= zip.get().strip()
  if f1_name and l1_name and a1_name and c1_name and s1_name and z1_name :
      
        conn= sqlite3.connect('address_book.db')

        c= conn.cursor()
        c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:add,:city,:state,:zip)",
                {
                    'f_name':f_name.get(),
                    'l_name':l_name.get(),
                    'add':add.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'zip':zip.get()
                    

                })


        conn.commit()

        conn.close()

        f_name.delete(0,END)
        l_name.delete(0,END)
        add.delete(0,END)
        city.delete(0,END)
        state.delete(0,END)
        zip.delete(0,END)
  else: 
      messagebox.showwarning(title='Review Needed', message='Please complete all fieds.')                      
      

def problem():
  window=Tk()
  window.geometry("")
  window.resizable(False,False)
  conn= sqlite3.connect('address_book.db')

  c= conn.cursor()
  c.execute("SELECT* ,oid FROM addresses")
  records=c.fetchall()
  i=0
  tree= ttk.Treeview(window, column=("column1", "column2", "column3","column4","column5","column6","column7"), show='headings')
  tree.heading("#1", text="Product ID")
  tree.column("#1", minwidth=0, width=140, stretch=NO)
  tree.heading("#2", text="Name")
  tree.column("#2", minwidth=0, width=140, stretch=NO)
  tree.heading("#3", text="Brand")
  tree.column("#3", minwidth=0, width=140, stretch=NO)

  tree.heading("#4", text="Gender")
  tree.column("#4", minwidth=0, width=140, stretch=NO)

  tree.heading("#5", text="Season")
  tree.column("#5", minwidth=0, width=140, stretch=NO)

  tree.heading("#6", text="Price")
  tree.column("#6", minwidth=0, width=140, stretch=NO)

  tree.heading("#7", text="OID")
  tree.column("#7", minwidth=0, width=140, stretch=NO)

  tree.grid(row=12,column=0)
  '''for student in r_set: 
      for j in range(len(student)):
            e = Entry(window, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
  i=i+1'''
  #print(records)
  for record in records:
        tree.insert("",END,values=record)
  print_records=""
  '''for record in records:
      print_records += str(record[0])+" "+str(record[1])+" | "+ str(record[2])+" | "+str(record[3])+" | "+str(record[4])+" | "+str(record[5])+" | "+ "\t" + " | "+str(record[6])+" "+"\n\n"
  query_label=Label(window,text=print_records).grid(row=12,column=0,columnspan=2)
'''

  
  conn.commit()

  conn.close()
  
  

f_name= Entry(root,width=30, font="Helvetica 10 bold")
f_name.grid(row=0,column=1,padx=20)

l_name= Entry(root,width=30, font="Helvetica 10 bold")
l_name.grid(row=1,column=1)

add= Entry(root,width=30, font="Helvetica 10 bold")
add.grid(row=2,column=1)

city= Entry(root,width=30, font="Helvetica 10 bold")
city.grid(row=3,column=1)

state= Entry(root,width=30, font="Helvetica 10 bold")
state.grid(row=4,column=1)

zip= Entry(root,width=30, font="Helvetica 10 bold")
zip.grid(row=5,column=1)

delete_box= Entry(root,width="30", font="Helvetica 10 bold")
delete_box.grid(row=9,column=1)

f_label = Label(root, text="Product ID",bg="black",fg="white", font="Helvetica 10 bold")
f_label.grid(row=0,column=0)

l_label = Label(root, text="Name",bg="black",fg="white", font="Helvetica 10 bold")
l_label.grid(row=1,column=0)

add_label = Label(root, text="Brand",bg="black",fg="white", font="Helvetica 10 bold")
add_label.grid(row=2,column=0)

city_label = Label(root, text="Gender",bg="black",fg="white", font="Helvetica 10 bold")
city_label.grid(row=3,column=0)

state_label = Label(root, text="Season",bg="black",fg="white", font="Helvetica 10 bold")
state_label.grid(row=4,column=0)

zip_label = Label(root, text="Price",bg="black",fg="white", font="Helvetica 10 bold")
zip_label.grid(row=5,column=0)

delete_box_label=Label(root, text="Select OID",bg="black",fg="white", font="Helvetica 10 bold").grid(row=9,column=0)

dena_bhai = Button(root, text="Submit Records",command=submit).grid(row=6,column=0,pady=10,padx=10,ipadx=30,ipady=10) 
query=Button(root,text=" Show records",command=problem).grid(row=6,column=1,ipadx=30,pady=10,ipady=10)

delete_btn=Button(root,text=" Delete Records",command=delete).grid(row=10,column=0,ipadx=30,pady=10,ipady=10)

edit_btn=Button(root,text=" Update Records ",command=update).grid(row=10,column=1,ipadx=30,pady=10,ipady=10)



conn.commit()

conn.close()



root.mainloop()
