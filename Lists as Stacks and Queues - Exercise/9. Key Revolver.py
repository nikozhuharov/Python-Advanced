from collections import deque
bullet_price = int(input())
barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
initial_number_bullets = len(bullets)
success = False
current_barrel = barrel

while bullets:
    bullet = bullets[-1]
    lock = locks[0]
    if lock >= bullet:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    bullets.pop()
    current_barrel -= 1
    if current_barrel == 0 and bullets:
        print("Reloading!")
        current_barrel = barrel
    if not locks:
        print(f"{len(bullets)} bullets left. Earned ${intelligence- ((initial_number_bullets-len(bullets))*bullet_price)}")
        success = True
        break

if not success:
    print(f"Couldn't get through. Locks left: {len(locks)}")



