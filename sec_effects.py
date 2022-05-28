import random
import math

def sec_eff(user_move,user_mon,opponent_mon,damage):
    #var for effect chance checking
    eff_ch=random.randrange(1,101)

    #variable for recoil
    recoil=0
    hp_regained=0

    #if burned by move
    if user_move.effect=="Burn" and opponent_mon.status=="none":
        if eff_ch<=user_move.effect_chance and opponent_mon.hp!=0:
            opponent_mon.status="Burn"
            opponent_mon.att=opponent_mon.att/2
            print(opponent_mon.name,"was Burned")

    #if suffer recoil
    elif user_move.effect=="Recoil":
        recoil=math.ceil(damage/3)
        if recoil>user_mon.hpIG:
            recoil=user_mon.hpIG

        user_mon.hp=user_mon.hpIG-recoil
        print(user_mon.name,"took",recoil,"HP of recoil")
    
    #if defense dropped
    elif user_move.effect=="-defe":
        if eff_ch<=user_move.effect_chance and opponent_mon.hp!=0:
            opponent_mon.defe=opponent_mon.defe*2/3
            print(opponent_mon.name,"'s Defense Fell")
    
    #if accuracy dropped
    elif user_move.effect=="-acc":
        if eff_ch<=user_move.effect_chance:
            opponent_mon.accuracy=2/3*opponent_mon.accuracy    
            print(opponent_mon.name,"'s Accuracy Fell")
    
    #if flinched
    elif user_move.effect=="flinch":
        if eff_ch<=user_move.effect_chance:
            opponent_mon.flinch=True
    
    #if draining move
    elif user_move.effect=="heal from opp":
        hp_regained=math.ceil(damage/2)

        difference=user_mon.hp-user_mon.hpIG

        user_mon.hpIG=user_mon.hpIG+hp_regained
        if user_mon.hpIG>user_mon.hp:
            user_mon.hpIG=user_mon.hp
            hp_regained=difference
        
        print(user_mon.name,"Drained",hp_regained,"HP From",opponent_mon.name)
    
    elif user_move.effect=="-2 spatt user":
        user_mon.spatt=user_mon.spatt*4/9
        print(user_mon.name,"'s Special Attack harshly Fell")
    
    elif user_move.effect=="paralysis" and opponent_mon.status=="none":
        if eff_ch<=user_move.effect_chance and opponent_mon.hp!=0:
            opponent_mon.status="paralysis"
            opponent_mon.spd=opponent_mon.spd/2
            print(opponent_mon.name,"was Paralysed")
    
    elif user_move.effect=="freeze" and opponent_mon.status=="none":
        if eff_ch<=user_move.effect_chance and opponent_mon.hp!=0:
            opponent_mon.status="freeze"
            opponent_mon.att=opponent_mon.att/2
            opponent_mon.spatt=opponent_mon.spatt/2
            print(opponent_mon.name,"was Frozen")
    