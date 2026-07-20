file_obj = open("sample.txt", 'w')
string = """Hi hello
This is priya
Today's Topic is FileHandling"""
file_obj.write(string)
file_obj.close

## Opening file in write mode
file_obj = open("sample.txt", 'w')
string_list = ["welcome to File Handling\n", 
                 "This is write operation\n"]
file_obj.writelines(string_list)
file_obj.close()

## Opening file in read mode
try:
      file_obj = open("test.txt", 'w')
      data = file_obj.read()
      print(data)
except Exception as e:
      print(f"Something wrong: {e}")
finally:
      file_obj.close()

## Opening file using 'with' keyword
try:
     with open('sample.txt', 'r') as file_obj:
         data = file_obj.read()
         print(type(data))
         print(data)
except Exception as e:
   print(f"Something wrong: {e}")


