'''
-LLM 코드 리뷰 및 개선 보고서 작성하기
다음 과제 문제를 LLM에 입력하고 첫 번째 출력 코드를 수정하지 않은 채로 레퍼런스 코드로 저장하시오.
이후 직접 코드를 실행해보고 오류가 발생한다면 직접 오류 분석 및 오류 해결, 개선점이 있을 시 개선 가능성을 분석한
뒤 요구사항을 모두 만족할 수 있도록 코드를 개선하시오.
제출 목록
1. LLM 입력 프롬프트
2. 프롬프트 입력 후 LLM 첫 출력 코드 (.py 형태)
3. 오류 및 개선점 분석
4. 개선한 코드 (.py)
5. LLM 프롬프트 입력 단계부터 오류 개선까지의 고찰
보고서 형식은 pdf로 작성하고 레퍼런스 코드, 개선 코드를 함께 압축하여 제출

LLM 입력 문제 : 명령어 기반 도서 대출 관리 시스템

add 책이름 수량
- 책 등록, 이미 있으면 수량 추가
borrow 사용자 책이름
- 책이 있고 수량이 남아 있으며, 같은 사용자가 같은 책을 대출 중이 아닐 때만 대출
- 실패 시 ERROR + 사유 출력
return 사용자 책이름
- 실제로 대출 중인 책만 반납 가능
- 실패 시 ERROR + 사유 출력
status 책이름
- 남은 수량 출력
- 책이 존재하지 않으면 ERROR 출력
user 사용자
- 사용자의 대출 목록 출력
- 없으면 EMPTY
list
- 전체 책 목록을 등록 순서대로 출력
Exit
- 종료

조건:
• 책과 사용자 이름에는 공백 없음
• 수량은 0 이상의 정수
• 잘못된 명령어 형식은 ERROR
• eval() 사용 금지
• 함수로 기능 분리
'''
class LibrarySystem:
    def __init__(self):
        # 도서 목록을 저장하는 딕셔너리 (책제목: 남은수량)
        # Python 3.7+부터 딕셔너리는 삽입 순서를 유지하므로 list 명령어 시 등록 순서대로 출력 가능합니다.
        self.books = {}
        # 사용자별 대출 목록을 저장하는 딕셔너리 (사용자: [대출한 책제목 리스트])
        self.users = {}

    def add_book(self, title, quantity_str):
        # 수량이 0 이상의 정수인지 확인 (isdigit()은 음수나 소수를 False로 처리)
        if not quantity_str.isdigit():
            print("ERROR: 수량은 0 이상의 정수여야 합니다.")
            return
        
        quantity = int(quantity_str)
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"[성공] '{title}' 도서가 {quantity}권 추가되었습니다. (현재 총 {self.books[title]}권)")

    def borrow_book(self, user, title):
        if title not in self.books:
            print("ERROR: 해당 도서관에 존재하지 않는 도서입니다.")
            return
        
        # 사용자가 대출 기록이 없으면 빈 리스트 생성
        if user not in self.users:
            self.users[user] = []

        if title in self.users[user]:
            print("ERROR: 동일한 책을 대출 중입니다.")
            return
            
        if self.books[title] <= 0:
            print("ERROR: 남아있는 책 재고가 없습니다.")
            return

        # 대출 처리
        self.books[title] -= 1
        self.users[user].append(title)
        print(f"[성공] {user}님이 '{title}' 도서를 대출하셨습니다.")

    def return_book(self, user, title):
        if title not in self.books:
            print("ERROR: 해당 도서관에 존재하지 않는 도서입니다.")
            return
            
        if user not in self.users or title not in self.users[user]:
            print("ERROR: 대출 중이 아닌 책입니다.")
            return

        # 반납 처리
        self.books[title] += 1
        self.users[user].remove(title)
        print(f"[성공] {user}님이 '{title}' 도서를 반납하셨습니다.")

    def status_book(self, title):
        if title not in self.books:
            print("ERROR: 해당 도서관에 존재하지 않는 도서입니다.")
            return
        
        print(f"[{title}] 남은 수량: {self.books[title]}")

    def user_info(self, user):
        if user not in self.users or not self.users[user]:
            print("EMPTY")
            return
            
        print(f"[{user}님의 대출 목록]")
        for book in self.users[user]:
            print(f"- {book}")

    def list_books(self):
        if not self.books:
            print("EMPTY")
            return
            
        print("[전체 도서 목록]")
        for title, quantity in self.books.items():
            print(f"- {title}: {quantity}권")


def main():
    library = LibrarySystem()
    print("=== 도서 대출 관리 시스템을 시작합니다 (종료: exit) ===")
    
    while True:
        command_line = input("\n명령어를 입력하세요: ").strip()
        
        # 엔터만 쳤을 경우 무시
        if not command_line:
            continue
            
        parts = command_line.split()
        cmd = parts[0].lower()

        # 명령어 검증 및 함수 호출 분기 (공백으로 나눈 요소 개수로 정확한 형식 체크)
        if cmd == "exit" and len(parts) == 1:
            print("시스템을 종료합니다.")
            break
            
        elif cmd == "add" and len(parts) == 3:
            title, quantity_str = parts[1], parts[2]
            library.add_book(title, quantity_str)
            
        elif cmd == "borrow" and len(parts) == 3:
            user, title = parts[1], parts[2]
            library.borrow_book(user, title)
            
        elif cmd == "return" and len(parts) == 3:
            user, title = parts[1], parts[2]
            library.return_book(user, title)
            
        elif cmd == "status" and len(parts) == 2:
            title = parts[1]
            library.status_book(title)
            
        elif cmd == "user" and len(parts) == 2:
            user = parts[1]
            library.user_info(user)
            
        elif cmd == "list" and len(parts) == 1:
            library.list_books()
            
        else:
            # 정해진 형식에서 벗어난 경우 (예: 공백이 포함된 제목 입력, 인자 개수 불일치 등)
            print("ERROR: 잘못된 명령어 형식이거나 알 수 없는 명령어입니다.")

if __name__ == "__main__":
    main()