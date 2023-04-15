# import os
# import glob

# fi = open("C:\\Users\\kin\\Downloads\\find.txt", 'w')
# l=[]
# for filepath in glob.glob(os.path.join("C:\\Users\\kin\\Downloads\\find_me\\New folder", '*.txt')):
#     with open(filepath) as f:
#         content = f.read()
#         str = " "
#         src = list(content.split(" "))
#         for i in range(len(src)):
#             if src[i] !='\n':
#                 str += chr(int(src[i]))
#         str += '\n'
#         l.append(str)
#     # print(l)
# fi.writelines(l)
# fi.close()
for i in range(0,10):
    print(i)