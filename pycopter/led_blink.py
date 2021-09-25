import time
from time import sleep

# import serial
import serial
from pyfirmata import Arduino, util, STRING_DATA


def _map(x, in_min, in_max, out_min, out_max) -> float:
    """
    :param x:
    :param in_min:
    :param in_max:
    :param out_min:
    :param out_max:
    :return:
    """
    print(x)
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def read_angle(initial, **kwargs):
    y = _map(initial, kwargs['in_min'], kwargs['in_max'], 0.00, 90.00)
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter('Angle'))
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(f'{y} degrees'))
    print(y, " degrees")
    return y


def set_pwm(val, **kwargs):
    sig = _map(req_deg, 0.00, 90.00, 0.2, 0.5)
    print(sig, "pwm signal")
    return sig


def error_correction(analog_sig):
    initial_position = initial_pos
    final_position = final_pos

    # if any([analog_sig < 0, analog_sig < initial_pos]):
    #     print('-' * 10)
    #     print(f'Correcting an error of {analog_sig}')
    #     print('-' * 10)
    #
    #     if analog_sig < 0:
    #         analog_sig = initial_pos - analog_sig
    #         initial_position = initial_pos + analog_sig
    #         final_position = final_pos + analog_sig
    #
    #     elif all([analog_sig < initial_pos, analog_sig > 0.00]):
    #         analog_sig = analog_sig
    #         initial_position = analog_sig
    #         final_position = final_pos + analog_sig
    #     sleep(1.5)
    return analog_sig, initial_position, final_position


def stabilize(**kwargs):
    pass


if __name__ == '__main__':
    # constants
    global initial_pos, final_pos

    u = None
    # required angle where rotation should happen
    req_deg: int = 60
    new_si = None
    si = 0.00
    p = 0

    initial_pos = 0.9042
    final_pos = 0.607

    # initializing arduino board with port as com 4
    board = Arduino('com4')
    print('-' * 20, 'preparing arduino uno board to load in 100 milliseconds', '-' * 20)
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(' Initializing '))
    # waiting for the board to be ready
    sleep(.1)
    print('board ready')
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(' Board is Ready '))

    it = util.Iterator(board)
    it.start()
    board.analog[0].enable_reporting()

    # setting pin  digital pin 3 as a pwm output
    pwm = board.get_pin('d:3:p')

    while True:
        if u is None:
            print('-' * 20, 'waiting for analog response', '-' * 20)
            sleep(1.5)

        # reading analog value from the controller
        u = board.analog[0].read()
        print(u)

        angle = read_angle(u, **dict(in_min=initial_pos, in_max=final_pos))

        if new_si is None:
            si = set_pwm(req_deg)
            pwm.write(si)
            p += 1

        if p > 0:
            if req_deg != angle:
                if diff := req_deg - angle:
                    print('-' * 20, f'correcting error of {diff} degrees', '-' * 20)
                    if diff < 0:
                        si += set_pwm(-diff)
                    else:
                        si -= set_pwm(diff)
                    # new_si = si
        if si:
            pwm.write(si)
