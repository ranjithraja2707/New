import faulthandler
faulthandler.enable()
import faulthandler

def buggy_function():
    faulty_list = [1, 2, 3]
    print(faulty_list[10])  # This will trigger a segmentation fault

faulthandler.enable()

try:
    buggy_function()
except Exception as e:
    print("Exception occurred:", e)
