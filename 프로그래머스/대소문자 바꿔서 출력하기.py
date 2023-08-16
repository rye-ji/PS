str = input()

if len(str) >= 1 and len(str) <= 20:    #제한 사항 준수

    changestr = ""      #빈 str 변수 지정

    for i in str:       #str의 한 글자씩 순서대로 i에 받기
        
        if i.isupper() == True:         #isupper는 대문자인지 여부 판단 #대문자가 맞다면
            changestr += i.lower()      #i를 소문자로 변환해서 changestr에 추가
        else:       #대문자가 아니라면 = 소문자가 맞다면
            changestr += i.upper()      #i를 대문자로 변환해서 changestr에 추가 
            
print(changestr)