import random
def deal_cards():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card=random.choice(cards)
    return card

user_cards = []
comp_cards = []
is_game_over = False
#to run the cards inside them 
for i in range(2):
    new_card = deal_cards()
    user_cards.append(deal_cards())
    comp_cards.append(deal_cards())


def calculate_score(cards):
        if( sum(cards) ==21 and len(cards) ==2) :
            return 0
        
        if 11 in cards and sum(cards) == 21 :
            cards.remove(11)
            cards.append(1)
            
        return sum(cards)
def compare(user_score , comp_score):
    if user_score==comp_score:
        return "draw"
    elif comp_score==0 :
        return "you lose "
    elif user_score>21 :
        return "You went over you lose"
    elif comp_score >21 :
        return "Opponent went over , you win"
    
    else :
        return "you win"



user_score =calculate_score(user_cards) 
comp_score = calculate_score(comp_cards)

while is_game_over==False :
    user_score =calculate_score(user_cards) 
    comp_score = calculate_score(comp_cards)
    print(f"Your cards:{user_cards} Score ={user_score}")

    print(f"Comp cards:{comp_cards} Score ={comp_score}")
   # print(f"The comparision {compare(user_score,comp_score)}")
    if user_score == 0 or comp_score ==0 or user_score >21 :
        is_game_over = True 
    else:
        user_deal=input("y for another card , n for pass ")
        if user_deal == 'y' :
            user_cards.append(deal_cards())
        else :
            is_game_over=True
        
        
while comp_score != 0 and  comp_score <17:
    comp_cards.append(deal_cards())
    comp_score= calculate_score(comp_cards)


print(f"Your Final cards:{user_cards} FINAL Score ={user_score}")

print(f"Your FINAL cards:{comp_cards} FINAL Score ={comp_score}")

print(compare(user_score,comp_score))