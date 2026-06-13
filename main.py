# 파일이름 : 신용등급 판독기
# 작 성 자 : 간민준
# [4단계: 함수] - 등급 판정 로직을 함수로 분리하여 관리
def get_credit_grade(score):
    if score >= 900:
        return "1등급 (우량)"
    elif score >= 700:
        return "2등급 (일반)"
    elif score >= 500:
        return "3등급 (주의)"
    else:
        return "저신용 (관리대상)"

# [4단계: 리스트/배열] - 고객 데이터를 담을 데이터 주머니
customer_list = []

print("="*40)
print("🏦 스마트 신용 등급 관리 시스템 V1.0")
print("="*40)

# [3단계: 반복문/메뉴] - 업무 종료 전까지 무한 반복
while True:
    print("\n[메뉴 선택]")
    print("1. 신규 고객 정보 등록")
    print("2. 최종 신용 점수 산출 및 등급 확인")
    print("3. VVIP 특별 칭호 및 혜택 확인")
    print("4. 대출 적격성 자동 심사")
    print("5. 전체 고객 데이터 명부 출력")
    print("6. 고객 정보 검색")
    print("0. 시스템 업무 종료")
    
    choice = input("\n원하는 서비스 번호를 입력하세요: ")

    if choice == '1':
        # [1단계: 변수/입출력] - 데이터 수집
        name = input("고객명: ")
        salary = int(input("연봉 (단위: 만원): "))
        debt = int(input("부채 총액 (단위: 만원): "))
        overdue = int(input("연체 횟수 (회): "))
        
        # 2단계 준비: 점수 계산을 위한 임시 저장
        # (기본 500점에서 연봉 높으면 +, 부채/연체 많으면 -)
        score = 500 + (salary // 100) - (debt // 50) - (overdue * 50)
        if score > 1000: score = 1000
        if score < 0: score = 0
        
        # [4단계: 리스트 저장] - 정보를 딕셔너리 형태로 묶어서 저장
        customer = {
            "name": name,
            "salary": salary,
            "debt": debt,
            "overdue": overdue,
            "score": score,
            "grade": get_credit_grade(score)
        }
        customer_list.append(customer)
        print(f"\n✅ {name} 고객님 등록이 완료되었습니다.")

    elif choice == '2':
        if not customer_list:
            print("❌ 등록된 고객이 없습니다.")
            continue
        curr = customer_list[-1]  # 가장 최근 등록된 고객
        print(f"\n🔍 {curr['name']}님의 최종 신용 점수: {curr['score']}점")
        print(f"📊 신용 등급: {curr['grade']}")

    elif choice == '3':
        if not customer_list:
            print("❌ 등록된 고객이 없습니다.")
            continue
        curr = customer_list[-1]
        # [2단계: 복합 조건문] - VVIP 판정
        if curr['salary'] >= 8000 and curr['overdue'] == 0:
            print(f"✨ [특보] {curr['name']}님은 '금융 마스터' 칭호 부여 대상입니다!")
            print("💰 혜택: 대출 한도 200% 상향 조정")
        else:
            print("ℹ️ 해당 고객은 VVIP 대상자가 아닙니다.")

    elif choice == '4':
        if not customer_list:
            print("❌ 등록된 고객이 없습니다.")
            continue
        curr = customer_list[-1]
        # 부채 비율이 연봉의 2배 미만이고 3등급 이상일 때 적격
        if curr['debt'] < curr['salary'] * 2 and "저신용" not in curr['grade']:
            print(f"✅ {curr['name']}님은 대출 승인 [적격] 판정입니다.")
        else:
            print(f"❌ {curr['name']}님은 대출 승인 [거절] 판정입니다.")

    elif choice == '5':
        print("\n" + "="*50)
        print(f"{'이름':^10} | {'점수':^6} | {'등급':^12} | {'비고'}")
        print("-" * 50)
        for c in customer_list:
            print(f"{c['name']:^10} | {c['score']:^6} | {c['grade']:^12} | {c['salary']}만원")
        print("="*50)

    elif choice == '6':
        search_name = input("검색할 고객 이름을 입력하세요: ")
        found = False
        for c in customer_list:
            if c['name'] == search_name:
                print(f"\n[검색 결과] {c['name']}님: {c['score']}점 / {c['grade']}")
                found = True
        if not found:
            print("❌ 해당 이름의 고객을 찾을 수 없습니다.")

    elif choice == '0':
        print("🚀 시스템을 종료합니다. 이용해 주셔서 감사합니다.")
        break

    else:
        print("⚠️ 잘못된 번호입니다. 다시 선택해 주세요.")



2차과제
print('='*50)
print(' [스마트 금융 시스템: 신용등급 찬독기] ')
print('='*50)

customer_basic_data = []
prompts = ['고객님의 성함을 입력하세요:' , ' 현재  연봉을 입력허세요'(단위: 만원): ', '보유 부체를 입력하세요(단위: 만원): ']

for i in range(len(prompts)):
    data = input(prompts[i])
    customer_basic_data.append(data)

name = customer_basic_data[0]
salery = float(customer_basicdata[1])
debt = float(customer_basic_data[2])
overdue_count = int(input('지난해 연체 횟수를 입력하시오: ')
base_score = 500.0

total_score = base_score
total_score += (salary * 0.1)
total_score -= (debt * 0.05)
total_score -= (overdue_count * 50)

score_analysis = [salary, debt, total_score]
score_analysis.insert(0, 100.0)
data_len = len(socre_analysis)
max_value = max(score_analyiss)
socre_analysis.sort(reverse = True)
print('\n' + '-'*20 + '판독결과' + '-'*20)

if total_score >= 900:
    grade = '1등급 (우량)'
    if slary >= 10000 and overdue_cont == 0:
        title = 'vvip마스터'
        benefit = '특별한도 상향 및 전담 매니저배치')
    else:
        title = '일반 우량 고객'
        benefit = '대출 금리 인하 혜택'
elif total_score >= 600:
    grade = '3등급(보통)'
else:
    grade = '5등급 (주의)'
    title = '성실 상황 고객'
    benefit = '대출 금리 인하 혜택'
else:
    grade = '5등급'
    title = '관리 대상 고객')
    benefit = '금융 교육 이수 권고'

print(f'고객성함: {name}')
print(f' 산출점슈: {total_score: .2f}점')
print(f' 신용등급: {grade}')
print(f' 부여칭호: [{title}]')
print(f' 특별혜택: {benefit}')

print('-'*50*)
print(f'시스템 로그: 데이터 {data_lenn}개 처리 완료 / 최고 수치 -: {max_vlaue}')
print('='*50)

# [2026-01] 나만의 파이썬 소프트웨어 개발 프로젝트
# 프로그램명: 신용등급 판독 시스템 V4.0 (🌟최종 완성형: 모듈화 및 데이터 확장)

# [데이터 확장] 전체 고객 데이터를 누적 저장할 데이터 주머니 (전역 변수)
customer_db = []


def register_customer():
    """
    [함수 1] 신규 고객의 기본 금융 데이터를 입력받는 함수
    """
    print("[안내] 신규 고객 금융 데이터를 등록합니다.")
    
    # for문을 사용한 기본 데이터 입력 (과제 요구사항 유지)
    customer_basic_data = []
    prompts = ["고객 성함: ", "현재 연봉(만원): ", "보유 부채(만원): "]
    for i in range(len(prompts)):
        data = input(prompts[i])
        customer_basic_data.append(data)
        
    name = customer_basic_data[0]
    salary = float(customer_basic_data[1])
    debt = float(customer_basic_data[2])
    overdue_count = int(input("지난해 연체 횟수: "))
    
    return name, salary, debt, overdue_count


def calculate_credit_score(salary, debt, overdue_count):
    """
    [함수 2] 입력받은 데이터를 금융 가중치 공식에 대입하여 점수, 등급, 칭호를 산출하는 함수
    """
    base_score = 500.0
    total_score = base_score + (salary * 0.1) - (debt * 0.05) - (overdue_count * 50)
    
    # [제어구조] 연속 및 중첩 if문을 활용한 등급/칭호 판정
    if total_score >= 900:
        grade = "1등급"
        if salary >= 10000 and overdue_count == 0:
            title = "VVIP 마스터"
        else:
            title = "일반 우량 고객"
    elif total_score >= 600:
        grade = "3등급"
        title = "성실 상환 고객"
    else:
        grade = "5등급"
        title = "관리 대상 고객"
        
    return total_score, grade, title


def add_to_database(name, salary, debt, overdue_count, total_score, grade, title):
    """
    [함수 3] 산출된 데이터를 딕셔너리 구조로 확장하여 데이터베이스(customer_db)에 추가하는 함수
    """
    global customer_db  # 전역 변수 참조 설정
    
    # [데이터 확장] 가독성을 높이기 위해 리스트 대신 딕셔너리(Key-Value) 구조 활용
    customer_profile = {
        "name": name,
        "salary": salary,
        "debt": debt,
        "overdue": overdue_count,
        "score": total_score,
        "grade": grade,
        "title": title
    }
    customer_db.append(customer_profile)
    print(f"\n[완료] {name} 고객님의 등급 판독이 완료되어 시스템에 기록되었습니다.")
    print(f"▶ 신용 점수: {total_score:.2f}점 | 등급: {grade} | 칭호: [{title}]")


def print_all_customers():
    """
    [함수 4] 등록된 전체 고객의 명부를 조회하는 함수
    """
    global customer_db
    print("[안내] 시스템에 등록된 전체 고객 명부입니다.")
    
    # 방어적 프로그래밍 (데이터 유무 확인)
    if len(customer_db) == 0:
        print("※ 현재 등록된 고객 데이터가 없습니다. 먼저 등록을 진행해 주세요.")
        return
        
    print(f"현재 등록 총원: {len(customer_db)}명")
    print("-"*50)
    
    # for문과 딕셔너리 Key를 활용한 정교한 순회 출력
    for idx, cust in enumerate(customer_db, start=1):
        print(f"[{idx}] 이름: {cust['name']} | 연봉: {cust['salary']}만 원 | 점수: {cust['score']:.2f}점 | 등급: {cust['grade']} ({cust['title']})")


def search_customer():
    """
    [함수 5] 특정 고객의 이름을 검색하여 상세 정보를 출력하는 함수
    """
    global customer_db
    print("[안내] 특정 고객의 신용 정보를 조회합니다.")
    
    if len(customer_db) == 0:
        print("※ 데이터베이스가 비어 있습니다.")
        return
        
    search_name = input("검색할 고객의 이름을 정확히 입력하세요: ")
    found = False  # 검색 플래그 변수
    
    for cust in customer_db:
        if cust["name"] == search_name:  # 관계 연산자 사용
            print(f"\n[검색 성공] {search_name} 고객님의 상세 금융 정보")
            print(f"· 현재 연봉: {cust['salary']}만 원")
            print(f"· 보유 부채: {cust['debt']}만 원")
            print(f"· 연체 횟수: {cust['overdue']}회")
            print(f"· 신용 점수: {cust['score']:.2f}점")
            print(f"· 최종 등급: {cust['grade']} [{cust['title']}]")
            found = True
            break
            
    if not found:  # 논리 연산자 사용
        print(f"※ [{search_name}] 이름으로 등록된 고객을 찾을 수 없습니다.")


# ========================================================
# 메인 실행 제어부 (무한 루프 & 메뉴 시스템)
# ========================================================
while True:
    print("\n" + "="*50)
    print("     [스마트 금융 시스템: 신용등급 판독기 v4.0]     ")
    print("="*50)
    print(" 1. 신규 고객 정보 등록 및 등급 판독")
    print(" 2. 전체 등록 고객 명부 조회")
    print(" 3. 특정 고객 정보 검색")
    print(" 5. 시스템 업무 종료")
    print("="*50)
    
    menu = input("원하시는 업무의 번호를 선택하세요: ")
    print("-"*50)
    
    if menu == "1":
        # 1. 입력 함수 호출
        name, salary, debt, overdue_count = register_customer()
        # 2. 연산 및 판정 함수 호출
        total_score, grade, title = calculate_credit_score(salary, debt, overdue_count)
        # 3. 데이터베이스 저장 함수 호출
        add_to_database(name, salary, debt, overdue_count, total_score, grade, title)
        
    elif menu == "2":
        # 전체 명부 출력 함수 호출
        print_all_customers()
        
    elif menu == "3":
        # 특정 고객 검색 함수 호출
        search_customer()
        
    elif menu == "5":
        print("[안내] 신용등급 판독 시스템 업무를 안전하게 종료합니다.")
        print("이용해 주셔서 감사합니다.")
        break  # 무한 루프 완전히 탈출
        
    else:
        print("※ 잘못된 번호입니다. 메뉴판(1, 2, 3, 5)의 번호 중 하나를 입력해 주세요.")
