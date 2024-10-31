import libs_64.__common as __common

def main():
    rc = jkrc.RC("192.168.0.127")
    rc.login()
    print(rc.set_tio_pin_mode(0, 0x11))

    mod_rtu_comm = {
        'chn_id': 1,
        'slave_id': 1,
        'baudrate': 9600, #115200 or 57600
        'databit': 8,
        'stopbit': 1,
        'parity': 0
    }
    print(rc.set_rs485_chn_comm(mod_rtu_comm))
    print(rc.get_rs485_chn_comm())
    print(rc.get_tio_pin_mode(0))
    rc.logout()

if __name__ == '__main__':
    __common.init_env()
    import jkrc

    main()