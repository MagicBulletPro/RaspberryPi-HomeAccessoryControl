from django.shortcuts import render, get_object_or_404, redirect
from .models import Accessory
import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering


# Initialize GPIO pins for all accessories
accessories = Accessory.objects.all()
for accessory in accessories:
    GPIO.setup(accessory.pin_number, GPIO.OUT)
    if accessory.status:
        GPIO.output(accessory.pin_number, GPIO.HIGH)
    else:
        GPIO.output(accessory.pin_number, GPIO.LOW)


def accessory_list(request):
    accessories = Accessory.objects.all()
    return render(request, 'accessory_list.html', {'accessories': accessories})

def toggle_accessory(request, accessory_id):
    accessory = get_object_or_404(Accessory, id=accessory_id)
    accessory.status = not accessory.status
    accessory.save()
    accessory.pin_number
    GPIO.setup(accessory.pin_number, GPIO.OUT)
    if accessory.status:
        GPIO.output(accessory.pin_number, GPIO.HIGH)
    else:
        GPIO.output(accessory.pin_number, GPIO.LOW)

    return redirect('accessory_list')



