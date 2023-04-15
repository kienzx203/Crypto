
        #ĐỊNH DẠNG FORMAT
r='1: {one}, 2: {two}'.format(one=111, two=222)
print(r)
s='a: {1}, b: {2}, c: {0}'.format('one', 'two', 'three')
print(s)
#print(s)
#>>> '{:<10}'.format('aaaa') # căn lề trái
#'aaaa      '
#>>> '{:>10}'.format('aaaa') # căn lề phải
#'      aaaa'
#>>> '{:*>10}'.format('aaaa') # căn lề trái, thay thế khoảng trắng bằng kí tự *
#'******aaaa'
#>>> '{:*<10}'.format('aaaa') # căn lề phải, thay thế khoảng trắng bằng kí tự *
#'aaaa******'
#>>> '{:*^10}'.format('aaaa') # căn giữa, thay thế khoảng trắng bằng kí tự *
#'***aaaa***'
        # capitalize() có tác dụng viết hoa chữ cái đầu tiên của chuỗi và các chữ cái còn lại viết thường 
#vd:
#a='how kteam'
#b=a.capitalize()
#print(b)
        # upper() có tác dụng viết hoa tất cả các chữ
#a='how kteam'
#b=a.upper()
#print(b)
        # lower() có tác dụng viết thường tất cả các chữ
#a='how kteam'
#b=a.lower()
#print(b)
        # swapcase() có tác dụng viết thường tất cả các chữ
#a='how KTEam'
#b=a.swapcase()
#print(b)
        # title() có tác dụng viết hóa chữ cái đầu sau từng khoảng trắng
#a='how kteam'
#print(b)
        #Hàm center() có tác dụng căn lề ở giữa 30 ấy có nghĩa chuỗi có 30 kí tự
#a='Kteam'
#b=a.center(30,'*')
#print(b)
        #Hàm rjust() có tác dụng căn lề ở phải 30 ấy có nghĩa chuỗi có 30 kí tự
#a='Kteam'
#b=a.rjust(30,'*')
#print(b)
        #Hàm ljust() có tác dụng căn lề ở trái 30 ấy có nghĩa chuỗi có 30 kí tự
#a='Kteam'
#b=a.ljust(30,'*')
#print(b)
       #Hàm mã hóa
#a='Kien'
#b=a.encode(encoding='utf-8',errors='strict')
#print(b);
          #Hàm join
#a='kien pro ka'
#b=a.join(['1 ','2 ','3 '])
#print(b)
#(Output:1 kien pro ka2 kien pro ka3 )
        #Hàm thay thế kí tự
#a='có gì hót'
#b=a.replace('ó','kteam',1)
# 1 là số lần thay thế chữ ó
#print(b)
        #Hàm loại bỏ kí tự đầu và cuối khi ko gõ thì sẽ xóa khoảng trắng(Hàm strip())
#a='có gì hót'
#b=a.strip('t')
        #nếu 't'khác chữ kí đầu và cuối thì in ra str a không thay đổi
#print(b)
#chú ý lstrip cắt bên trái còn fstrip cắt bên phải
         #Hàm Split()có tác dúng tách kí tự từ trái qua còn hàm rsplit tách từ bên phải qua
#a='kien dep trai'
#b=a.split('(ghi kí tự) ',2)
#print(b)
        #Hàm partition() 
#a='how kteam free education'
#b=a.partition('ktea')
#print(b)
        #Hàm đếm số kí tự trong chuỗi
#a='how kteam free education'
#b=a.count('kteam',0,10)
#0,10 tìm số lượng từ vị trí chuỗi 0 đến 10 phần sau ko có cũng được nếu ko có thì sẽ đi full chuỗi
#print(b)
        #Hàm startswith trả về giá trị true false cho bt có kí tự trong chuỗi ko và phải bắt đầu kí tự số x là kí tự 'k' mới true
#a='how kteam free education'
#b=a.startswith('k',x,y)
#print(b)
# tương  tự hàm endswith () kiểm tra từ kí tự cuối chuỗi
        #Hàm find() đưa ra vị trí đầu tiên khi tìm chuỗi còn hàm rfind đưa ra vị trí đấu tiên tìm chuỗi từ phải qua
#a='how kteam free education'
#b=a.find('kteam')
#print(b)
        # Sự khác biệt index() và find() nếu ko tìm thấy kí tự find() đưa ra -1 còn index() sẽ báo lỗi
        # Hàm islower() kiểm tra chuỗi có viết thường hết hay không , isupper() kiểm tra coi viết Hoa hết hay không cả 2 hàm đều trả true false
        # Hàm isspace() kiểm tra chuỗi full khoảng trắng không trả về true false
#        Kiểu dữ liệu list
#+ giới hạn bởi các ngoặc vuông []
#+ các phần tử của list cách nhau bởi dấu phẩy ,
#+ Lít có khả năng chứa mọi giá trị đối tượng của python và bao gồm chính nó
# List rỗng: []
#EG:
#a = [[1,2,3],2,3]
#b=[i for i in range(30)]
#c=[[n,n*2,n*3] for n in range(1,4)]
#d=list('kteam')
#print(a)
#print(b)
#print(c)
#print(d)
# MỘT SỐ TOÁN TỬ TRONG LIST:List giống ma trận
#list ms cộng được vs list, chỉ được nhân list với một số 
 #EG:+toán tử cộng  
#a=[1,2]
#a=a+['one','two']
#print(a)
#a=[1,2,'a','b',[3,4]]
#b=a[1]
#print(b)
#nếu b=a[5] out:[3,4], nếu b=a[4][0] out:3
        #Muốn thây đổ phần tử list chỉ cần đưa ra và thay đổi
#c=a[2]
#a[2]='c'
#print(a) 
       #lưu ý không nên sữa chuỗi khi gán một biến vs list
# eg
# a=[1,2,3]
# b=a
# b[0]='kteam'
#print(a)
#print(b)
       #output:
# ['kteam', 2, 3]
# ['kteam', 2, 3] b[0] thay dổi khiến a[0] thay đổi vì những kiểu list là kiểu tham chiếu

        