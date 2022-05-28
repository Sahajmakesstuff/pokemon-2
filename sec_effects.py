import random
import math

doubled=False

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
            opponent_mon.attIG=opponent_mon.attIG/2
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
        if eff_ch<=user_move.effect_chance and opponent_mon.hpIG!=0:
            opponent_mon.defeIG=opponent_mon.defeIG*2/3
            print(opponent_mon.name,"'s Defense Fell")
    
    #if accuracy dropped
    elif user_move.effect=="-acc":
        if eff_ch<=user_move.effect_chance:
            opponent_mon.accuracyIG=2/3*opponent_mon.accuracyIG    
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
        user_mon.spattIG=user_mon.spattIG*4/9
        print(user_mon.name,"'s Special Attack harshly Fell")
    
    elif user_move.effect=="paralysis" and opponent_mon.status=="none":
        if eff_ch<=user_move.effect_chance and opponent_mon.hp!=0:
            opponent_mon.status="paralysis"
            opponent_mon.spdIG=opponent_mon.spdIG/2
            print(opponent_mon.name,"was Paralysed")
    
    elif user_move.effect=="freeze" and opponent_mon.status=="none":
        if eff_ch<=user_move.effect_chance and opponent_mon.hp!=0:
            opponent_mon.status="freeze"
            opponent_mon.attIG=opponent_mon.attIG/2
            opponent_mon.spattIG=opponent_mon.spattIG/2
            print(opponent_mon.name,"was Frozen")
    
    elif user_move.effect=="confuse user":
        user_mon.attIG=user_mon.attIG*2/3
        user_mon.defeIG=user_mon.defeIG*2/3
        user_mon.spdIG=user_mon.spdIG*2/3
        user_mon.spattIG=user_mon.spattIG*2/3
        user_mon.spdefIG=user_mon.spdefIG*2/3
        print(user_mon.name,"was Confused")
    
    elif user_move.effect=="-spd":
        if eff_ch<=user_move.effect_chance and opponent_mon.hp!=0:
            opponent_mon.spdIG=opponent_mon.spdIG*2/3
            print(opponent_mon.name,"'s Speed Fell")
        
    elif user_move.effect=="omniboost":
        if eff_ch<=user_move.effect_chance:
            user_mon.attIG=user_mon.attIG*3/2
            user_mon.defeIG=user_mon.defeIG*3/2
            user_mon.spdIG=user_mon.spdIG*3/2
            user_mon.spattIG=user_mon.spattIG*3/2
            user_mon.spdefIG=user_mon.spdefIG*3/2

            print()
            print(user_mon.name,"'s Attack Rose")
            print(user_mon.name,"'s Defence Rose")
            print(user_mon.name,"'s Speed Rose")
            print(user_mon.name,"'s Special Attack Rose")
            print(user_mon.name,"'s Special Defence Rose")
    
    elif user_move.effect=="+user att":
        if eff_ch<=user_move.effect_chance:
            user_mon.attIG=user_mon.attIG*3/2
            print(user_mon.name,"'s Attack Rose")
    
    elif user_move.effect=="recharge":
        user_mon.recharge+=1
    
    elif user_move.effect=="kill user":
        user_mon.hpIG=0
    
    elif user_move.effect=="-spatt":
        if eff_ch<=user_move.effect_chance:
            opponent_mon.spattIG=opponent_mon.spattIG*2/3
            print(opponent_mon.name,"'s Special Attack Fell")
    
    elif user_move.effect=="-att":
        if eff_ch<=user_move.effect_chance:
            opponent_mon.attIG=opponent_mon.attIG*2/3
            print(opponent_mon.name,"'s Attack Fell")
    
    elif user_move.effect=="-defe -spdef user":
        user_mon.defeIG=user_mon.defeIG*2/3
        user_mon.spdefIG=user_mon.spdefIG*2/3
        print(user_mon.name,"'s Defence Fell")
        print(user_mon.name,"'s Special Defence Fell")
    
    elif user_move.effect=="-att -defe user":
        user_mon.att=user_mon.attIG*2/3
        user_mon.defe=user_mon.defeIG*2/3
        print(user_mon.name,"'s Attack Fell")
        print(user_mon.name,"'s Defence Fell")
    
    elif user_move.effect=="-spdef":
        if eff_ch<=user_move.effect_chance:
            opponent_mon.spdefIG=opponent_mon.spdefIG*2/3
            print(opponent_mon.name,"'s Special Defence Fell")
    
    elif user_move.effect=="confusion":
        if eff_ch<=user_move.effect_chance:
            opponent_mon.attIG=opponent_mon.attIG*2/3
            opponent_mon.defeIG=opponent_mon.defeIG*2/3
            opponent_mon.spdIG=opponent_mon.spdIG*2/3
            opponent_mon.spattIG=opponent_mon.spattIG*2/3
            opponent_mon.spdefIG=opponent_mon.spdefIG*2/3
            print(opponent_mon.name,"was Confused")
    
    elif user_move.effect=="double if status":
        if opponent_mon.status != "none":
            doubled=True
        
        else:
            doubled=False
    
    #if poisoned by move
    elif user_move.effect=="poison" and opponent_mon.status=="none":
        if eff_ch<=user_move.effect_chance and opponent_mon.hpIG!=0:
            opponent_mon.status="poison"
            opponent_mon.spattIG=opponent_mon.spattIG/2
            print(opponent_mon.name,"was Poisoned")
    
    elif user_move.effect=="double if poisoned":
        if opponent_mon.status=="poison":
            doubled=True
        else:
            doubled=False

    