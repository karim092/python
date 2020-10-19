import time

class TrafficLight:
    color = ['красный', 'желтый', 'зеленый']

    def running(self):
        print(TrafficLight.color[0])
        time.sleep(7)
        print(TrafficLight.color[1])
        time.sleep(2)
        print(TrafficLight.color[2])
        time.sleep(5)

a = TrafficLight()
a.running()