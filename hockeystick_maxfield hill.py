# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 07:56:31 2023

@author: maxfield
"""

import pygame, simpleGE

class Back (simpleGE.BasicSprite):
    def __init__(self,scene): 
        super().__init__(scene)
        self.setImage("rink.png")
        self.setSize(640,480)
        self.x=320
        self.y=240


class Net(simpleGE.BasicSprite):
    def __init__(self,scene):
      super().__init__(scene)
      self.setImage("Net.png")
      self.setSize (100,100)
      self.x=600
      self.y=200


class Net2(simpleGE.BasicSprite):
    def __init__(self,scene):
      super().__init__(scene)
      self.setImage("Net2.png")
      self.setSize (100,100)
      self.x=50
      self.y=200



class Puck(simpleGE.SuperSprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("Puck.png")
        self.setSize(50,50)
        self.x=600
        self.y=200
    def checkEvents(self):
        if self.collidesWith(self.scene.net):
            self.scene.score += 1
            self.reset()
        if self.collidesWith(self.scene.net2):
            self.scene.score2 += 1
            self.reset()    
        if self.collidesWith(self.scene.skate):
            self.addForce(-.2,self.rotation)
        if self.collidesWith(self.scene.stick):
            self.addForce(.2, self.rotation)    
        
    def reset(self):
        self.x=320
        self.y=200
    
  




class Skate(simpleGE.SuperSprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.images={
            "up" : pygame.image.load("SkateStickUp.png"),
            "forward" : pygame.image.load ("SkateStick.png"),
            "backward" : pygame.image.load ("SkateStickRight.png"),
            "down" : pygame.image.load ("SkateStickDown.png")}
        self.imageMaster=self.images ["forward"]
        self.setAngle(90)
      
    def reset(self):
        self.x=520
        self.y=200


    def checkEvents(self):
        self.imageMaster = self.images["forward"]
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.rotateBy(5)
            self.imageMaster = self.images["down"]
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.rotateBy(-5)
            self.imageMaster = self.images["up"]
        if self.scene.isKeyPressed(pygame.K_UP):
            self.addForce(.2, self.rotation)
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.reset()
        if self.scene.isKeyPressed(pygame.K_b):
            self.setBoundAction(self.BOUNCE)      
      

class Stick(simpleGE.SuperSprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.images={
            "up" : pygame.image.load("StickSkateUp.png"),
            "forward" : pygame.image.load ("StickSkate.png"),
            "backward" : pygame.image.load ("StickSkateRight.png"),
            "down" : pygame.image.load ("SkateStickDown.png")}
        self.imageMaster=self.images ["forward"]
        self.setAngle(90)
      
    def reset(self):
        self.x=120
        self.y=200



      
    def checkEvents(self):
        self.imageMaster = self.images["forward"]
        if self.scene.isKeyPressed(pygame.K_a):
            self.rotateBy(5)
            self.imageMaster = self.images["down"]
        if self.scene.isKeyPressed(pygame.K_d):
            self.rotateBy(-5)
            self.imageMaster = self.images["up"]
        if self.scene.isKeyPressed(pygame.K_w):
            self.addForce(.2, self.rotation)
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.reset()
        if self.scene.isKeyPressed(pygame.K_b):
            self.setBoundAction(self.BOUNCE)
     
class Instruction (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines=[
        "Arrow keys and WASD to move and press B the add bounderies, then press space to set your player in position."    
            ]
        self.center=(320,240)
        self.size=(700,300)
        
        
class BtnQuit (simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.Text=("Quit")
        self.hide()
        
        
class BtnReset (simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text= "Reset"
        self.hide()


        
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
       
        self.puck=Puck(self)
        self.net=Net(self)
        self.net2=Net2(self)
        self.skate=Skate(self)
        self.stick=Stick(self)
        self.back=Back(self)
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Score: 0"
        self.lblScore.center = (50, 50)
        self.lblScore2 = simpleGE.Label()
        self.lblScore2.text = "Score: 0"
        self.lblScore2.center = (50, 100)
        self.score = 0
        

        self.lblTime = simpleGE.Label()
        self.lblTime.text = "Time left: 120"
        self.lblTime.center = (550, 50)
        self.timer = simpleGE.Timer()
        
        self.instructions= Instruction()
        self.btnQuit=BtnQuit()
        self.btnReset=BtnReset()
        
    


        
        self.sprites = [self.back, self.lblScore, self.lblScore2, self.lblTime, self.skate, self.stick, self.puck,self.net,self.net2, self.instructions,self.btnQuit,self.btnReset]
   
    
    def resetGame(self):
        self.instructions.hide()
        self.btnQuit.hide()
        self.btnReset.hide()
        self.menu=False
    



    def update(self):
        timeLeft = 120 - self.timer.getElapsedTime()
        if timeLeft < 0:
            self.stop()
        self.lblTime.text = f"Time left: {timeLeft:.2f}"
        self.lblScore.text = f"score: {self.score}"
        self.lblScore2.text = f"score: {self.score}"
        
        if self.instructions.clicked:
            self.resetGame()
            self.menu=True
        if self.btnQuit.clicked:
            self.stop()
            print(f"you scored {self.score}")
        if self.btnReset.clicked:
            self.resetGame()

        
        
        
        
def main():
    game = Game()
    game.setCaption("Hockey!")
    game.start()
   


if __name__ == "__main__":
    main()
            