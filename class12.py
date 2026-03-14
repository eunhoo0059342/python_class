'''
<데이터타입>
4. 리스트 타입 [요소,요소,요소]
- 순서(인덱스, 숫자타입)
- 값을 추출 => 인덱싱 변수이름[인덱스]

5. 딕셔너리 {key:value,key:value,key:value}
- key(숫자, 문자열)-value(모든데이터타입다가능) 한쌍으로 이루어져있습니다.
- 순서(인덱스)가 없습니다.
- 값을 추출 => 변수이름[key]

'''

# 과자 이름과 가격을 매칭한 딕셔너리를 만들어보기 
# "홈럼볼" - 1200, "새우깡" - 1000원, "빈츠" - 2400
snack = {"홈런볼": 1200, "새우깡": 1000, "빈츠": 2400}
print(snack["홈런볼"])
# (1) 과자를 더 추가하고 싶어요 - 리스트에서는 리스트변수.append()
# 변수 값을 저장하는 '='  => 변수[새로운key]=새로운value 

# 예제) 빼빼로 1100원을 snack변수에 추가해주세요.
snack["빼빼로"] = 1100
print(snack)

# (2) key들만 뽑아보기 => 딕셔너리.keys()
print(list(snack.keys()))

# (3) value들만 뽑아보기 => 딕셔너리.values()
print(list(snack.values()))

# (4) key-value를 리스트형태로 뽑아보기 => 딕셔너리.items()
print(list(snack.items()))

# (5)딕셔너리의 반복 => 딕셔너리.items() 
# [,(),()]
# - snack
for k,v in snack.items():
    # k,v = (key,value)
    print(k,v)



# (심화) 다중 할당
# 여러개 데이터를 갖는 데이터타입을 사용해서 변수 여러개에 동시에 할당
# - 단, 요소의 갯수와 변수의 갯수는 일치해야합니다.
fruits=['apple','banana']
a = fruits[0]
b = fruits[1]

####
a,b= ['apple','banana']
print(a,b)



print("mission 1============")
# 중복되지 않는 ip를 가져오세요. 
reduced_log = [{'time': '1014', 'ip': '89.149.233.0', 'type': 'trade', 'item': 'wiz asset', 'price': 40000, 'res_code': 504}, {'time': '1508', 'ip': '89.149.233.20', 'type': 'trade', 'item': 'wiz asset', 'price': 45000, 'id': 'haha160'}, {'time': '1500', 'ip': '89.149.233.30', 'type': 'trade', 'item': 'wiz asset', 'price': 5000, 'id': 'son1257'}, {'time': '1048', 'ip': '89.149.233.3', 'type': 'trade', 'item': 'wiz asset', 'price': 5000, 'id': 'wyre97'}, {'time': '1353', 'ip': '89.149.233.48', 'type': 'trade', 'item': 'wiz asset', 'price': 5000, 'id': 'lala20'},{'time': '1510', 'ip': '89.149.233.30', 'type': 'trade', 'item': 'wiz asset', 'price': 6000, 'id': 'son1257'}, {'time': '1248', 'ip': '89.149.233.3', 'type': 'trade', 'item': 'wiz asset', 'price': 5000, 'id': 'wyre97'}, {'time': '1553', 'ip': '89.149.233.48', 'type': 'trade', 'item': 'wiz asset', 'price': 5000, 'id': 'lala20'}]
answer = []

for i in range(len(reduced_log)):
    # print(reduced_log[i])
    if reduced_log[i]["ip"] not in answer:
        answer.append(reduced_log[i]["ip"])
print(answer)

print("mission 2============")
# fpn_db 딕셔너리
# key(가짜 ip) - value(진짜 ip)

fpn_db = {'41.222.235.255':'41.93.255.255','154.65.127.255':'102.36.183.255','196.13.123.255':'196.13.175.255','102.38.191.255':'102.69.223.255','102.131.16.255':'102.69.247.255','102.223.173.255':'43.251.120.0','43.246.152.0':'43.247.104.0','27.117.192.0':'46.235.128.0','185.104.203.255':'185.110.39.255','93.114.189.255':'92.114.55.255','89.43.173.255':'89.42.175.255','	89.37.59.255':'85.204.192.255','212.77.31.255':'178.170.211.255','204.231.240.255':'37.203.199.255','109.234.103.255':'212.120.159.255','217.173.223.255':'185.217.20.0','185.176.128.0':'91.214.173.0','89.149.233.36':'218.155.162.150','89.149.233.0':'119.235.64.0','218.150.009.000':'218.150.980.709','45.221.240':'106.246.246.138','160.119.108':'164.160.255.255','45.222.191.255':'45.221.24.255','41.66.255.255':'196.43.242.255','196.43.225.255':'196.43.207.255','196.43.194.255':'196.201.2.255','41.189.191.255':'41.191.247.255','169.239.251.255':'192.251.202.255','193.108.23.255':'193.108.28.255','196.40.159.255':'196.201.5.255'}
answer2 = ""
for k, v in fpn_db.items():
    # print(k, v)
    for i in range(len(answer)):
        # print(answer[i])
        if k == answer[i]:
            print("가짜ip",k)
            print("진짜ip",fpn_db[k],v)
            answer2 = v

print("mission 3============")
# 첫번째 3글자 국자 그다음 세글자 위치
a = answer2.split(".")
print(a)
ip_map_country = {'121':'Guam','45':'Brazil','197':'Namibia','14':'Japan','185':'Spain','78':'France','103':'Singapol','119':'Netherlands','89':'Fiji island','91':'Bulgaria','14':'china','5':'Poland','45':'Philippines','77':'Finland','85':'Serbia','160':'Morocco','88':'Lithuania','46':'Armenia','199':'Switzerland','170':'Argentina','115':'Mongolia','23':'United States','200':'Mexico','5':'Russia','80':'Germany','109':'Island','196':'Cuba','41':'Kenya','185':'Czechoslovakia','14':'Australia','80':'Algeria','43':'Vietnam','103':'Laos'}
ip_map_address = {'121':'western donnie AVE-17','45':'Maureen plaza -70','197':'National Science Building-16','14':'East Lansing MI-4','185':'Memphis street-197','78':'Lauren Street_50','103':'Louis Mo-19','89':'William Street-5','235':'Upper Alma Road-9','91':'Parla AVE-80','14':'New sum Street-193','5':'Years building-8','45':'Phlia AVE-55','77':'Fin Street-90','85':'Serbia building-6','160':'Eckman horse Street-10','88':'Lith building-1002','46':'Ralph AVE-22','199':'Suite Street 179','170':'Argen AVE-66','115':'Mon von AVE-80','23':'United Sorborn building-78','200':'Ashford APT-27','5':'Cond Garden hills-8','80':'Luke Plaza-25','109':'Parlia Apt-103','196':'Cubanian Street-5','41':'Calle Amapolas Apt-105','185':'Czech AVE-72','14':'Del Mar Apt-26','80':'East Algeria Street-2','43':'Upper Julian AVE-26','103':'Maximilian Apt-8'}
print(ip_map_country[a[0]])
print(ip_map_address[a[1]])



# (과제)
# https://www.acmicpc.net/problem/11720
# https://www.acmicpc.net/problem/10808
