'''
class 선언(도서관시스템)
책제목과 수량이 키벨류값인 self.books와 사용자 이름과 대출한 책제목 리스트가 키벨류값인 self.users 설정
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
        '''
        isdigit 함수는 모든 문자가 숫자(0~9)일 때 True를 반환하는 함수
        소수점, 부호가 있으면 False를 반환
        그러나 윗첨자, 아래첨자 등도 True로 인식
        isdigit -> isdecimal로 변경
        '''
        if not quantity_str.isdecimal():
            print("ERROR: 수량은 0 이상의 정수여야 합니다.")
            return
        '''
        수량을 str로 인식되었기 때문에 사용할 때 int형 변환
        '''
        quantity = int(quantity_str)
        '''
        이미 있는 책의 경우 수량만 추가, 없는 책의 경우 제목 추가 및 수량 추가
        '''
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"[성공] '{title}' 도서가 {quantity}권 추가되었습니다. (현재 총 {self.books[title]}권)")

    '''
    책 목록에 없는 책을 입력한 경우 ERROR 메세지 출력
    이미 빌리고 있는 책을 또 입력한 경우 ERROR 메세지 출력
    남아있는 책이 없을 경우 ERROR 메세지 출력
    
    그 외 정상 대출 처리
    '''
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

    '''
    도서관에 없는 책을 반납하는 경우,
    대출한 적이 없는 경우, 대출 중이 아닌 책을 반납하려는 경우
    ERROR 메세지 출력
    
    그 외 반납 처리
    '''
    def return_book(self, user, title):
        if title not in self.books:
            print("ERROR: 해당 도서관에 존재하지 않는 도서입니다.")
            return
            
        if user not in self.users:
            print("ERROR: 등록되지 않은 사용자입니다.")
            return
        
        if title not in self.users[user]:
            print("ERROR: 대출 중이 아닌 책입니다.")
            return

        # 반납 처리
        self.books[title] += 1
        self.users[user].remove(title)
        print(f"[성공] {user}님이 '{title}' 도서를 반납하셨습니다.")

    '''
    책 목록에 있는 경우 수량 확인
    없는 경우 ERROR 메세지 출력
    '''
    def status_book(self, title):
        if title not in self.books:
            print("ERROR: 해당 도서관에 존재하지 않는 도서입니다.")
            return
        
        print(f"[{title}] 남은 수량: {self.books[title]}")

    '''
    사용자 목록(대출 기록)이 없는 경우, 현재 대출 목록이 없는 경우 EMPTY
    그 외 대출 목록 보여줌
    '''
    def user_info(self, user):
        if user not in self.users:
            print("EMPTY: 등록되지 않은 사용자입니다.")
            return
        if not self.users[user]:
            print("EMPTY: 대출 목록이 없습니다.")
            return
            
        print(f"[{user}님의 대출 목록]")
        for book in self.users[user]:
            print(f"- {book}")
    
    '''
    책이 아예 없는 경우가 아니면 도서 목록 보여줌
    '''
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
        '''
        입력값에 따라 작동하도록 설정
        공백에 따라 split한 값의 list를 받아 직접 함수에 넣어줌
        예외처리를 위해 정해진 규격 외에 모든 입력을 오류로 간주(else)
        '''
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

'''
직접 실행 되었을 때만 작동하도록 하는 코드
'''
if __name__ == "__main__":
    main()