'''while: iterate as long as condition is true '''
count = 5
while count > 0:
    print(str(count))
    count -= 1
  

    
'''continue: continue this loop when if statement occur.'''
remain = 5
while remain > 0:
    print(str(remain))
    value = int(input("what?"))
    if value == 0:
        print("0 is inputted.")
        # ループに戻る
        continue;
    print(100 /value)
    remain -= 1
    
    
# continueで２重ループを抜ける
for i in range(8):  # 10回ループする。iには0から9が順番に代入される
    for j in range(8):  # 10回ループする。jには0から9が順番に代入される
        if (i == 3 and j == 4):
            break  # ifの条件が合えばbreakになり、内側のforループを抜ける
    else:  # 内側のforのelse節は内側ループが全部まわり切ったら実行される、つまり前の行のbreakで抜けた場合ここは実行されない
        continue  # 外側のforに対応するcontinue文、ここが実行されたら次の行のbreakには処理がいかず、外側のforの次のループにジャンプする
    # break  # 外側のforを抜ける
    print("(i,j)=({},{})".format(i, j))
    
    

'''
例外処理:
     try:                     
         通常処理                    
     except:
         例外ときの処理
       
       
例外処理は指定することができる： 
     try:
         通常処理
     except ValueError:
         例外ときの処理
'''
    
# Example:    
num = int(input("please input a number?"))

for i in range(1, num+1):
    if num % i == 0:
        if (i != 1 and i != num):
            print("this is not prime", num)
            # breakつけないと、出力結果が多くなる。
            break
    else:
        print("this is prime", num)
        # 出力結果を一つにするため、ループを中断する。
        break
            # break
