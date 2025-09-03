# 11. 이름, 나이, 전화번호로 구성된 연락처를 반복적으로 입력받아 저장하고 만약 이름이나 나이를 0을 입력하면 입력을 중단하고 입력받은 목록을 반환하는 함수와 입력 받은 연락처 목록을 받아 콘솔에 출력하는 함수 작성한 후 입력받아 출력하는 테스트 코드 작성
# 학번 : 202311398
# 작성자 : 문효원

def input_contact():
    contact_information = []

    while True:
        name = input("이름을 입력하세요 (종료: 0 입력): ")
        if name == "0":
            break
        age = input("나이를 입력하세요 (종료: 0 입력): ")
        if age == "0":
            break
        phone = input("전화번호를 입력하세요: ")
        
        contact = {"이름": name, "나이": int(age), "전화번호": phone}
        contact_information.append(contact) # append = 리스트 끝에 원소 추가
        
    return contact_information

def print_contact(contact_information):
    print("\n==== 연락처 목록 ====")
    for c in contact_information:  # c는 리스트 안의 딕셔너리 하나
        print("이름:", c['이름']) # C 언어에서는 c.name
        print("나이:", c['나이'])
        print("전화번호:", c['전화번호'])

contacts_list = input_contact()
print_contact(contacts_list)