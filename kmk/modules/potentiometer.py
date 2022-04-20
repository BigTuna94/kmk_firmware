import busio
from analogio import AnalogIn
from supervisor import ticks_ms

from kmk.modules import Module

class BasePotentiometer:
    def __init__(self, is_inverted=False):
        self.is_inverted = is_inverted
        self.read_pin = None
        self._direction = None
        self._pos = 0
        self._timestamp = ticks_ms()

        self._truncate_bits = 6
        
        # callback function on events. Needs to be defined externally
        self.on_move_do = None
        
    def get_state(self):
        return {
            'direction': self.is_inverted and -self._direction or self._direction,
            'position': self.is_inverted and -self._pos or self._pos,
        }
        
    def get_pos(self):
        # Debounce...
        # AnalogRead always reports 16 bit values - truncate to 6 to de-noise
        # convert to percentage and round to quarter of a percent
        
        readings = [(self.read_pin.value >> (16 - self._truncate_bits)) for i in range(3)]
        reading = sum(readings) / len(readings)

        
        # reading = self.read_pin.value >> 10
        dec_val = reading / (pow(2, self._truncate_bits) - 1)

        # new_pos = round(dec_val * 4, 1) / 4
        new_pos = round(dec_val, 2)

        return int(new_pos * 127)

    def update_state(self):    
        self._direction = 0
        new_pos = self.get_pos()
        if abs(new_pos - self._pos) > 2:
            # movement detected!
            if new_pos > self._pos:
                self._direction = 1
            else:
                self._direction = -1
            self._pos = new_pos
            if self.on_move_do is not None:
                self.on_move_do(self.get_state())
              
class GPIOPotentiometer(BasePotentiometer):
    def __init__(self, pin, move_callback, is_inverted=False):
        super().__init__(is_inverted)
        self.read_pin = AnalogIn(pin)
        self._pos = self.get_pos()
        self.cb = move_callback
        self.on_move_do = lambda state: self.cb(state)

class PotentiometerHandler(Module):
    def __init__(self):
        self.potentiometers = []
        self.pins = None
    
    def on_runtime_enable(self, keyboard):
        return

    def on_runtime_disable(self, keyboard):
        return

    def during_bootup(self, keyboard):
        if self.pins:
            for args in self.pins:
                self.potentiometers.append( GPIOPotentiometer(*args) )
        return
    
    def before_matrix_scan(self, keyboard):
        '''
        Return value will be injected as an extra matrix update
        '''
        for potentiometer in self.potentiometers:
            potentiometer.update_state()

        return keyboard

    def after_matrix_scan(self, keyboard):
        '''
        Return value will be replace matrix update if supplied
        '''
        return

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return