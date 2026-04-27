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

