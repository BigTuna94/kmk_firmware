import board

from kb import KMKKeyboard

from kmk.extensions.RGB import RGB, AnimationModes
from kmk.modules.
from kmk.keys import KC
from kmk.modules.potentiometer import PotentiometerHandler
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

rgb_ext = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=keyboard.rgb_num_pixels, animation_mode=AnimationModes.STATIC)
keyboard.extensions.append(rgb_ext)

_______ = KC.TRNS
XXXXXXX = KC.NO

FN1 = KC.MO(1)
FN2 = KC.MO(2)
FN3 = KC.MO(3)
MIDI = KC.TG(4)

RGB_TOG = KC.RGB_TOG
RAINBOW = KC.RGB_MODE_RAINBOW


def slider_1_handler(state):
    print(state)

def slider_2_handler(state):
    print(state)
    
def slider_3_handler(state):
    print(state)

faders = PotentiometerHandler(
    (board.RV1, slider_1_handler, False),
    (board.RV2, slider_2_handler, False),
    (board.RV3, slider_3_handler, False),
)
keyboard.modules.append(faders)


keyboard.keymap = [
    [   # Base Layer
        KC.ESC, KC.TILD,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.BSLS,  KC.DEL,     KC.MINS, KC.EQUAL,
             KC.TAB,       KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.BACKSPACE,         KC.LBRC, KC.RBRC,
             KC.LCTRL,     KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,  KC.ENTER,   KC.QUOT, KC.HOME,
             KC.LSFT,      KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,      KC.UP,           KC.END,
                 FN1,      KC.LGUI,  KC.LALT,            KC.SPC,             KC.ENTER,           KC.RGUI,  KC.RALT,  FN2,          KC.LEFT,  KC.DOWN,  KC.RIGHT,
    ],
    
    [   # FN1 Layer
        _______, _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,    _______, _______,
             _______,      _______,  _______,  RGB_TOG,  RAINBOW,  _______,  _______,  _______,  _______,  _______,  _______,  _______,              _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,    _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,      _______,         _______,
             XXXXXXX,      _______,  _______,            _______,            _______,            _______,  _______,  FN2,          _______,  _______,  _______,
    ],
    
    [   # FN2 Layer
        _______, _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,    _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,              _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,    _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,      _______,         _______,
                 FN3,      _______,  _______,            _______,            _______,            _______,  _______,  XXXXXXX,      _______,  _______,  _______,
    ],
    
    [   # FN3 Layer
        _______, _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,    _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,              _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,    _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  MIDI,     _______,  _______,  _______,  _______,      _______,         _______,
             XXXXXXX,      _______,  _______,            _______,            _______,            _______,  _______,  XXXXXXX,      _______,  _______,  _______,
    ],
    
    [   # MIDI Layer
          MIDI,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,    _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,              _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,    _______, _______,
             _______,      _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,      _______,         _______,
             XXXXXXX,      _______,  _______,            _______,            _______,            _______,  _______,  XXXXXXX,      _______,  _______,  _______,
    ],
]
]


if __name__ == '__main__':
    keyboard.go()
