import logging

from micropython import const

from kmk.common.keycodes import Keycodes

KEY_UP_EVENT = const(1)
KEY_DOWN_EVENT = const(2)
INIT_FIRMWARE_EVENT = const(3)
NEW_MATRIX_EVENT = const(4)
HID_REPORT_EVENT = const(5)

logger = logging.getLogger(__name__)


def init_firmware(keymap, row_pins, col_pins, diode_orientation):
    return {
        'type': INIT_FIRMWARE_EVENT,
        'keymap': keymap,
        'row_pins': row_pins,
        'col_pins': col_pins,
        'diode_orientation': diode_orientation,
    }


def key_up_event(row, col):
    return {
        'type': KEY_UP_EVENT,
        'row': row,
        'col': col,
    }


def key_down_event(row, col):
    return {
        'type': KEY_DOWN_EVENT,
        'row': row,
        'col': col,
    }


def new_matrix_event(matrix):
    return {
        'type': NEW_MATRIX_EVENT,
        'matrix': matrix,
    }


def hid_report_event():
    return {
        'type': HID_REPORT_EVENT,
    }


def matrix_changed(new_matrix):
    def _key_pressed(dispatch, get_state):
        state = get_state()
        # Temporarily preserve a reference to the old event
        # We do fake Redux around here because microcontrollers
        # aren't exactly RAM or CPU powerhouses - the state does
        # mutate in place. Unfortunately this makes reasoning
        # about code a bit messier and really hurts one of the
        # selling points of Redux. Former development versions
        # of KMK created new InternalState copies every single
        # time the state changed, but it was sometimes slow.
        old_matrix = state.matrix
        old_keys_pressed = state.keys_pressed

        dispatch(new_matrix_event(new_matrix))

        with get_state() as new_state:
            for ridx, row in enumerate(new_state.matrix):
                for cidx, col in enumerate(row):
                    if col != old_matrix[ridx][cidx]:
                        if col:
                            dispatch(key_down_event(
                                row=ridx,
                                col=cidx,
                            ))
                        else:
                            dispatch(key_up_event(
                                row=ridx,
                                col=cidx,
                            ))

        with get_state() as new_state:
            if old_keys_pressed != new_state.keys_pressed:
                dispatch(hid_report_event())

            if Keycodes.KMK.KC_RESET in new_state.keys_pressed:
                try:
                    import machine
                    machine.bootloader()
                except ImportError:
                    logger.warning('Tried to reset to bootloader, but not supported on this chip?')

    return _key_pressed