import random


my_money = 1000


print("--- 🎰 레지락 카지노: 인생역전 77배 & 구걸 에디션 🎰 ---")
print("1회 성공 시 77배! 하지만 실패해서 파산하면... 방법은 하나뿐입니다.")


while True:
    if my_money > 0:
        print(f"\n[현재 잔액: {my_money}원]")
       
        try:
            bet_input = input("베팅 금액 (0은 종료): ")
            if bet_input == '0': break
            bet = int(bet_input)
           
            if bet > my_money:
                print("잔액 부족! 무리한 베팅은 파산의 지름길입니다.")
                continue
               
            limit = int(input("도전 횟수 설정 (1~10회): "))
            if not (1 <= limit <= 10):
                print("1회에서 10회 사이만 고르세요.")
                continue
               
            # 배율 로직 수정: 1회 77배, 10회 1.0배
            if limit == 1:
                multiplier = 77.0
            elif limit == 10:
                multiplier = 1.0
            else:
                multiplier = round(3.2 - (limit * 0.2), 1)
           
            secret_number = random.randint(1, 100)
            attempts = 0
            success = False


            print(f"💰 {limit}회 성공 시 배율: [{multiplier}배] 적용!")


            while attempts < limit:
                remaining = limit - attempts
                guess_input = input(f"\n[{attempts + 1}/{limit}] 남은 기회 {remaining}번... 숫자: ")
               
                try:
                    guess = int(guess_input)
                except ValueError:
                    print("숫자만 입력하세요! 기회 1번 날아갑니다.")
                    attempts += 1
                    continue
                   
                attempts += 1


                if guess < secret_number:
                    if remaining > 1:
                        print("UP! 아직은 웃음이 나오시죠?")
                    else:
                        print("UP!!! 마지막입니다. 여기서 틀리면 돈 날리는 거예요!")
                elif guess > secret_number:
                    if remaining > 1:
                        print("DOWN! 너무 높아요. 침착하게 생각하세요.")
                    else:
                        print("DOWN!!! 이번에 틀리면 전액 몰수입니다!")
                else:
                    success = True
                    break
           
            if success:
                total_multiplier = multiplier
                if '7' in str(secret_number):
                    print("\n🎊 [JACKPOT] 숫자 7 포함! 보너스 +2.0배 추가!")
                    total_multiplier += 2.0
                if attempts == 1:
                    print("🎊 [SUPER JACKPOT] 이걸 진짜 맞히네? 홀인원 보너스 +5.0배 추가!")
                    total_multiplier += 5.0


                reward = int(bet * total_multiplier)
                my_money += (reward - bet)
                print(f"✨ 성공! {reward}원 획득! (현재 잔액: {my_money}원)")
            else:
                my_money -= bet
                print(f"\n💀 몰수! 정답은 {secret_number}였습니다.")
                if my_money <= 0:
                    print("잔액이 0원이 되었습니다. 게임 오버... 인줄 알았지?")


        except ValueError:
            print("올바른 값을 입력하세요.")


    # 파산 상태 체크 및 회생 시스템
    if my_money <= 0:
        print("\n[시스템: 파산 상태 감지]")
        print("돈이 하나도 없으시네요? 불쌍하니까 기회를 드리죠.")
        print("'나는 빡빡이다'를 정확히 입력하면 100원을 지급해드립니다.")
       
        recovery = input("입력: ")
        if recovery == "나는 빡빡이다":
            my_money = 100
            print("✨ [충전 완료] 자존심과 바꾼 100원이 입금되었습니다. 다시는 올인하지 마세요.")
        else:
            print("❌ 오타가 났거나 자존심이 허락하지 않으시나 보네요. 그럼 진짜 끝입니다.")
            break


print(f"\n최종 자산 {my_money}원으로 마무리하겠습니다.")
