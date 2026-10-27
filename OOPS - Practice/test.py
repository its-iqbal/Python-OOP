# class SmartDevice:
#     total_devices = 0  # We want to track every device created

#     def __init__(self, name):
#         self.name = name
#         self.__is_on = False
#         SmartDevice.total_devices += 1

#     def turn_on(self):
#         self.__is_on = True

#     def __str__(self):
#         # 🐛 Bug 2 is hiding here
#         return f"Smart Device: {self.name}"

# class SmartTV(SmartDevice):
#     def __init__(self, name, channel):
#         super().__init__(name)
#         self.channel = channel

# # --- Testing the System ---
# tv = SmartTV("Living Room TV", 5)
# tv1 = SmartTV("Dining Room TV", 6)


# # If we run this next line, the program crashes with an AttributeError!
# print(tv, "\n", tv1)

# print(tv.total_devices)


class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

b=B()