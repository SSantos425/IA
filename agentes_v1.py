from multiprocessing import set_forkserver_preload
from operator import index, length_hint
from posixpath import split
import time
import math
import asyncio
from unittest import case
from numpy import flip
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class DummyAgent(Agent):
    class Soma(CyclicBehaviour):
        async def on_start(self):
            print("Starting Manager . . .")          
            
           
            #teste_str2 = "23 + 12 – 55 + (2 + 4) – 8 / 2^2"
            teste_str1 = "23 + 12"
            self.a = teste_str1.split()
          
            

        async def run(self):            
            def soma():
                x = self.a.index(item)              
                soma = int(self.a[x-1]) + int(self.a[x+1])

                print(soma)
            
            def sub():
                x = self.a.index(item)    

                sub = int(self.a[x-1]) - int(self.a[x+1])
                print(sub)

            def multi():
                x = self.a.index(item)    

                multi = int(self.a[x-1]) * int(self.a[x+1])
                print(multi)

            def div():
                x = self.a.index(item)    

                multi = int(self.a[x-1]) / int(self.a[x+1])
                print(multi)

            def expo():
                x = self.a.index(item)   

                expo = int(self.a[x-1]) ** int(self.a[x+1])
                print(expo)

            def sqrt():
                x = self.a.index(item)   

                sqrt = int(self.a[x+1])**0.5
                print(sqrt)



            opcoes = { 1:soma, 2:sub, 3:multi, 4:div, 5:expo, 6:sqrt}
            for item in self.a:
                if item == '+':
                   opcoes.get(1)()

                if item == '-':
                    opcoes.get(2)()  

                if item == '*':
                    opcoes.get(3)()    

                if item == '/':
                    opcoes.get(4)()

                if item == '^':
                    opcoes.get(5)()

                if item == '**':
                    opcoes.get(6)()           
            await asyncio.sleep(1)

    async def setup(self):
        print("Agent starting . . .")
        b = self.Soma()
        self.add_behaviour(b)

if __name__ == "__main__":
    dummy = DummyAgent("samuel@jabbers.one", "1357")
    future = dummy.start()
    future.result()

    print("Wait until user interrupts with ctrl+C")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
    dummy.stop()