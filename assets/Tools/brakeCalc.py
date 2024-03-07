import numpy as np
import skfuzzy as brain
from skfuzzy import control as c

dist = c.Antecedent(np.arange(0, 50, 1), 'dist')
speed = c.Antecedent(np.arange(0, 100, 1), 'speed')
brakes_pressure = c.Consequent(np.arange(0, 100, 1), 'brakes_pressure')

dist['very near'] = brain.trimf(dist.universe, [0, 0, 10])
dist['near'] = brain.trimf(dist.universe, [5, 15, 25])
dist['far'] = brain.trimf(dist.universe, [20, 30, 40])
dist['very far'] = brain.trimf(dist.universe, [35, 50, 50])

speed['very slow'] = brain.trapmf(speed.universe, [0, 0, 20, 30])
speed['slow'] = brain.trapmf(speed.universe, [20, 30, 45, 55])
speed['fast'] = brain.trapmf(speed.universe, [45, 55, 70, 80])
speed['very fast'] = brain.trapmf(speed.universe, [70, 80, 100, 100])

brakes_pressure['very low'] = brain.trimf(brakes_pressure.universe, [0, 20, 40])
brakes_pressure['low'] = brain.trimf(brakes_pressure.universe, [20, 40, 60])
brakes_pressure['high'] = brain.trimf(brakes_pressure.universe, [40, 60, 80])
brakes_pressure['very high'] = brain.trimf(brakes_pressure.universe, [60, 100, 100])

rule1 = c.Rule(dist['very near'] & speed['very slow'], brakes_pressure['very high'])
rule2 = c.Rule(dist['near'] & speed['very slow'], brakes_pressure['very low'])
rule3 = c.Rule(dist['very near'] & speed['slow'], brakes_pressure['very high'])
rule4 = c.Rule(dist['near'] & speed['slow'], brakes_pressure['low'])
rule5 = c.Rule(dist['far'] & speed['slow'], brakes_pressure['very low'])
rule6 = c.Rule(dist['very near'] & speed['fast'], brakes_pressure['very high'])
rule7 = c.Rule(dist['near'] & speed['fast'], brakes_pressure['low'])
rule8 = c.Rule(dist['far'] & speed['fast'], brakes_pressure['very low'])
rule9 = c.Rule(dist['very near'] & speed['very fast'], brakes_pressure['very high'])
rule10 = c.Rule(dist['near'] & speed['very fast'], brakes_pressure['high'])
rule11 = c.Rule(dist['far'] & speed['very fast'], brakes_pressure['low'])
rule12 = c.Rule(dist['very far'] & speed['very fast'], brakes_pressure['very low'])

brake_c = c.ControlSystem([
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6,
    rule7,
    rule8,
    rule9,
    rule10,
    rule11,
    rule12])
brakes = c.ControlSystemSimulation(brake_c)


def placeholder():
    return "Sorry, this tool is currently indev"


def main():
    while True:
        v = int(input("Enter Speed (0-100 km/h) : "))
        s = int(input("Enter Distance (m) : "))

        if v / 2 <= s:
            print("No need to press brakes")
        else:
            brakes.input['speed'] = v
            brakes.input['dist'] = s

            brakes.compute()
            print("Brake Pressure (%): ", brakes.output['brakes_pressure'])
            print("New Speed Level: ", v - (v * brakes.output['brakes_pressure'] / 100))

        print("Rerun?")
        inp = input("+/-:")
        if inp == "+":
            continue
        else:
            break
